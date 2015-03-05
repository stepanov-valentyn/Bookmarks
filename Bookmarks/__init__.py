__author__ = 'gareth'
from flask import Flask, render_template, url_for, request, redirect, flash
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

import os


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = '\xf9\x19\x96_\xcf\xc1\x97i\xfc\xb3\x85\xd1n4n!\x0e3\x08\xb7\xb86\x19g'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'Bookmarks.db')
db = SQLAlchemy(app)

import model
import view