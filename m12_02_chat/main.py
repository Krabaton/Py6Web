import sys
import asyncio
import aiohttp_jinja2
import jinja2
from aiohttp import web
from src.routes import setup_routes
from src.settings import config
from src.store.accessor import DBAccessor


app = web.Application()
app['config'] = config
aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader('src', 'templates'))

setup_routes(app)
app["db"] = DBAccessor()
app["db"].setup(app)
app["websockets"] = []


if __name__ == '__main__':
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    web.run_app(app, port=config["common"]["port"])
