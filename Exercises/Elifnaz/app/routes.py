from app import app
from app.db import *
import uuid
from flask import request

@app.get("/katalog/<string:deneme_id>")
def getdeneme(deneme_id):
    try:
        return denemeler[deneme_id]
    except KeyError:
        return {"mesaj": "Birim bulunamadı"}, 404

@app.get("/katalog")
def getdenemeler():
    return {"denemeler":list.denemeler.values()}

@app.post("/katalog")
def postMakale():
    MakaleData = request.get_json()
    Makale_ID = uuid.uuid4().hex
    makale = {**MakaleData,"id":Makale_ID}
    makaleler[Makale_ID] = makale
    return makale







@app.get("/katalog")
def katalog_getir():
    return {"katalog":deneme}


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

@app.get("/katalog/<string:isim>")
def birimGetir(isim):
    for kat in katalog:
        if kat["birim"] == isim:
            return kat
    return {"mesaj":"Katalog Bulunamadı"}, 404


@app.get("/katalog/<string:isim>/herhangi")
def egitimlerGetir(isim):
    for kat in katalog:
        if kat["birim"] == isim:
            return {"herhangi":kat["herhangi"]}
    return {"mesaj":"Katalog Bulunamadı"}, 404