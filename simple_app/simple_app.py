import os
from dotenv import load_dotenv
load_dotenv()

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

st.title("LangChain Demo with Llama 2 or Google Gamma Model")
input_text = st.text_input("What question do you have in mind?")

prompt = ChatPromptTemplate.from_messages([
    ("system","You are a helpful assistant. Please help with the given question"),
    ("user","Question:{question}")
])

llm = OllamaLLM(model="gemma3:1b")

output_parser= StrOutputParser()

chain = prompt|llm|output_parser

if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)
