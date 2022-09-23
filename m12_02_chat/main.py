import sys
import base64
import asyncio
import aiohttp_jinja2
import jinja2
from aiohttp import web
from cryptography import fernet
from aiohttp_session import setup
from aiohttp_session.cookie_storage import EncryptedCookieStorage

from src.routes import setup_routes
from src.settings import config
from src.store.accessor import DBAccessor
from src.middlewares import error_middleware, authorize


app = web.Application()

f_key = fernet.Fernet.generate_key()
print(f_key)
secret_key = base64.urlsafe_b64decode(f_key)
print(secret_key)
setup(app, EncryptedCookieStorage(secret_key))
app.middlewares.append(error_middleware)
app.middlewares.append(authorize)
app['config'] = config
aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader('src', 'templates'))
app.router.add_static('/static', path='src/static', name='static')
setup_routes(app)
app["db"] = DBAccessor()
app["db"].setup(app)
app["websockets"] = []


if __name__ == '__main__':
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    web.run_app(app, port=config["common"]["port"])
