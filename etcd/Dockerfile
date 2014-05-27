FROM 10.10.103.215:5000/etcd
MAINTAINER Chen XingYu wizard_cxy@hotmail.com

ENV WORKDIR /var/vcap/store/etcd
RUN mkdir -p $WORKDIR


EXPOSE 4001
EXPOSE 7001
CMD /etcd/bin/etcd -snapshot -data-dir=$WORKDIR \
    -addr=10.10.18.45:4001 \
    -peer-addr=10.10.18.45:7001 \
    -name=micro_ng-0