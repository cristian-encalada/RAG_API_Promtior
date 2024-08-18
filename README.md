# RAG Chatbot using Langchain and OpenAI API

Web RAG chatbot using Langchain, Langsmith, beautifulsoup4, deployed with Azure

The chatbot is going to answer questions about my personal site:
* https://cristianencalada.dev/

## Live demo

### Backend

API Endpoints URL: [Live API URL](https://rag-web-langchain-backend-bzdbhxcucfaue8hw.eastus-01.azurewebsites.net/)

![API endpoints](./doc/api_endpoints.png)


### Frontend

In progress

## Requirements

1. Have a valid OpenAI Key. Check [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Have a valid Tavily key. Check [LangSmith](https://www.langchain.com/langsmith)
3. Python version __3.11__ or previous. With new versions of Python, such as 3.12, the Railway deployment is going to have errors. Verify it with:

```sh
python --version
```

4. __Recomemnded__, have virtual environments (venv) for Python [Python vev documentation](https://docs.python.org/3/library/venv.html)

5. Create a .env file with the following variables:

```sh
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGSMITH_API_KEY="lsv2_pt_xxxxxx"
OPENAI_API_KEY="sk-proj-xxxxxxxx"
```

## Run backend locally (without Docker)

1. Create a virtual environment in the /backend directory

```sh
python -m venv venv
```

```sh
.\venv\Scripts\activate
```

2. Install python dependency packages:

```
pip install -r requirements.txt
```

3. Launch FastAPI

```sh
uvicorn app:app
```

Output
```sh
INFO:     Started server process [6944]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

## Run backend with Dockerfile

1. Build the docker image

```
docker build -t rag-web-langchain-back .
```

2. Run the docker image

```
docker run -p 8000:8000 rag-web-langchain-back
```

The Fast API endpoints should be running at:

```sh
http://127.0.0.1:8000/docs
```

## Author

Cristian Encalada - [Linkedin](https://www.linkedin.com/in/cristian-encalada/)

## Acknowledgements

* https://python.langchain.com/v0.2/docs/tutorials/rag/
* https://vercel.com/templates/next.js/nextjs-ai-chatbot