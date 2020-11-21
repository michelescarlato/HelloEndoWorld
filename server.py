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


def separated_str(inputname):
    inputnameStrip = re.sub("([A-Z])", " \\1", inputname).strip()
    return inputnameStrip


app = flask.Flask(__name__)
app.config["DEBUG"] = True

gitrepo = "https://github.com/michelescarlato/HelloEndoWorld.git"

def GitHash(gitrepoName):
    hash = check_output(["git", "ls-remote","-h", gitrepoName])
    hash = str(hash)
    hashOutput = hash.split()
    hashHead = hashOutput[0]
    return hashHead[3:42]

#print(GitHash(gitrepo))

@app.route('/helloworld', methods=['GET'])
def home():
    return flask.render_template('hello_stranger.html')

@app.route('/helloworld/<name>')
#def hello(nome):
    #print(separated_str(name))
    #https://www.tutorialspoint.com/Regex-in-Python-to-put-spaces-between-words-starting-with-capital-letters
    #return "Hello "+nome
def hello(name=None):
    nome=separated_str(name)
    return flask.render_template('hello.html', name=nome)

@app.route('/versionz')
def version():
    GitHeadHash= GitHash(gitrepo)
    return jsonify(GitProject ="HelloEndoWorld",
                    GitHeadHash= GitHeadHash)

app.run(host='0.0.0.0', port=PORT)
