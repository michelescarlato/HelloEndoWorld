#!/usr/bin/env python
from flask import Flask, jsonify, request
from subprocess import check_output
import subprocess
from os import environ, path
from dotenv import load_dotenv
#import time
import sys
import time
import json, os, signal


# Load parametrs from shutdown.txt file
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, 'shutdown.txt'))

SHUTDOWN = environ.get('SHUTDOWN')
PID = environ.get('PID')

print("Running sigpkill on HTTP server")

for i in range(int(SHUTDOWN),0,-1):
    sys.stdout.write(str(i)+' ')
    sys.stdout.flush()
    time.sleep(1)
#graceful shutdown of flask
os.kill(int(PID), signal.SIGINT)
#check_output(["pkill", "python"])
