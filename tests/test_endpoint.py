import unittest
import requests
from subprocess import check_output
import subprocess
from os import environ, path
from dotenv import load_dotenv

# Find .env file
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '../.env'))
# Load parametrs from .env file
#PORT = environ.get('PORT')
HOST = environ.get('HOST')
GITREPO = environ.get('GITREPO')
f = open("tests/PORT.txt", "r")
PORT = f.read()

# Endpoint tests
def GitHash(gitrepoName):
    hash = check_output(["git", "ls-remote","-h", gitrepoName])
    hash = str(hash)
    hashOutput = hash.split()
    hashHead = hashOutput[0]
    hashHead = hashHead[3:42]
    return hashHead

GitHeadHash= GitHash(GITREPO)

def test_request_response():
    response = requests.get('http://'+HOST+':'+PORT+'/helloworld')
    assert response.status_code == 200
    res=response.text
    assert res == "Hello Stranger"
    #assert response.assertEqual("Hello Stranger")

def test_request_responseHelloName():
    response = requests.get('http://'+HOST+':'+PORT+'/helloworld/PaoloDeLuca')
    assert response.status_code == 200
    #assert response.assertEqual("Hello Stranger")
    res=response.text
    assert res == "Hello Paolo De Luca"

def test_request_responseJSON():
    response = requests.get('http://'+HOST+':'+PORT+'/versionz')
    response_body = response.json()
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response_body["GitProject"] == "HelloEndoWorld"
    assert response_body["GitHeadHash"] == GitHeadHash

#def test_server_port():
    #python3 /home/mi1chelescarlato/HelloEndoWorld/server.py
