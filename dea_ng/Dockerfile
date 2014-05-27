FROM 10.10.103.215:5000/dea_ng
MAINTAINER Chen XingYu wizard_cxy@hotmail.com


RUN apt-get update && apt-get install -y openssh-server supervisor iptables quota debootstrap && mkdir -p /var/run/sshd && mkdir -p /var/log/supervisor
RUN echo 'root:haha' | chpasswd

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD run.sh /

ENV PATH $PATH:/usr/local/go/bin:/home/go/bin
ENV GOPATH /home/go:/dea_ng/go
RUN ulimit -c unlimited

ENV PACKAGE_DIR /var/vcap/packages/
ENV DEA_NG_RUN_DIR /var/vcap/sys/run/dea_next
ENV WARDEN_RUN_DIR /var/vcap/sys/run/warden
ENV LOG_DIR /var/vcap/sys/log/dea_next
ENV DEA_NG_PIDFILE $DEA_NG_RUN_DIR/dea_next.pid
ENV WARDEN_CONF_DIR /var/vcap/jobs/dea_next/config

ENV JOB_DIR /var/vcap/jobs/dea_next

ENV DEA_NG_DATA_DIR /var/vcap/data/dea_next
ENV WARDEN_DATA_DIR /var/vcap/data/warden
ENV CONTAINER_DEPOT_PATH $WARDEN_DATA_DIR/depot
ENV PLATFORM_CONFIG $JOB_DIR/config/platform.yml

ENV TMPDIR /var/vcap/data/dea_next/tmp

RUN mkdir -p $PACKAGE_DIR && mkdir -p $DEA_NG_RUN_DIR && mkdir -p $WARDEN_RUN_DIR && mkdir -p $LOG_DIR && mkdir -p $WARDEN_DATA_DIR && mkdir -p $TMPDIR && mkdir -p $DEA_NG_DATA_DIR && mkdir -p $JOB_DIR/config && mkdir -p $CONTAINER_DEPOT_PATH && mkdir -p /var/vcap/packages/buildpack_cache

RUN echo 32768 61000 > /proc/sys/net/ipv4/ip_local_port_range
RUN sysctl -w net.ipv6.conf.all.disable_ipv6=1
RUN sysctl -w net.ipv6.conf.default.disable_ipv6=1

ADD dea.yml $JOB_DIR/config/
ADD warden.yml $JOB_DIR/config/
ADD rootfs_lucid64.tar.gz $PACKAGE_DIR
#Do not work for now
#RUN echo 5 > /proc/sys/net/ipv4/tcp_fin_timeout
#RUN echo 1 > /proc/sys/net/ipv4/tcp_tw_recycle
#RUN echo 1 > /proc/sys/net/ipv4/tcp_tw_reuse

CMD ["/usr/bin/supervisord"]