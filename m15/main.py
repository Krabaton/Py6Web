from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from src.middlewares.process_time import ProcessTimeMiddleware
from src.router import notes, users, auth
from src.config import BASE_DIR

app = FastAPI()

black_list = ['127.0.0.1', '192.168.23.43']


@app.middleware('http')
async def check_ip(request: Request, call_next):
    ip_client = request.client.host
    print(ip_client)
    if ip_client in black_list:
        print('BLOCK IP!!!!!')
    response = await call_next(request)
    return response

app.add_middleware(ProcessTimeMiddleware)

templates = Jinja2Templates(directory="templates")
app.mount("/source", StaticFiles(directory=BASE_DIR / "templates/source"), name="source")

app.include_router(auth.router)
app.include_router(notes.router)
app.include_router(users.router)


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse('index.html', {"request": request, "title": "Todo APP"})


@app.get("/user-notes", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse('list-notes.html', {"request": request, "title": "Todo APP"})
