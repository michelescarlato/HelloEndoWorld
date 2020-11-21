#https://www.afternerd.com/blog/python-http-server/
import http.server
import socketserver
import logging
import sys

try:
    PORT = int(sys.argv[1])
except:
    PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
