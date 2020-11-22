FROM python:latest
RUN mkdir /HelloEndoWorld
COPY . /HelloEndoWorld
WORKDIR "/HelloEndoWorld"
RUN make
#RUN python3 /HelloEndoWorld/server.py
