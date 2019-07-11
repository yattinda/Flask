# flask_blog/__init__.py

from flask_blog import app

@app.route("/")
def show_entries():
	return "Hello world"



