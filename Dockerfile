FROM ubuntu:latest
RUN apt-get update -y && apt-get install -y python3-pip python-dev git
RUN git clone https://github.com/michelescarlato/HelloEndoWorld.git
WORKDIR "/HelloEndoWorld"
RUN make
