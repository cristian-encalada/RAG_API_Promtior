from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from langchain_community.retrievers import TavilySearchAPIRetriever

import os

os.environ['OPENAI_API_KEY'] = 'YOUR_API'
os.environ['TAVILY_API_KEY'] = 'YOUR_API'

retriever = TavilySearchAPIRetriever(k=3)

prompt = ChatPromptTemplate.from_template(
    """You are an expert research assistant (chatbot). Please answer the following question based on the provided context. Please cite your sources at the end of your response.

Context: {context}

Question: {question}"""
)
chain = (
    RunnablePassthrough.assign(context=(lambda x: x["question"]) | retriever)
    | prompt
    | ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    | StrOutputParser()
)