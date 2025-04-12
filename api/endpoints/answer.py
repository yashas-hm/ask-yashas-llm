from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from api.model.query_model import QueryModel
from api.utils.llm_pipeline import LLMChain


def get_prompt_route(llm: LLMChain):
    router = APIRouter()

    @router.post('/prompt')
    async def answer_endpoint(query: QueryModel):
        try:
            result = llm.invoke_chain(query=query.query, history=query.history)
            return JSONResponse(content={"response": result}, status_code=200)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    return router
