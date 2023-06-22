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

irklar = [
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
@app.get("/irklar")
def irklari_getir():
    return {"irklar":irklar}


###################################################################
from flask import request ####################
@app.post("/irklar")
def irkOlustur():
    request_veri = request.get_json()
    yeni_irk = {"altBaslik":request_veri["altBaslik"],"kediIrklari":[]}
    irklar.append(yeni_irk)
    return yeni_irk,201

############################################################
@app.post("/irklar/<string:isim>/kediIrklari") # 127:0.0.1:5000/katalog/Network/egitimler
def irkEkle(isim):
    request_veri = request.get_json()
    for irkList in irklar:
        if irkList["altbaslik"] == isim:
            yeni_kediIrki = {"irk":request_veri["irk"],"ozellik":request_veri["ozellik"]}
            irkList["kediIrklari"].append(yeni_kediIrki)
            return yeni_kediIrki,201
    return {"mesaj":"Katalog Bulunamadı"}, 404