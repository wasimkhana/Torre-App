from flask import render_template, url_for
from app import app


@app.route('/')
def hello_world():
    """
    hello_world function to test route.
    return: layout.html
    """
    return render_template("layout.html")
