from api.model.query_model import QueryModel
from api.utils.llm_pipeline import LLMChain


async def answer_endpoint(query: QueryModel, llm: LLMChain):
    result = llm.invoke_chain(query=query.query, history=query.history)
    return {'response': result}
