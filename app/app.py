"""
Spark Chatbot Application
=========================

This file contains the main logic for the Spark chatbot application.
The chatbot is built using the `RAG` (Retrieval-Augmented Generation) model,
which is a state-of-the-art language model. The chatbot allows users to ask 
questions and provides answers based on the information it has been trained on.

The application is built using the Streamlit framework, 
which provides a user-friendly interface for interacting 
with the chatbot.

Author: Nathan Souza
"""

from src.core.service import create_rag_chain
# from src.shared.utils.utils import clear_chat_history
import streamlit as st


def clear_chat_history():
    """
    Clears the chat history stored in the Streamlit session state.
    """
    st.session_state.messages = []


# ================================================================

st.set_page_config(
    page_title="Chatbot Spark",
    page_icon="⚡"
)


st.title('Pergunte ao assistente Spark!⚡')

with st.sidebar:

    LOGO_PATH = "app/src/shared/style/images/ufrn-logo.png"
    st.image(LOGO_PATH, use_column_width=True)

    st.markdown("# Sobre o Projeto")
    st.markdown("""
    Este projeto é um Trabalho de Conclusão de Curso (TCC) desenvolvido por [Nathan Souza](https://github.com/nathansouz4).

    - **Instituição:** Universidade Federal do Rio Grande do Norte
    - **Curso:** Engenharia Elétrica
    - **Orientador:** Allan de Medeiros Martins
    """)

    temperature = st.sidebar.slider(
        'Temperatura', min_value=0.0, max_value=1.0, value=0.1, step=0.01)

    llm_model = st.selectbox("Escolha um modelo LLM",
                             ("gemini-1.5-pro", "gemini-pro"))

    st.sidebar.button('Limpar o histórico de bate-papo',
                      on_click=clear_chat_history)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input('Me faça uma pergunta!')

# instance the chain method with the selected temperature
chain = create_rag_chain(llm_model=llm_model, temperature=temperature)

if prompt:
    # display the prompt
    st.chat_message('user').markdown(prompt)
    # store the user prompt in state
    st.session_state.messages.append({'role': 'user', 'content': prompt})

    with st.spinner('Gerando resposta...'):
        response = chain.invoke(prompt)

    # display the response
    st.chat_message('ai').markdown(response)

    # store the LLM response in state
    st.session_state.messages.append({'role': 'ai', 'content': response})
