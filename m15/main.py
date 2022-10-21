import time

from fastapi import FastAPI, Request

from src.router import notes

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

app.include_router(notes.router)


@app.get("/")
def read_root():
    return {"message": "TODO App v1.01"}

