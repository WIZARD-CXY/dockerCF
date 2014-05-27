FROM 10.10.103.215:5000/baseruby
MAINTAINER Chen XingYu wizard_cxy@hotmail.com

# simply use gem install to install nats

RUN apt-get update && apt-get install -y openssh-server supervisor && mkdir -p /var/run/sshd && mkdir -p /var/log/supervisor
RUN echo 'root:haha' | chpasswd

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD Gemfile /home/nats/
RUN cd /home/nats/ && BUNDLE_WITHOUT=development:test bundle package --all && \
    bundle install --local --deployment --without development test 
# run the nats server
EXPOSE 22 4222

CMD ["/usr/bin/supervisord"]

