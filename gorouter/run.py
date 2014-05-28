#!/usr/bin/env python

import os
from jinja2 import *
from maestro.guestutils import *

#create Jinja2 environment object and refer to templates directory
env = Environment(loader=FileSystemLoader('/home/gorouter/'))
 
#create Jinja2 template object based for gorouter
template = env.get_template('conf.template')
natsIP=get_specific_host('nats','nats-1')
result=template.render(natsIP=natsIP)

with open("/home/gorouter/conf.yml","wb") as f:
    f.write(result)


os.execl('/usr/bin/supervisord', 'supervisord')
