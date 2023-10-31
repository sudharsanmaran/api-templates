from fastapi import FastAPI

from src.routers import router

app = FastAPI(
    title="Eagle Bot API Automations",
    version="1.0.0",
)

app.include_router(router)


@app.get("/")
async def root():
    return {"message": "application started successfully"}
