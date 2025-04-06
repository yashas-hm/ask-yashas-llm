from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

class CORSMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        allowed_origin = "https://yashashm.dev"
        origin = request.headers.get("Origin")
        if origin != allowed_origin:
            return JSONResponse({"detail": "Forbidden"}, status_code=403)

        response = await call_next(request)
        return response
