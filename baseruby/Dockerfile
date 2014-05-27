FROM 10.10.103.215:5000/myubuntu12.04

MAINTAINER Chen XingYu wizard_cxy@hotmail.com

# Install ruby.
ADD http://ruby.taobao.org/mirrors/ruby/ruby-1.9.3-p545.tar.gz /tmp/
RUN apt-get update && apt-get -y install build-essential zlib1g-dev libssl-dev libreadline6-dev libyaml-dev && \ 
    tar -zxf /tmp/ruby-1.9.3-p545.tar.gz && \
    (cd ruby-1.9.3-p545/ && ./configure --disable-install-doc && make && make install) && \
    rm -rf ruby-1.9.3-p545/ && \
    rm -f /tmp/ruby-1.9.3-p545.tar.gz
# change the RubyGems source to taobao source
RUN gem sources --remove http://rubygems.org/ && \
    gem sources -a http://ruby.taobao.org/ && \
    gem sources -l
# install bundle using gems
RUN gem install bundler
