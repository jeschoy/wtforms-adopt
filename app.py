from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from flask import Flask, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db

app = Flask(__name__)

app.config['SECRET_KEY'] = 'whatabigsecret'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.app_context().push()
connect_db(app)

db.create_all()

toolbar = DebugToolbarExtension(app)

