# flask_blog/__init__.py

from flask import Flask

app = Flask(__name__)

import flask_blog.views

