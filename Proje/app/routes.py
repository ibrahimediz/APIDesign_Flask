from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    baslik="Dijital Vizyon"
    birimAdi={"birim":"Yapay Zeka"}
    egitimler = [
        {"egitmen":{"egitmenAdi":"İbrahim"},
        "alan":"Machine Learning"
        },
        {"egitmen":{"egitmenAdi":"Erdal"},
        "alan":"Network Programming"
        }
    ]
    return render_template("index.html",title="",
    unit=birimAdi,egitimler=egitimler)

"""
GET 127.0.0.1:4530/birimadi {"birim":"Yapay Zeka"}
POST 127.0.0.1:4530/birimadi {"birim":"Network","egitimler":[]}
"""


katalog = [
    {
    "birim":"Yapay Zeka",
    "egitimler":[
        {
        "egitim":"Machine Learning",
        "sure":30
        }]}]

@app.get("/katalog")
def katalog_getir():
    return {"katalog":katalog}

from flask import request ####################
@app.post("/katalog")
def katalogolustur():
    request_veri = request.get_json()
    yeni_katalog = {"birim":request_veri["birim"],"egitimler":[]}
    katalog.append(yeni_katalog)
    return yeni_katalog,201
