from app import app
from flask import render_template, jsonify, request
import uuid

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

@app.get("/users")
def getUsers():
    return jsonify(users),200

@app.get("/users/<id>")
def getUserById(id):
    user = [*filter(lambda user: str(user["_id"]) == id, users)]
    if user:
        return jsonify(user[0]),200
    else:
        return jsonify({"Status Code": "404", "Message": "User Not Found"}),404

@app.put("/users/<id>")
def updateUserById(id):
    global users
    user = [*filter(lambda user: str(user["_id"]) == id, users)]
    newUserData =  request.get_json()
    if (newUserData and "name" in newUserData and newUserData["name"]):
        if user:
            print("found user, update the list")
            updateData = {"_id": id, "name": newUserData["name"]}
            users = [*map(lambda user: updateData if str(user["_id"]) == id else user, users)]
            return jsonify(updateData),200
        else:
            return jsonify({"Status Code": "404", "Message": "User Not Found"}),404
    else:
        return jsonify({"Status Code": "400", "Message": "Bad Request"}),400

@app.post("/users")
def createUser():
    global users
    newUserData =  request.get_json()
    if (newUserData and "name" in newUserData and newUserData["name"]):
        newUserData["_id"] = str(uuid.uuid4())
        users.append(newUserData)
        return jsonify(newUserData),201
    else:
        return jsonify({"Status Code": "400", "Message": "Bad Request"}),400