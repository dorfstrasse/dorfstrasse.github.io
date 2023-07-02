from application import app
from flask import Flask,render_template,redirect, request,url_for,session
from application.routes.index import *
# from application.routes.login import *

# @app.route('/')
# def index():
    # return redirect(url_for('home'))
    # if session.get('login') == True:
    #     return redirect(url_for('home'))
    # else:
    #     return redirect(url_for('home'))

@app.errorhandler(404)
def page_not_found(e):
        return render_template('98-error-404.html'),404
