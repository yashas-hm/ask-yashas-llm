from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/healthCheck", tags=["Healthcheck"])
def health_check():
    return JSONResponse(content={"status": "ok", "message": "AskYashas is healthy!"}, status_code=200)
