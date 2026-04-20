from fastapi import FastAPI

from .routes import auth, health, sse, websocket
from src.api.middleware import cors as cors_middleware
from src.api.middleware import error_handler
from src.api.middleware import logging as logging_middleware
from src.api.middleware import metrics as metrics_middleware


def create_app() -> FastAPI:
    app = FastAPI(title="Demo Backend", version="0.1.0")

    cors_middleware.register(app)
    logging_middleware.register(app)
    error_handler.register(app)
    metrics_middleware.register(app)

    app.include_router(health.router, prefix="/health", tags=["health"])
    app.include_router(sse.router, prefix="/events", tags=["sse"])
    app.include_router(websocket.router, prefix="/ws", tags=["websocket"])
    app.include_router(auth.router, prefix="/auth", tags=["auth"])

    return app


app = create_app()
