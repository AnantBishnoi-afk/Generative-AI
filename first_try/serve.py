from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from langserve import add_routes

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
chat_groq = ChatGroq(model_name="llama-3.1-8b-instant",api_key=groq_api_key)

system_template = "Translate the text in this language {language}"
chat_prompt = ChatPromptTemplate.from_messages([
    ("system",system_template),
    ("user","{text}")
])

parser = StrOutputParser()
chain = chat_prompt|chat_groq|parser

app = FastAPI(
    title = "Langchain server",
    version = "1.0",
    description = "This is a test app for fastapi implementation"
)
add_routes(
    app,
    chain,
    path="/chain"
)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)