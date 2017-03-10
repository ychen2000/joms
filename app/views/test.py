# -*- coding:utf-8 -*-

from app import app
from fabric.api import lcd, local


@app.route("/test")
def test():
    with lcd('/data/ychen/flask/joms/app/'):
        local('fab test')
    return 'aa'

