from typing import Callable
from fastapi import FastAPI
from decouple import config

from core.APILayer import APILayer


def _startup_model(app: FastAPI) -> None:
    app.state.APILayer = APILayer(
        mongodb_uri=config("MONGODB_URI"),
    )


def start_app_handler(app: FastAPI) -> Callable:
    def startup() -> None:
        _startup_model(app)

    return startup


def _shutdown_model(app: FastAPI) -> None:
    app.state.APILayer = None


def stop_app_handler(app: FastAPI) -> Callable:
    def shutdown() -> None:
        _shutdown_model(app)

    return shutdown
