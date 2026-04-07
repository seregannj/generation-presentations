from fastapi import FastAPI
from app.api.generate import router

app = FastAPI(title="GenDoc MVP")

app.include_router(router)
