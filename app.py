from api.endpoints import default, health_check
from api.endpoints.answer import get_prompt_route
from api.utils.llm_pipeline import LLMChain
from api.utils.middleware import SecurityMiddleware
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

llm = LLMChain.create_llm_pipeline()
app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
router = APIRouter()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=False,
)
app.add_middleware(SecurityMiddleware)

app.include_router(default.router)
app.include_router(health_check.router, prefix='/api')
app.include_router(get_prompt_route(llm), prefix='/api')
