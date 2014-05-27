FROM 10.10.103.215:5000/basego 
MAINTAINER Chen XingYu wizard_cxy@hotmail.com

ADD conf.yml /home/go/
# Install gorouter dependencies

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get install -y bzr
RUN go get -v github.com/tools/godep
RUN go get -v github.com/cloudfoundry/gorouter

RUN cd $GOPATH/src/github.com/cloudfoundry/gorouter && godep restore ./...

EXPOSE 8081
CMD gorouter -c /home/go/conf.yml
