import logging
import sys
import argparse
import urllib
import flask
import re



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

app.run(host='0.0.0.0', port=PORT)
