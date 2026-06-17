from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        # On indique à Firefox qu'on lui envoie du HTML
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
       
        # Du HTML avec du CSS pour centrer et grossir le texte
        html = "<h1 style='text-align: center; font-size: 70px; margin-top: 15%; font-family: sans-serif;'>Hello World</h1>"
        self.wfile.write(html.encode())

HTTPServer(("127.0.0.1", 8000), Handler).serve_forever()

