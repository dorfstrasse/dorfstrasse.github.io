from flask import Flask
from flask_bootstrap import Bootstrap
from flask_wtf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = 'eskybk2023'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://default:rse2IPfnQSx5@ep-ancient-math-184814.ap-southeast-1.postgres.vercel-storage.com:5432/verceldb'
bootstrap = Bootstrap(app)


import application.controller.routes