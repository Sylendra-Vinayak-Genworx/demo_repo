from fastapi import FastAPI

from .routes import health, sse, websocket
from ...middleware import cors as cors_middleware
from ...middleware import error_handler
from ...middleware import logging as logging_middleware
from ...middleware import metrics as metrics_middleware


def create_app() -> FastAPI:
    app = FastAPI(title="Demo Backend", version="0.1.0")

    cors_middleware.register(app)
    logging_middleware.register(app)
    error_handler.register(app)
    metrics_middleware.register(app)

    app.include_router(health.router, prefix="/health", tags=["health"])
    app.include_router(sse.router, prefix="/events", tags=["sse"])
    app.include_router(websocket.router, prefix="/ws", tags=["websocket"])

    return app


app = create_app()
