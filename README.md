# HelloEndoWorld
After cloning the the project, and entering into the directory HelloEndoWorld run:

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

It is also possible to use a different PATH using the -P flag, e.g.:
```bash
python3 server.py -P /usr/bin/
```
It is also available a help using -h flag.

Default configuration parameters are specified in the file .env.

E.g. the log file will be demo.log, but the parameter can be changed through the .env file.
In the .env file also are specified: default port, default path, host ip address, Git Repository (used to retrieve head hash).

To perform the tests against a running instance execute:

```bash
python3 -m pytest
```

At the moment only http endpoints have unit tests, which can be found in tests/test_flaskr.py
Tests for the flags still need to be written.

To run a docker instance, build the container with:
```bash
docker build -t python-helloendoworld .
```

After building, run it with:
```bash
docker run -it -w /HelloEndoWorld helloendoworld python3 server.py
```

To check which IP address is using the container execute:
```bash
docker ps
```
Then use the container id in the following command:
```bash
docker inspect $CONTAINER_ID | grep IPAddress
```

Usually this ip address is 172.17.0.2.

To test the HTTP endpoints:
```bash
curl 172.17.0.2:8080/helloworld
curl 172.17.0.2:8080/helloworld/PaoloDeLuca
curl 172.17.0.2:8080/versionz
```

Jenkinsfile contains the pipeline used to run the HTTP server and tests.

