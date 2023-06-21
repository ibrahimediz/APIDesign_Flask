from app import app
from flask import render_template, jsonify

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
    user = [*filter(lambda user: str(user["_id"]) == id, users)]
    if user:
        return jsonify(user[0])
    else:
        return jsonify({"Status Code": "404", "Message": "User Not Found"})

@app.put("/users/<id>")
def updateUserById(id):
    user = [*filter(lambda user: str(user["_id"]) == id, users)]
    newUserData =  request.get_json()
    if (newUserData and newUserData["name"]):
        if user:
            print("found user, update the list")
            return jsonify(user[0])
        else:
            return jsonify({"Status Code": "404", "Message": "User Not Found"})
    else:
        return jsonify({"Status Code": "400", "Message": "Bad Request"})