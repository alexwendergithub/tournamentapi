from fastapi import FastAPI
from routers import tournaments

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(tournaments.router)