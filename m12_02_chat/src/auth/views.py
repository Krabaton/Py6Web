from aiohttp import web
from aiohttp_jinja2 import template


class Main(web.View):
    @template('pages/index.html')
    async def get(self):
        return {"title": 'Chat', "auth": False}


class Login(web.View):
    @template('pages/login.html')
    async def get(self):
        return {"title": 'Chat', "auth": False}

    async def post(self):
        pass


class SignIn(web.View):
    @template('pages/signin.html')
    async def get(self):
        return {"title": 'Chat', "auth": False}

    async def post(self):
        pass


class SignOut(web.View):
    async def get(self):
        pass
