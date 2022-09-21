from aiohttp.web import Application
from src.views import index, detail, note, tag, create_tag, create_note, done_note, delete_note


def setup_routes(app: Application):
    app.router.add_get('/', index, name='index')
    app.router.add_get('/note/', note, name='note')
    app.router.add_get('/detail/{note_id}', detail, name='detail')
    app.router.add_get('/tag/', tag, name='tag')
    app.router.add_route('POST', '/tag', create_tag)
    app.router.add_route('POST', '/note', create_note)
    app.router.add_get('/done/{note_id}', done_note, name='done')
    app.router.add_get('/delete/{note_id}', delete_note, name='delete')
