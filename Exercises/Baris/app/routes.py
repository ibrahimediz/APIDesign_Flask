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

@app.post("/animals")
def postAnimals():
    animalData = request.get_json()
    animal_ID = uuid.uuid4().hex
    animal = {**animalData,"id":animal_ID}
    animals[animal_ID] = animal
    return animal

@app.post("/variety")
def postVariety():
    varietyData = request.get_json()
    if varietyData["birim_id"] not in stores:
        return {"mesaj":"Birim Bulunamadı"} , 404
    varietyID = uuid.uuid4().hex
    egitim = {**varietyData,"id":varietyID}
    varities[varietyID] = variety
    return variety

@app.post("/animals/<string:isim>")
def createAnimal(isim):
    request_veri = request.get_json()
    for i in animals:
        if i["animals"] == isim:
            new_animal = {"variety":request_veri["variety"],"color":request_veri["color"]}
            kat["animals"].append(new_animal)
            return new_animal,201,
    return {"mesaj":"Katalog Bulunamadı"}, 404