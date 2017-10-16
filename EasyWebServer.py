#! /usr/bin/env python3.4

import http.server
from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
	server_address = ('',8001)
	httpd = server_class(server_address, handler_class)
	httpd.serve_forever()
if __name__ == '__main__':
	run()