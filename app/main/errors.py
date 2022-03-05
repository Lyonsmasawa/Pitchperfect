from flask import render_template
from . import main #import the blueprint instance main

@main.app_errorhandler(404) #application wide error handler
def four_Ow_four(error):
    return render_template('fourOwfour.html'),404