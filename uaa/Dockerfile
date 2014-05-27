FROM 10.10.103.215:5000/uaaf1
MAINTAINER Chen XingYu wizard_cxy@hotmail.com


RUN apt-get update && apt-get install -y openssh-server supervisor && mkdir -p /var/run/sshd && mkdir -p /var/log/supervisor
RUN echo 'root:haha' | chpasswd

RUN mkdir /home/config/
ADD cf-registrar-config.yml /home/config/
ADD log4j.properties /home/config/
ADD uaa.yml /home/config/
ADD varz.yml /home/config/
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ENV LOG_DIR /var/vcap/sys/log/uaa/
RUN mkdir -p $LOG_DIR
ENV CLOUD_FOUNDRY_CONFIG_PATH /home/config
ENV CONFIG_FILE /home/config/cf-registrar-config.yml

EXPOSE 22 8080
CMD ["/usr/bin/supervisord"]

