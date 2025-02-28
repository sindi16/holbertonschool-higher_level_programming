import http.server
import json


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """Custom HTTP request handler to serve simple API endpoints."""

    def do_GET(self):
        """Handles GET requests and serves JSON or plain text responses."""
        routes = {
            "/data": self.handle_data,
            "/status": self.handle_status,
            "/": self.handle_root,
        }

        handler = routes.get(self.path, self.handle_not_found)
        handler()

    def handle_data(self):
        """Handles the /data endpoint, returning a JSON response."""
        data = {"name": "John", "age": 30, "city": "New York"}
        json_data = json.dumps(data)
        self._send_response(200, json_data, "application/json")

    def handle_status(self):
        """Handles the /status endpoint, returning API status."""
        self._send_response(200, "OK", "text/plain")

    def handle_root(self):
        """Handles the root endpoint, returning a welcome message."""
        self._send_response(200, "Hello, this is a simple API!", "text/plain")

    def handle_not_found(self):
        """Handles undefined endpoints with a 404 error."""
        self._send_response(404, "404 Not Found", "text/plain")

    def _send_response(self, status_code, content, content_type):
        """Utility function to send HTTP responses with headers."""
        self.send_response(status_code)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        self.wfile.write(content.encode())

  
def run(
    server_class=http.server.HTTPServer,
    handler_class=SimpleHTTPRequestHandler,
    port=8000,
):
    """Starts the HTTP server."""
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting HTTP server on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()

