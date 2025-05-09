import os

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse


def bypass_middleware(key: str) -> bool:
    bypass_key = os.environ.get('BYPASS_KEY')
    if bypass_key is None or key != bypass_key:
        return False
    else:
        return True


class SecurityMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        if bypass_middleware(key=request.query_params.get("bypass_key")):
            return await call_next(request)

        if request.url.path == '/' or request.url.path == '/api/healthCheck':
            return await call_next(request)

        allowed_origin = [
            "https://yashashm.dev",
            "https://ask.yashashm.dev",
        ]

        origin = request.headers.get("Origin")
        if origin not in allowed_origin:
            return JSONResponse({"detail": "Forbidden"}, status_code=403)

        return await call_next(request)
