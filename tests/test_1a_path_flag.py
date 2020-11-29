import unittest
import requests
from subprocess import check_output
import subprocess
from os import environ, path
from dotenv import load_dotenv
import time
import os
import sys
import time

# Find .env file
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '../.env'))

# Load parametrs from .env file
PORT = environ.get('PORT')
HOST = environ.get('HOST')
#PATH = str("/etc/local")

def test_PATH():
    time.sleep(2)
    PATH = str("/etc/local")
    subprocess.Popen(["python3", "server.py","-p","7777","-P",""+PATH+"","-s"+"-1"])
    time.sleep(2)
    #requests.get('http://'+HOST+':'+PORT+'/PATH/')
    response = requests.get('http://'+HOST+':7777/PATH')
    res=str(response.text)
    assert str(PATH) == str(res)

def test_shutdown():
    requests.get('http://'+HOST+':7777/shutdown/')
    time.sleep(2)
