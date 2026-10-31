from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        body = f"hello from a kube-dc preview ({os.environ.get('HOSTNAME', '?')})\n".encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(body)

HTTPServer(("", 8080), H).serve_forever()
