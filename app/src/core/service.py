from langchain_google_genai import GoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv

load_dotenv('app/src/shared/.env')


def create_rag_chain(llm_model: str = 'gemini-1.5-pro', temperature: float = 0.0):
    """
    Initializes the language model and vectorstore, and returns a chain for generating responses.

    Returns:
        A chain for generating responses, which includes a context retriever, prompt, language model, and output parser.
    """
    embed = OpenAIEmbeddings(
        # Initializes an OpenAI embeddings model.
        model="text-embedding-3-large")
    # Initializes a Google Generative AI model.
    model = GoogleGenerativeAI(model=llm_model, temperature=temperature)

    # Directory where the vectorstore will be persisted.
    persist_directory = "vectorstore_db_openai_v2"

    # Initializes the vectorstore.
    vectorstore = Chroma(  # Initializes the vectorstore again with different parameters.
        # Name of the collection in the vectorstore.
        collection_name="RAPTOR_vectorstore",
        # Embeddings function used for the vectorstore.
        embedding_function=embed,
        # Directory where the vectorstore will be persisted.
        persist_directory=persist_directory)

    # Define a retriever for the vectorstore.
    # Creates a retriever for the vectorstore.
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    template = """
    Você é um assistente chatbot para tarefa de question answering(QA). Se o contexto nao for relevante para a pergunta, não informe essa informação.Responda à pergunta baseado no seguinte contexto:
    {context}

    Responda a seguinte pergunta:
    Pergunta: {question}
    """  # Template for the prompt.
    prompt = ChatPromptTemplate.from_template(
        template)  # Creates a prompt from the template.

    def format_docs(docs):  # Function to format the documents.
        return "\n\n".join(doc.page_content for doc in docs)

    rag_chain = (  # Chain for generating responses.
        # Context retriever and question.
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt  # Prompt.
        | model  # Language model.
        | StrOutputParser()  # Output parser.
    )  # Returns the chain for generating responses.

    return rag_chain  # Returns the chain for generating responses.
