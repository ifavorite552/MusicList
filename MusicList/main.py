from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import pathlib
import mimetypes

class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        pr_url = urllib.parse.urlparse(self.path)

        if pr_url.path == '/':
            self.send_html_file('index.html')
        elif pr_url.path == '/search':
            self.send_html_file('search.html')
        elif pathlib.Path().joinpath(pr_url.path[1:]).exists():
            self.send_static()
        else:
            self.send_html_file('error.html', 404)

    def send_html_file(self, filename, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        try:
            with open(filename, 'rb') as file:
                self.wfile.write(file.read())
        except FileNotFoundError:
            self.send_html_file('error.html', 404)

    def send_static(self):
        self.send_response(200)
        mt = mimetypes.guess_type(self.path)
        if mt[0]:
            self.send_header("Content-type", mt[0])
        else:
            self.send_header("Content-type", 'application/octet-stream')
        self.end_headers()

        try:
            with open(f'.{self.path}', 'rb') as file:
                self.wfile.write(file.read())
        except FileNotFoundError:
            self.send_html_file('error.html', 404)


def run(server_class=HTTPServer, handler_class=HttpHandler):
    server_address = ('', 8000)
    http = server_class(server_address, handler_class)
    try:
        print("Сервер запущено на <http://localhost:8000>")
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()

if __name__ == '__main__':
    run()
