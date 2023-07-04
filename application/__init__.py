from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://default:rse2IPfnQSx5@ep-ancient-math-184814.ap-southeast-1.postgres.vercel-storage.com:5432/verceldb'
bootstrap = Bootstrap(app)


import application.controller.routes