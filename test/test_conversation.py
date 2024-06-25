from langchain_google_genai import GoogleGenerativeAI
from langchain_openai import OpenAIEmbeddings
# vectodb
from langchain_community.vectorstores import Chroma

# prompt engeneering
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables.history import RunnableWithMessageHistory


from langchain_community.chat_message_histories import ChatMessageHistory


from langchain_core.chat_history import BaseChatMessageHistory


from langchain.chains.history_aware_retriever import create_history_aware_retriever

from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain


from dotenv import load_dotenv

load_dotenv('app/src/shared/.env')


def create_rag_chain(llm_model: str = 'gemini-1.5-pro', temperature: float = 0.0):
    """
    Initializes the language model and vectorstore, and returns a chain for generating responses.

    Returns:
        A chain for generating responses, which includes a context retriever, prompt, language model, and output parser.
    """
    embed = OpenAIEmbeddings(model="text-embedding-3-large")
    model = GoogleGenerativeAI(model=llm_model, temperature=temperature)

    persist_directory = "vectorstore_db"
    vectorstore = Chroma(
        collection_name="RAPTOR_vectorstore",
        embedding_function=embed,
        persist_directory=persist_directory
    )

    retriever = vectorstore.as_retriever()

    contextualize_system_prompt = """Dado um histórico de bate-papo e a última pergunta do usuário \
    que pode fazer referência ao contexto no histórico de bate-papo, formule uma pergunta autônoma \
    que possa ser compreendida sem o histórico do bate-papo. NÃO responda à pergunta, \
    apenas reformule-a se necessário e, caso contrário, devolva-a como está."""

    contextualize_system_prompt = ChatPromptTemplate.from_messages(
        [
            ("ai", contextualize_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )

    history_aware_retriever = create_history_aware_retriever(llm=model,
                                                             retriever=retriever,
                                                             prompt=contextualize_system_prompt)

    template = """Você é um assistente chamado Spark e sua função é responder dúvidas e questionamentos relacionadas as instalações elétricas brasileiras \
    com base no contexto, o qual pode incluir textos e/ou tabelas referentes as normas brasileiras (NBRs): \
    {context}
    """

    prompt = ChatPromptTemplate.from_messages([("ai", template),
                                               MessagesPlaceholder(
                                                   "chat_history"),
                                               ("human", "{input}")])

    question_answer_chain = create_stuff_documents_chain(model, prompt)
    rag_chain = create_retrieval_chain(
        history_aware_retriever, question_answer_chain)

    store = {}
    session_id = "default_session_id"

    def get_session_history(session_id: str) -> BaseChatMessageHistory:
        if session_id not in store:
            store[session_id] = ChatMessageHistory()
        return store[session_id]

    conversational_rag_chain = RunnableWithMessageHistory(
        rag_chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="chat_history",
        output_messages_key="answer",
    )

    return conversational_rag_chain
