import aiohttp
from aiohttp import web

clients = []


async def websocket_handler(request):

    ws = web.WebSocketResponse()
    await ws.prepare(request)
    clients.append(ws)

    async for msg in ws:
        print(msg)
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                for _ws in clients:
                    await _ws.send_str(msg.data)
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print('ws connection closed with exception %s' %
                  ws.exception())
    clients.remove(ws)
    print('websocket connection closed')

    return ws

app = web.Application()
app.add_routes([web.get('/ws', websocket_handler)])

if __name__ == '__main__':
    web.run_app(app)
