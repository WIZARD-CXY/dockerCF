#!/usr/bin/env python

import os
from jinja2 import *
from maestro.guestutils import *

#create Jinja2 environment object and refer to templates directory
env = Environment(loader=FileSystemLoader('/cloud_controller_ng/config/'))
 
#create Jinja2 template object based for gorouter
template = env.get_template('conf.template')

templateVars = {}
templateVars["local_route"] = os.environ.get("local_route")
templateVars["natsIP"] = get_specific_host('nats','nats-1')
templateVars["external_domain"] = os.environ.get("external_domain")
templateVars["system_domain"] = os.environ.get("system_domain")
templateVars["app_domains"] = os.environ.get("app_domains")
templateVars["ccdbUserName"] = os.environ.get("ccdbUserName")
templateVars["ccdbPassWord"] = os.environ.get("ccdbPassWord")
templateVars["ccdbHost"] = get_specific_host('db','pg-1')
templateVars["uaaHost"] = os.environ.get("uaaHost")

result=template.render(templateVars)

with open("/cloud_controller_ng/config/cloud_controller.yml","wb") as f:
    f.write(result)


os.execl('/usr/bin/supervisord', 'supervisord')