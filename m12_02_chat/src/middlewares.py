import aiohttp_jinja2
from aiohttp import web
from aiohttp_session import get_session


async def handle_404(request):
    return aiohttp_jinja2.render_template('404.html', request, {"message": f"Not found url {request.url}"}, status=404)


async def handle_500(request):
    return aiohttp_jinja2.render_template('500.html', request, {"message": "500: Internal Server Error"}, status=500)


@web.middleware
async def error_middleware(request, handler):
    try:
        return await handler(request)
    except web.HTTPException as ex:
        if ex.status == 404:
            return await handle_404(request)
        if ex.status == 500:
            return await handle_500(request)
        raise
    except Exception:
        request.protocol.logger.exception("Error handling request")
        return await handle_500(request)


@web.middleware
async def authorize(request, handler):
    def isprotect(path: str):
        for route in ['/chat', '/signout']:
            if path.startswith(route):
                return True
        return False

    if isprotect(request.path):
        session = await get_session(request)
        if session.get('user'):
            return await handler(request)
        else:
            raise web.HTTPForbidden(text="403: Forbidden")

    return await handler(request)
