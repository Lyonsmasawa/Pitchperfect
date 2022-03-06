from flask import render_template
from . import main

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/what')
def what():
    return render_template('what.html')