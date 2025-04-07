from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

class CORSMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        if request.url.path == "/":
            return await call_next(request)
        
        allowed_origin = [
            "https://yashashm.dev",
            "https://chat.yashashm.dev", 
            "https://ask-yashas-llm.onrender.com-"
        ]
        origin = request.headers.get("Origin")
        if origin in allowed_origin:
            return JSONResponse({"detail": "Forbidden"}, status_code=403)

        return await call_next(request)