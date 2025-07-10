#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        
        elif self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json_data.encode())

        elif self.path == '/info':
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            json_info = json.dumps(info)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json_info.encode())
        
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

if __name__ == '__main__':
    port = 8000
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print(f"Serving on http://localhost:{port}")
    httpd.serve_forever()
