from fastapi import FastAPI
from langserve import add_routes
from app.chain import chain as chatbot_chain


app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="Spin up a simple api server using Langchain's Runnable interfaces",
)


@app.get("/", status_code=200)
async def return_ok():
    return {"status": "ok"}

add_routes(
    app,
    chatbot_chain,
    path="/openai",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)