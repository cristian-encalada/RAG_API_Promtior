from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from app.chain import chain as chatbot_chain

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="Spin up a simple api server using Langchain's Runnable interfaces",
)

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

add_routes(
    app,
    chatbot_chain,
    path="/chatbot",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)