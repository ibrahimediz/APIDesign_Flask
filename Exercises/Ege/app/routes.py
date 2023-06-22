from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    baslik = "Ege Ekmekcioglu"
    birimAdi = {"birim": "Ekonomi"}
    isimler = [
        {"İktisatci": {"ismi": "Milton"},
            "alan": "Kamu Ekonomi"
        },
        {"İktisatci": {"ismi": "Adam"},
            "alan": "Serbest Ekonomi"
        },
        {"İktisatci": {"ismi": "David"},
            "alan": "Karsilastirmali Ekonomi"
        }
    ]
    return render_template("index.html", title=baslik, unit=birimAdi, isimler=isimler)


katalog = [
    {
    "birim":"Ekonomi",
    "isimler":[
        {
        "isim":"Milton",
        "sure":30
        }]}]
@app.get("/katalog")
def katalog_getir():
    return {"katalog":katalog}

from flask import request ####################
@app.post("/katalog")
def katalogolustur():
    request_veri = request.get_json()
    yeni_katalog = {"birim":request_veri["birim"],"isimler":[]}
    katalog.append(yeni_katalog)
    return yeni_katalog,201

from markupsafe import escape

@app.post("/katalog/<string:isim>/isimler") # 127:0.0.1:5000/katalog/Network/egitimler
def egitimOlustur(isim):
    request_veri = request.get_json()
    for kat in katalog:
        if kat["birim"] == isim:
            yeni_isim = {"ismi":request_veri["ismi"],"sure":request_veri["sure"]}
            kat["isimler"].append(yeni_isim)
            return yeni_egitim,201
    return {"mesaj":"Katalog Bulunamadı"}, 404




