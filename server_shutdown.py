#!/usr/bin/env python
from subprocess import check_output
import subprocess
from os import environ, path
from dotenv import load_dotenv
#import time
import sys
import time

f = open("shutdown_timer.txt", "r")
SHUTDOWN = f.read()
SHUTDOWN = int(SHUTDOWN)
print("Running pkill python")

#Graphical countdown visualization
for i in range(SHUTDOWN,0,-1):
    sys.stdout.write(str(i)+' ')
    sys.stdout.flush()
    time.sleep(1)

check_output(["pkill", "python"])
