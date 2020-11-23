FROM ubuntu:latest
RUN apt-get update -y && apt-get install -y python3-pip python-dev git
RUN git clone https://github.com/michelescarlato/HelloEndoWorld.git
WORKDIR "/HelloEndoWorld"
RUN make
ENV myCustomEnvVar="This is a sample." \
    otherEnvVar="this is also a sample"

#RUN mkdir /HelloEndoWorld
#COPY . /HelloEndoWorld
#WORKDIR "/HelloEndoWorld"
#RUN make
#RUN python3 /HelloEndoWorld/server.py
