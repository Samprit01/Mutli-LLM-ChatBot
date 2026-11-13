from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
import time

def openai_call(question: str):
    llm = ChatOpenAI(model='gpt-4o')
    start = time.time()
    response = llm.invoke(question)
    end = time.time()
    return response.content, (end - start)

def ollama_call(question: str):
    llm = ChatOllama(model='gemma4')
    start = time.time()
    response = llm.invoke(question)
    end = time.time()
    return response.content, (end - start)

def gemini_call(question: str):
    llm = ChatGoogleGenerativeAI(model='gemini-flash-lite-latest')
    start = time.time()
    response = llm.invoke(question)
    end = time.time()
    return response.text, (end - start)