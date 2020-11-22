import logging
import sys
import argparse
import urllib
import flask
import re
from subprocess import check_output
import subprocess
from json import dumps
from flask import current_app, Blueprint, jsonify
import os
"""App configuration."""
from os import environ, path
from dotenv import load_dotenv

# Find .env file
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))
# Load parametrs from .env file
PATH = environ.get('PYTHONHOME')
PORT = environ.get('PORT')
LOGFILE = environ.get('LOGFILE')
HOST = environ.get('HOST')
GITREPO = environ.get('GITREPO')

# This fixed a visualization error in the browser
def jsonify(*args, **kwargs):
    indent = None
    separators = (',', ':')
    if current_app.config['JSONIFY_PRETTYPRINT_REGULAR'] and not request.is_xhr:
        indent = 2
        separators = (', ', ': ')
    if args and kwargs:
        raise TypeError('jsonify() behavior undefined when passed both args and kwargs')
    elif len(args) == 1:  # single args are passed directly to dumps()
        data = args[0]
    else:
        data = args or kwargs
    return current_app.response_class(
        (dumps(data, indent=indent, separators=separators), '\n'),
        mimetype=current_app.config['JSONIFY_MIMETYPE']
    )

#Check the port number range
class PortAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if not 0 < values < 2**16:
            raise argparse.ArgumentError(self, "port numbers must be between 0 and 65535")
        setattr(namespace, self.dest, values)
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port",
                        help='Port number to connect to',
                        dest='port',
                        default=8079,
                        type=int,
                        action=PortAction,
                        metavar="{0..65535}")
parser.add_argument("-P", "--PATH",
                        help='PATH environment override',
                        dest='PATH',
                        default='/usr/bin',
                        type=str)
args = parser.parse_args()
#self.name = args.name

if args.port:
    #print("port set"+str(args.port))
    PORT = args.port
#else
    #PORT = '8080'
if args.PATH:
    #print("port set"+str(args.port))
    PATH = args.PATH
#else
    #PATH =
# Camel-case gets cut by spaces
def separated_str(inputname):
    inputnameStrip = re.sub("([A-Z])", " \\1", inputname).strip()
    return inputnameStrip

# Git hash of the head of the repository
def GitHash(gitrepoName):
    hash = check_output(["git", "ls-remote","-h", gitrepoName])
    hash = str(hash)
    hashOutput = hash.split()
    hashHead = hashOutput[0]
    hashHead = hashHead[3:42]
    return hashHead

app = flask.Flask(__name__)
app.config["DEBUG"] = False
logging.basicConfig(filename=LOGFILE, level=logging.INFO)


@app.route('/helloworld', methods=['GET'])
def home():
    #return flask.render_template('hello_stranger.html')
    return "Hello Stranger"

@app.route('/helloworld/<name>')
def hello(name=None):
    nome=separated_str(name)
    #return flask.render_template('hello.html', name=nome)
    return "Hello "+nome

@app.route('/versionz')
def version():
    GitHeadHash= GitHash(GITREPO)
    return jsonify(GitProject ="HelloEndoWorld",
                    GitHeadHash= GitHeadHash)

portString = str(PORT)
f = open("tests/PORT.txt", "w")
f.write(portString)
f.close()

os.environ['PATH'] = PATH
print("This path will be used:\n"+os.environ.get('PATH'))
app.run(host=HOST, port=PORT)
