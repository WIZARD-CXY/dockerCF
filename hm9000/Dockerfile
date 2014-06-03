FROM 10.10.103.215:5000/hm9000final 
MAINTAINER Chen XingYu wizard_cxy@hotmail.com


RUN apt-get update && apt-get install -y openssh-server supervisor && mkdir -p /var/run/sshd && mkdir -p /var/log/supervisor
RUN echo 'root:haha' | chpasswd

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
#ADD config file into the image
RUN mkdir -p /home/hm9000/
ADD hm9000.template /home/hm9000/
ADD run.py /home/

ENV LOG_DIR /var/vcap/sys/log/hm9000
RUN mkdir -p $LOG_DIR

CMD ["python", "/home/run.py"]