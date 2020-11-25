# HelloEndoWorld

For this project, I used Xubuntu 20.04, and I needed to install the following packages:

```bash
sudo apt-get install python3-pip make
```

After cloning the project, and entering into the directory HelloEndoWorld run:

```bash
cd HelloEndoWorld
make

```


It will install the requirements to run the server.

Then run the server with:
```bash
python3 server.py
```

It will run the server on the 8080 port.
It is possible to run it on different ports using the -p flag, e.g.:

```bash
python3 server.py -p 7933
```

It is possible to use a different PATH using the -P flag, e.g.:
```bash
python3 server.py -P /usr/bin/
```

It is also possible to set a timer for a graceful shutdown of the flask server using the -s flag, e.g.:
```bash
python3 server.py -s 30
```
will shutdown the server after 30 seconds of activity.

It is also available a help using -h flag.

Default configuration parameters are specified in the file .env.

E.g. the log file will be demo.log, but the parameter can be changed through the .env file.
In the .env file also are specified: default port, default path, host ip address, Git Repository (used to retrieve head hash).

To perform the tests against a running instance execute:

```bash
python3 -m pytest
```

At the moment only http endpoints have unit tests, which can be found in tests/test_flaskr.py
The Jenkins pipeline also performs the execution of unit tests on a different port.
Tests for the flags still need to be written.

To run a docker instance, build the container with:
```bash
docker build -t python-helloendoworld .
```
The container can be run on localhost, using docker run -it (to pass a shell command as a parameter), -d (detach), and -p (publish port(s)) to :

```bash
docker run -it -d -p 8080:8080 sanmiguelsan/helloendoworld python3 server.py
```
In alternative it can be run on a different (local) IP address:
```bash
docker run -it helloendoworld python3 server.py -p 8079
```
To check which IP address is using the container execute:
```bash
docker ps
```
Then use the container id in the following command:
```bash
docker inspect $CONTAINER_ID | grep IPAddress
```
Usually, this IP address is 172.17.0.2.

To test the HTTP endpoints:
```bash
curl 172.17.0.2:8080/helloworld
curl 172.17.0.2:8080/helloworld/PaoloDeLuca
curl 172.17.0.2:8080/versionz
```
Jenkinsfile contains the pipeline used to run the HTTP server and tests.
