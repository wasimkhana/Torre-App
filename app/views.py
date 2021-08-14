from flask import render_template, url_for
from app import app
import requests
import json

@app.route('/')
@app.route('/about')
def about():
    """
    about method is to show the data from api
    return: layout.html, api_data
    """
    req = requests.get('https://torre.bio/api/bios/wasimkhanak5')
    api_data=json.loads(req.content)
    return render_template("about.html", data=api_data, title='About')
