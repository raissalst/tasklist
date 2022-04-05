from os import getenv

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app: Flask):
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DB_URI")

    db.init_app(app)

    app.db = db

    from app.models import CategoryModel, EisenhowerModel, TaskModel, tasks_categories
