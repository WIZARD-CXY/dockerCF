#!/usr/bin/env python

import os
from jinja2 import *
from maestro.guestutils import *

#create Jinja2 environment object and refer to templates directory
env = Environment(loader=FileSystemLoader('/home/hm9000/'))
 
#create Jinja2 template object based for gorouter
template = env.get_template('hm9000.template')

templateVars = {}
templateVars["natsIP"] = get_specific_host('nats','nats-1')
templateVars["etcdIP"] = get_specific_host('etcd','etcd-1')
templateVars["ccngIP"] = get_specific_host('ccng','ccng-1')

result=template.render(templateVars)

with open("/home/hm9000.json","wb") as f:
    f.write(result)


os.execl('/usr/bin/supervisord', 'supervisord')