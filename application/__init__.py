from flask import Flask,render_template,redirect, request,url_for,session
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = 'vander2212'
bootstrap = Bootstrap(app)

import application.controller.routes