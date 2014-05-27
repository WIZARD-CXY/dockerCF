FROM 10.10.103.215:5000/myubuntu12.04
MAINTAINER Chen XingYu wizard_cxy@hotmail.com

# Install go

## Update system
RUN apt-get update
RUN apt-get install -y wget ca-certificates build-essential

### For some reason `go get` required these to run, despite it not being documented?
RUN apt-get install -y git mercurial
RUN mkdir /home/go

ENV PATH $PATH:/usr/local/go/bin:/home/go/bin
ENV GOPATH /home/go

RUN wget --no-verbose https://go.googlecode.com/files/go1.2.src.tar.gz
RUN tar -v -C /usr/local -xzf go1.2.src.tar.gz
RUN cd /usr/local/go/src && ./make.bash --no-clean 2>&1
