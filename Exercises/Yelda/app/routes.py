from app import app
from flask import render_template

@app.route("/")
@app.route("/index")

def index():
    baslik="Kediler"
    altBaslik={"altBaslik":"Kedi Irkları"}
    kediIrklari=[
        {"irk":{"isim":"Ankara Kedisi"},
         "ozellik":"sdfasdfasdf"
        },
        {"irk":{"isim":"Bombay"},
         "ozellik":"klşhjkljl"
        },
        {"irk":{"isim":"Himalayan"},
         "ozellik":"rtwertwert"
        },
        {"irk":{"isim":"Persian"},
         "ozellik":"cvxcvnxcv"
        }
    ]
    return render_template("index.html",title=baslik,unit=altBaslik, kediIrklari=kediIrklari)


###################################################################

kittens = [
    {
    "altBaslik":"Kedi Irkları",
    "kediIrklari":[
        {"irk":{"isim":"Ankara Kedisi"},
         "ozellik":"sdfasdfasdf"
        },
        {"irk":{"isim":"Bombay"},
         "ozellik":"klşhjkljl"
        },
        {"irk":{"isim":"Himalayan"},
         "ozellik":"rtwertwert"
        },
        {"irk":{"isim":"Persian"},
         "ozellik":"cvxcvnxcv"
        }
    ]}]
@app.get("/kittens")
def kediIrklari_getir():
    return {"kittens":kittens}


###################################################################
from flask import request ####################
@app.post("/kittens")
def kittenOlustur():
    request_veri = request.get_json()
    yeni_kitten = {"altBaslik":request_veri["altBaslik"],"kediIrklari":[]}
    kittens.append(yeni_kitten)
    return yeni_kitten,201