# -*- coding:utf-8 -*-
import MySQLdb

def login(username, password):
    username = MySQLdb.escape_string(username)
    password = MySQLdb.escape_string(password)
    if username == '' or password == '':
        return {"status": 0, "message": u"用户名或密码不能为空！"}
    else:
        return {"status": 1, "message": u"未知错误！"}


