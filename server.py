#https://www.afternerd.com/blog/python-http-server/
import http.server
import socketserver
import logging
import sys
import argparse

class PortAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if not 0 < values < 2**16:
            raise argparse.ArgumentError(self, "port numbers must be between 0 and 65535")
        setattr(namespace, self.dest, values)


parser = argparse.ArgumentParser()


parser.add_argument("-p", "--port",
                        help='Port number to connect to',
                        dest='port',
                        default=8080,
                        type=int,
                        action=PortAction,
                        metavar="{0..65535}")

args = parser.parse_args()
if args.port:
    #print("port set"+str(args.port))
    PORT = args.port

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
