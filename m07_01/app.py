from http.server import HTTPServer, BaseHTTPRequestHandler
import mimetypes


class HttpGetHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # print(self.headers)
        data = self.rfile.read(int(self.headers['Content-Length']))
        print(data)
        self.send_response(302)
        self.send_header('Location', '/contact')
        self.end_headers()

    def do_GET(self):
        print(self.path)
        match self.path.split('/'):
            case '', '':
                self.send_html_file('index.html')
            case '', 'blog':
                self.send_html_file('blog.html')
            case '', 'contact':
                self.send_html_file('contact.html')
            case '', 'assets', *_:
                self.send_response(200)
                mt = mimetypes.guess_type(self.path)
                if mt:
                    self.send_header('Content-type', mt[0])
                else:
                    self.send_header('Content-type', 'text/plain')
                self.end_headers()
                with open(f'.{self.path}', 'rb') as fd:  # ./assets/js/app.js
                    self.wfile.write(fd.read())
            case _:
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


def run(server_class=HTTPServer, handler_class=HttpGetHandler):
    server_address = ('', 8000)
    http = server_class(server_address, handler_class)
    try:
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()


if __name__ == '__main__':
    run()
    