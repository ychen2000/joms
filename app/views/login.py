from app import app
from flask import request, session, redirect, url_for

@app.route("/login", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect('/test')
    return'''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''








