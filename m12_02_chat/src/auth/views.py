import aiohttp.web
from aiohttp import web
from aiohttp_jinja2 import template
from aiohttp_session import get_session

from src.store.models import User, Messages


class Main(web.View):
    @template('pages/index.html')
    async def get(self):
        session = await get_session(self.request)
        auth = True if 'user' in session else False
        return {"title": 'Chat', "auth": auth}


class Login(web.View):
    @template('pages/login.html')
    async def get(self):
        session = await get_session(self.request)
        auth = True if 'user' in session else False
        return {"title": 'Chat', "auth": auth}

    async def post(self):
        data_form = await self.request.post()
        user = await self.request.app["db"].user.query.where(User.email == data_form["email"]).gino.one()
        if user and user.password == data_form["password"]:
            session = await get_session(self.request)
            session["user"] = user.login
            session["user_id"] = user.id
            location = self.request.app.router['main'].url_for()
            return web.HTTPFound(location=location)
        else:
            raise web.HTTPFound(location=self.request.app.router['login'].url_for())


class SignIn(web.View):
    @template('pages/signin.html')
    async def get(self):
        session = await get_session(self.request)
        auth = True if 'user' in session else False
        return {"title": 'Chat', "auth": auth}

    async def post(self):
        data_form = await self.request.post()
        await self.request.app["db"].user.create(email=data_form["email"], password=data_form["password"],
                                                 login=data_form["login"])
        location = self.request.app.router['login'].url_for()
        return web.HTTPFound(location=location)


class SignOut(web.View):
    async def get(self):
        session = await get_session(self.request)
        if session.get("user"):
            del session["user"]
            location = self.request.app.router['login'].url_for()
            return web.HTTPFound(location=location)
        raise web.HTTPForbidden(text='403: Forbidden')
