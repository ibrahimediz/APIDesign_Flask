from app import app
from flask import render_template
@app.route("/")
@app.route("/index")
def index():
    baslik="Petstore"
    birim={"birim":"animals"}
    animals = [
        {"animal":{"variety":"golden"},
        "color":"dark brown"
        },
        {"animal":{"variety":"bulldog"},
        "color":"black"
        },
        {"animal":{"variety":"terrier"},
        "color":"white"
        },
        {"animal":{"variety":"pitbull"},
        "color":"white"
        },
        {"animal":{"variety":"spaniel"},
        "color":"brown"
        }
    ]
    
    return render_template("index.html",title="",unit=animals,variety=variety)

animals = [
    {
    "variety":"pitbull",
    "color":[
        {
        "egitim":"brown",
        "age":4
        }]}]
@app.get("/animals")
def katalog_getir():
    return {"animals":animals}

from flask import request ####################
@app.post("/animals")
def katalogolustur():
    request_veri = request.get_json()
    yeni_katalog = {"variety":request_veri["variety"],"color":[]}
    animals.append(yeni_katalog)
    return yeni_katalog,201    

