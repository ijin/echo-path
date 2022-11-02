#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def print_info(self):
        self.log_message("%s %s\n%s", self.command, self.path, self.headers)

    def do_GET(self):
        self.print_info()
        self.wfile.write(("path: " + self.path + "\n").encode('utf-8'))

httpd = HTTPServer(("", 8000), RequestHandler)
httpd.serve_forever()
