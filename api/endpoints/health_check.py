from fastapi import APIRouter
from fastapi.responses import JSONResponse

from api.constants import BOT

router = APIRouter()


@router.get("/healthCheck", tags=["Healthcheck"])
def health_check():
    return JSONResponse(content={"status": "ok", "message": f"{BOT} is healthy!"}, status_code=200)
