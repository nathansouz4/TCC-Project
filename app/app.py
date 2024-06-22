# from app.src.core import get_documents_from_web, create_db, create_chain, process_chat

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os
from langchain_google_genai import GoogleGenerativeAI
# streamlit for the UI dev
import streamlit as st

import textwrap


def to_markdown(text):
    # text=text._result.candidates[0].content.parts[0].text
    text = text.replace('•', '  *')
    return textwrap.indent(text, '> ', predicate=lambda _: True)


# import sdk google gemini

load_dotenv('app/src/shared/.env')

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# chose a model
llm = GoogleGenerativeAI(model="gemini-pro")


def clear_chat_history():
    st.session_state.messages = []


st.title('Ask to Spark ⚡')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input('Me faça uma pergunta!')

with st.sidebar:

    temperature = st.sidebar.slider(
        'temperature', min_value=0.01, max_value=1.0, value=0.1, step=0.01)

    st.sidebar.button('Clear Chat History', on_click=clear_chat_history)


if prompt:
    # display the prompt
    st.chat_message('user').markdown(prompt)
    # store the user prompt in state
    st.session_state.messages.append({'role': 'user', 'content': prompt})

    response = llm.invoke(prompt)
    formatted_text = to_markdown(response)
    st.chat_message('ai').markdown(formatted_text)

    print(response)

    # store the LLM response in state
    st.session_state.messages.append({'role': 'ai', 'content': formatted_text})
