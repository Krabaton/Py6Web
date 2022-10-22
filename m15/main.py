from fastapi import FastAPI, Request

from src.middlewares.process_time import ProcessTimeMiddleware
from src.router import notes, users, auth

app = FastAPI()

app.add_middleware(ProcessTimeMiddleware)
app.include_router(auth.router)
app.include_router(notes.router)
app.include_router(users.router)


@app.get("/")
def read_root():
    return {"message": "TODO App v1.01"}

