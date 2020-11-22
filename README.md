# HelloEndoWorld
After cloning the the project, and entering into the directory HelloEndoWorld run:

cd HelloEndoWorld
make

It will install the requirements to run the server.

Then run the server with

python3 server.py

It will run the server on the 8080 port
It is possible to run it on different ports using the -p flag, e.g.:

python3 server.py -p 7933

It is also possible to use a different PATH using the -P flag, e.g.:

python3 server.py -P /usr/bin/

It is also available a help using -h flag.

Default configuration parameters are specified in the file .env.

E.g. the log file will be demo.log, but the parameter can be changed through the .env file.
In the .env file also are specified: default port, default path, host ip address, Git Repository (used to retrieve head hash).

To perform the tests against a running instance, move into tests/ directory and execute:

cd tests/
pytest

At the moment only http endpoints have unit tests, which can be found in tests/test_flaskr.py
Tests for the flags still need to be written.

To run a docker instance, build the container with:
docker build -t python-helloendoworld .
After building, run it with:
docker run -it -w /HelloEndoWorld python-helloendoworld python3 server.py

To check which IP address is using the container execute:
docker ps
Then:
docker inspect CONTAINER_ID | grep IPAddress

To test the HTTP endpoints:
curl IPAddress:8080/helloworld
curl IPAddress:8080/helloworld/PaoloDeLuca
curl IPAddress:8080/versionz
