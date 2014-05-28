FROM 10.10.103.215:5000/basego 
MAINTAINER Chen XingYu wizard_cxy@hotmail.com


RUN apt-get update && apt-get install -y openssh-server supervisor && mkdir -p /var/run/sshd && mkdir -p /var/log/supervisor
RUN echo 'root:haha' | chpasswd

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN mkdir -p /home/gorouter/

ADD conf.template /home/gorouter/
# Install gorouter dependencies

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get install -y bzr
RUN go get -v github.com/tools/godep
RUN go get -v github.com/cloudfoundry/gorouter

RUN cd $GOPATH/src/github.com/cloudfoundry/gorouter && godep restore ./...
ADD run.py /home/

EXPOSE 8081
CMD ["python", "/home/run.py"]
