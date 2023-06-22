from app import app
from app.db import *
import uuid
from flask import request
from flask_smorest import abort

@app.get("/katalog/<string:birim_id>")
def getBirim(birim_id):
    try:
        return birimler[birim_id]
    except KeyError:
       abort(404,message="Birim Bulunamadı")

@app.get("/katalog")
def getBirimler():
    return {"birimler":list(birimler.values())}

@app.post("/katalog")
def postBirim():
    birimData = request.get_json()
    if "birim" not in birimData:
        abort(400,
        message="Bad Request,Gönderilen JSON data içerisinde Birim Adı Bulunamadı ",)
    birim_ID = uuid.uuid4().hex
    birim = {**birimData,"id":birim_ID}
    birimler[birim_ID] = birim
    return birim

@app.post("/egitim")
def postEgitim():
    egitimData = request.get_json()
    if ("sure" not in egitimData or "egitim" not in egitimData or "birim_id" not in egitimData):
        abort(400,message="Bad Request sure,egitim,birim_id parametrelerinin gönderildiğinde emin olun")
    if egitimData["birim_id"] not in birimler:
        return {"mesaj":"Birim Bulunamadı"} , 404
    egitimID = uuid.uuid4().hex
    egitim = {**egitimData,"id":egitimID}
    egitimler[egitimID] = egitim
    return egitim

@app.get("/egitim")
def getEgitimler():
    return {"egitimler":list(egitimler.values())}

@app.get("/egitim/<string:egitim_id>")
def getEgitim(egitim_id):
    try:
        return egitimler[egitim_id]
    except KeyError:
        abort(404,message="Eğitim Bulunamadı")





# @app.get("/katalog")
# def katalog_getir():
#     return {"katalog":birimler}

# from flask import request ####################
# @app.post("/katalog")
# def katalogolustur():
#     request_veri = request.get_json()
#     yeni_katalog = {"birim":request_veri["birim"],"egitimler":[]}
#     birimler.append(yeni_katalog)
#     return yeni_katalog,201
    
# from markupsafe import escape

# @app.post("/katalog/<string:isim>/egitimler") # 127:0.0.1:5000/katalog/Network/egitimler
# def egitimOlustur(isim):
#     request_veri = request.get_json()
#     for kat in katalog:
#         if kat["birim"] == escape(isim):
#             yeni_egitim = {"egitim":request_veri["egitim"],"sure":request_veri["sure"]}
#             kat["egitimler"].append(yeni_egitim)
#             return yeni_egitim,201
#     return {"mesaj":"Katalog Bulunamadı"}, 404


# @app.get("/katalog/<string:isim>")
# def birimGetir(isim):
#     for kat in katalog:
#         if kat["birim"] == isim:
#             return kat
#     return {"mesaj":"Katalog Bulunamadı"}, 404


# @app.get("/katalog/<string:isim>/egitimler")
# def egitimlerGetir(isim):
#     for kat in katalog:
#         if kat["birim"] == isim:
#             return {"egitimler":kat["egitimler"]}
#     return {"mesaj":"Katalog Bulunamadı"}, 404
