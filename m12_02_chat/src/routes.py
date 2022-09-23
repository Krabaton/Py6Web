from aiohttp.web import Application
from src.auth.views import Main, Login, SignIn, SignOut

routes = [
    ('GET', '/', Main, 'main'),
    ('*', '/login', Login, 'login'),
    ('*', '/signin', SignIn, 'signin'),
    ('*', '/signout', SignOut, 'signout')
]


def setup_routes(app: Application):
    for route in routes:
        app.router.add_route(route[0], route[1], route[2], name=route[3])
