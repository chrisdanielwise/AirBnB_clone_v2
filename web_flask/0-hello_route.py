#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)


@app.route('/airbnb-onepage/')
def hello():
        return 'Hello, World!'


    if _name_ == '_main_':
            app.run(port=5000)
