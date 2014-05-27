FROM 10.10.103.215:5000/db
MAINTAINER Chen XingYu wizard_cxy@hotmail.com

EXPOSE 5524

CMD sysctl -w "kernel.shmmax=284934144" && su vcap -c "/var/vcap/install/postgress/bin/postgres -D /var/vcap/store/postgres"
