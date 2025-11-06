from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db import init_db
from app.models import Transaction

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    print("Database initialised!")

    yield

    print("App shutting down...")

app = FastAPI(lifespan=lifespan)

@app.get("/")
def root():
    return {"message": " MoneyMind AI backend is running!"}