from app import app
from flask import render_template

counter = 0
routes = [{"path": "index", "title": "Home Page"}, {"path": "about", "title": "About"}, {"path": "support", "title": "Contact Us"}]

@app.route("/")
@app.route("/index")
def index():
    global counter
    counter += 1
    return render_template('index.html', counter=counter, routes=routes)


@app.route("/about")
@app.route("/support")
def others():
    return render_template('others.html')