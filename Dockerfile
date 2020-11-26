FROM ubuntu:focal-20201106
RUN apt-get update -y && apt-get install -y python3-pip python-dev git
RUN git clone https://github.com/michelescarlato/HelloEndoWorld.git
WORKDIR "/HelloEndoWorld"
RUN make
EXPOSE 8080
CMD ["python3","server.py"]
#RUN python3 server.py
