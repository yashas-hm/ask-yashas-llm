import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

from api.endpoints.answer import answer_endpoint
from api.model.query_model import QueryModel
from api.utils.llm_pipeline import LLMChain
from api.utils.middleware import CORSMiddleware

app=FastAPI()
api_token = os.environ.get("API_TOKEN")
if api_token is None:
    api_token='AIzaSyDj8REBgZE21uFjvqBU8pgPoJNE3I7Ner0'
llm=LLMChain(api_token)

app.add_middleware(CORSMiddleware)

@app.get('/')
def redirect_to_site():
    return RedirectResponse("https://yashashm.dev", status_code=301)

@app.post('/prompt')
async def answer(query: QueryModel):
    try:
        return await answer_endpoint(query, llm)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    