from flask import render_template
from . import main

@main.errorhandler(404)
def fourOwfour(error):
    '''
    Function that will render the 404 error page
    '''
    return render_template('fourOwfour.html'), 404