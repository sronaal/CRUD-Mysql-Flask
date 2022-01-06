from flask import Flask
from routes.products import productos
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://user:password@localhost/market"
SQLAlchemy(app)

app.register_blueprint(productos)



    