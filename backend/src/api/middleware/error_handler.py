from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


def register(app: FastAPI) -> None:
    @app.exception_handler(Exception)
    async def handle_exception(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content={"detail": str(exc) or "Internal server error"},
        )
