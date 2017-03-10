# -*- coding:utf-8 -*-

from fabric.api import run, env

env.hosts = ['192.168.1.242:22']
env.user = 'root'
env.password = '111111'

def test():
    run('nohup /data/tomcat2/bin/startup.sh')

