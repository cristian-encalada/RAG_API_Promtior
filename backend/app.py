from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import os
from langsmith import Client
from langchain_core.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
langsmith_api_key = os.getenv("LANGSMITH_API_KEY")
LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2")

app = FastAPI()

@app.get("/")
async def root():
    return RedirectResponse("/docs")


# Initialize LangChain components
llm = ChatOpenAI(model="gpt-4o")
client = Client()

# Load, chunk and index the contents of Promtior's website.
loader = WebBaseLoader(
    web_paths=("https://www.promtior.ai/",),
    bs_kwargs=dict(),
)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)
vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())

# Request model
class QueryRequest(BaseModel):
    question: str

# FastAPI endpoint
@app.post("/ask")
async def ask_question(request: QueryRequest):
    try:
        retriever = vectorstore.as_retriever()
        prompt = client.pull_prompt("rlm/rag-prompt")

        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)

        rag_chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )

        result = rag_chain.invoke(request.question)
        return {"answer": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# clean up
# vectorstore.delete_collection()
