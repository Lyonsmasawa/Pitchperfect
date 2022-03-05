from turtle import title
from flask import render_template
from . import main

@main.route('/')
def index():
    """
    Root page
    """
    title = "Pitches"

    return render_template('index.html', title = title)