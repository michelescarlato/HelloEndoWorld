#!/usr/bin/env python
from subprocess import check_output
import subprocess
from os import environ, path
from dotenv import load_dotenv
import time


f = open("shutdown_timer.txt", "r")
SHUTDOWN = f.read()
SHUTDOWN = int(SHUTDOWN)

#check_output(["sleep", SHUTDOWN])
time.sleep(SHUTDOWN)
print("Running pkill python")
check_output(["pkill", "python"])
