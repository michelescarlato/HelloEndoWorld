import unittest
import requests
from subprocess import check_output
import subprocess
from os import environ, path
from dotenv import load_dotenv
import time

# Find .env file
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '../.env'))
# Load parametrs from .env file
PORT = environ.get('PORT')
HOST = environ.get('HOST')
GITREPO = environ.get('GITREPO')
#f = open("tests/PORT.txt", "r")
#PORT = f.read()


#subprocess.Popen(["cd .."])

def test_port():
    PORT = str(6685)
    subprocess.Popen(["pwd"])
    #subprocess.Popen(["python3", "server.py","-p",""+PORT+"","&"])
    subprocess.Popen(["python3", "server.py","-p",""+PORT+""])
    print("server running")
    time.sleep(2)
    requests.get('http://'+HOST+':'+PORT+'/shutdown/')
    time.sleep(2)
    
