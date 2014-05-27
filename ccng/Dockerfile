FROM 10.10.103.215:5000/ccngf
MAINTAINER Chen XingYu wizard_cxy@hotmail.com

RUN apt-get update && apt-get install -y supervisor openssh-server zip && mkdir -p /var/run/sshd && mkdir -p /var/log/supervisor
RUN echo 'root:haha' | chpasswd

EXPOSE 22 8181

ADD cloud_controller.yml /cloud_controller_ng/config/
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ENV CLOUD_CONTROLLER_NG_CONFIG /cloud_controller_ng/config/cloud_controller.yml
RUN mkdir -p /var/vcap/shared && mkdir -p /var/vcap/nfs/shared
CMD ["/usr/bin/supervisord"]