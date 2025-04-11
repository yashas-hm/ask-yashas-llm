from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter()

@router.get('/')
def default():
    return RedirectResponse("https://yashashm.dev/chat", status_code=302)
