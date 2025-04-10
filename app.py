import os
from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from api.endpoints.answer import answer_endpoint
from api.model.query_model import QueryModel
from api.utils.llm_pipeline import LLMChain
from api.utils.middleware import SecurityMiddleware

app=FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
api_token = os.environ.get("API_TOKEN")
if api_token is None:
    api_token='AIzaSyDj8REBgZE21uFjvqBU8pgPoJNE3I7Ner0'
llm=LLMChain(api_token)

app.add_middleware(SecurityMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

@app.get('/')
def main():
    return RedirectResponse("https://yashashm.dev", status_code=200)

@app.post('/api/prompt')
async def answer(query: QueryModel):
    try:
        return await answer_endpoint(query, llm)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    