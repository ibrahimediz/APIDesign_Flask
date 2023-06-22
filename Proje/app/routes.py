from app import app


katalog = [
    {
    "birim":"Yapay Zeka",
    "egitimler":[
        {
        "egitim":"Machine Learning",
        "sure":30
        },
        {
        "egitim":"Deep Learning",
        "sure":35
        }
        ]
        },
    {
    "birim":"Java",
    "egitimler":[
        {
        "egitim":"Introduction Java",
        "sure":50
        },
        ]
        },
        ]

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


@app.post("/katalog/<string:isim>/egitimler") # 127:0.0.1:5000/katalog/Network/egitimler
def egitimOlustur(isim):
    request_veri = request.get_json()
    for kat in katalog:
        if kat["birim"] == isim:
            yeni_egitim = {"egitim":request_veri["egitim"],"sure":request_veri["sure"]}
            kat["egitimler"].append(yeni_egitim)
            return yeni_egitim,201
    return {"mesaj":"Katalog Bulunamadı"}, 404