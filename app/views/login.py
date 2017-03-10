# -*- coding:utf-8 -*-

from app import app
from flask import request, render_template, flash, redirect
from app.models import account


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = str(request.form.get("username"))
        pwd = str(request.form.get("pwd"))
        res = account.login(name, pwd)
        if res["status"] == 0:
            flash(res["message"], "alert-warning")
        else:
            return redirect("/index")
    return render_template("login.html")






