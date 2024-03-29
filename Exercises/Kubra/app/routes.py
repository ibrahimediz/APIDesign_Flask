from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    baslik="Markalar"
    birim={"birim":"Kozmetik"}
    parfum = [
        {"marka":{"markaAdi":"Yves Saint Laurent"},
        "parfumAdi":"Libre"
        },
        {"marka":{"markaAdi":"Burberry"},
        "parfumAdi":"Her"
        }
    ]
    return render_template("index.html",title=baslik,
    unit=birim,parfum=parfum)

    """
GET 127.0.0.1:4530/birimadi {"birim":"Yapay Zeka"}
POST 127.0.0.1:4530/birimadi {"birim":"Network","egitimler":[]}
"""
katalog = [
    {
    "birim":"Kozmetik",
    "parfum":[
        {
        "marka":"Yves Saint Laurent",
        "luks":"Evet"
        }]}]
@app.get("/katalog")
def katalog_getir():
    return {"katalog":katalog}


#from flask import request ####################
#@app.post("/katalog")
#def katalogolustur():
#    request_veri = request.get_json()
#    yeni_katalog = {"birim":request_veri["birim"],"parfum":[]}
#    katalog.append(yeni_katalog)
#    return yeni_katalog,201

from flask import request ####################
@app.post("/katalog/<string:isim>/parfum") # 127:0.0.1:5000/katalog/Network/parfum
def markaOlustur(isim):
    request_veri = request.get_json()
    for kat in katalog:
        if kat["birim"] == isim:
            yeni_marka = {"marka":request_veri["marka"],"luks":request_veri["luks"]}
            kat["parfum"].append(yeni_marka)
            return yeni_marka,201
    return {"mesaj":"Katalog Bulunamadı"}, 404

