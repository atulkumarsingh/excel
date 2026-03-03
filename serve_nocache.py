import http.server


class NoCacheHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()


class ThreadingNoCacheHTTPServer(http.server.ThreadingHTTPServer):
    # Allow quick restart without waiting for socket release.
    allow_reuse_address = True


if __name__ == "__main__":
    PORT = 8000
    with ThreadingNoCacheHTTPServer(("", PORT), NoCacheHTTPRequestHandler) as httpd:
        print(f"Serving on port {PORT} with no-cache headers...")
        httpd.serve_forever()
