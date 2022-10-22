from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from decouple import config

from routers import open_interest

from events.event_handlers import start_app_handler, stop_app_handler

app = FastAPI(
    title="Radar: api-python-dashboard", 
    description=open("README.md", mode="r").read()
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(open_interest.router)

app.add_event_handler("startup", start_app_handler(app))
app.add_event_handler("shutdown", stop_app_handler(app))

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=5000,
        log_level="debug",
        workers=config("WORKERS", cast=int, default=1),
    )
