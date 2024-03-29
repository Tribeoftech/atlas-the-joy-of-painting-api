"""
Creates a Flask application instance with the given configuration.

Initializes SQLAlchemy with the given database URI and connects it to the
application instance. Returns the configured Flask application instance.
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def create_app():
	app = Flask(__name__)
	app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgres://postgres:hank@localhost:5432/postgres')
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	db.init_app(app)
	return app


app = create_app()

# app will not run, could not implement API in time for deadline
if __name__ == '__main__':
	app.run()