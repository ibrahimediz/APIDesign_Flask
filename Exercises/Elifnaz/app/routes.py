from app import app
from flask import render_template

@app.route("/")
@app.route("/index")

def index():
    baslik="Elifnaz"
    birim12={"birim":"test"}
    herhangi = [
        {"div":{"divadi":"ps"},
        "alan":"testing"
        },
        {"div":{"divadi":"smaca"},
        "alan":"testing123"
        }
    ]
    return render_template("index.html", title="", unit=birim12,
    herhangi=herhangi)

katalog = [
    {
    "birim":"test",
    "herhangi":[
        {
        "divi":"testing",
        "sure":30
        }]},
         {
    "birim":"telelelli",
    "herhangi":[
        {
        "divi":"off",
        "sure":130
        }]}
        ]

@app.get("/katalog")
def katalog_getir():
    return {"katalog":katalog}

from flask import request ####################
@app.post("/katalog")
def katalogolustur():
    request_veri = request.get_json()
    yeni_katalog = {"birim":request_veri["birim"],"herhangi":[]}
    katalog.append(yeni_katalog)
    return yeni_katalog,201

@app.post("/katalog/<string:isim>/herhangi") # 127:0.0.1:4620/katalog/Network/egitimler
def egitimOlustur(isim):
    request_veri = request.get_json()
    for kat in katalog:
        if kat["birim"] == isim:
            yeni = {"divi":request_veri["divi"],"sure":request_veri["sure"]}
            kat["herhangi"].append(yeni)
            return yeni,201
    return {"mesaj":"Katalog Bulunamadı"}, 404
            