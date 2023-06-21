from app import app
from flask import render_template

counter = 0
routes = [
    {"path": "index", "title": "Home Page"}, 
{"path": "about", "title": "About"}, 
{"path": "support", "title": "Contact Us"}]

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

users = [{"_id": 1, "name": "ali"},{"_id": 2, "name": "veli"},{"_id": 3, "name": "ahmet"},{"_id": 4, "name": "cem"},{"_id": 5, "name": "mert"}]
@app.get("/users/<id>")
def getUserById(id):
    print(type(id))
    return filter(lambda user: item['_id'] == id, users)