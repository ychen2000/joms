from app import app
from flask import session

@app.route("/test")
def test():
    return session['username']
