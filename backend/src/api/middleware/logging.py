from fastapi import FastAPI, Request


def register(app: FastAPI) -> None:
    @app.middleware("http")
    async def log_requests(request: Request, call_next):
        response = await call_next(request)
        return response
