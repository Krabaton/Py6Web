from http.server import HTTPServer, BaseHTTPRequestHandler
import mimetypes
from jinja2 import Environment, FileSystemLoader
import json
import urllib.parse
import pathlib

env = Environment(loader=FileSystemLoader('templates'))


class HttpGetHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # print(self.headers)
        data = self.rfile.read(int(self.headers['Content-Length']))
        self.save_data_to_json(data)
        self.send_response(302)
        self.send_header('Location', '/contact')
        self.end_headers()

    def do_GET(self):
        print(urllib.parse.urlparse(self.path))
        pr_url = urllib.parse.urlparse(self.path)
        match pr_url.path:
            case '/':
                self.send_html_file('index.html')
            case '/blog':
                print(urllib.parse.parse_qs(pr_url.query))
                self.render_template('blog.html')
            case '/contact':
                self.send_html_file('contact.html')

            case _:
                print(pathlib.Path().joinpath(pr_url.path[1:]).exists())
                if pathlib.Path().joinpath(pr_url.path[1:]).exists():
                    self.send_static()
                else:
                    self.send_response(404)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    with open('404.html', 'rb') as fd:
                        self.wfile.write(fd.read())

    def send_html_file(self, filename):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(filename, 'rb') as fd:
            self.wfile.write(fd.read())

    def render_template(self, filename):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        pic = '/assets/img/Layer.png'
        with open('./data/blog.json', 'r', encoding='utf-8') as fd:
            r = json.load(fd)
        template = env.get_template(filename)
        html = template.render(blogs=r, pic=pic)
        self.wfile.write(html.encode())

    def save_data_to_json(self, data):
        data_parse = urllib.parse.unquote_plus(data.decode())
        data_parse = {key: value for key, value in [el.split('=') for el in data_parse.split('&')]}
        with open('./data/data.json', 'w', encoding='utf-8') as fd:
            json.dump(data_parse, fd, ensure_ascii=False)

    def send_static(self):
        self.send_response(200)
        mt = mimetypes.guess_type(self.path)
        if mt:
            self.send_header('Content-type', mt[0])
        else:
            self.send_header('Content-type', 'text/plain')
        self.end_headers()
        with open(f'.{self.path}', 'rb') as fd:  # ./assets/js/app.js
            self.wfile.write(fd.read())


def run(server_class=HTTPServer, handler_class=HttpGetHandler):
    server_address = ('', 8000)
    http = server_class(server_address, handler_class)
    try:
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()


if __name__ == '__main__':
    run()
