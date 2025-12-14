import streamlit as st
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains import create_history_aware_retriever
from langchain_chroma import Chroma
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
from dotenv import load_dotenv
load_dotenv()
groq_api_key=os.getenv("GROQ_API_KEY")
os.environ['HF_TOKEN']=os.getenv("HF_TOKEN")


embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

st.title("Conversational RAG with pdf reference and chat history")
st.write("upload a pdf and chat with refrence to it")

api_key = st.text_input("Enter you api key:", type="password")

if api_key:
    llm = ChatGroq(groq_api_key=api_key,model_name="llama-3.1-8b-instant")

    session_id=st.text_input("Session ID ", value = "Default Session")
    
    if 'store' not in st.session_state:
        st.session_state.store = {}
    