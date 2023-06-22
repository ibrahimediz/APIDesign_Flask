from app import app

katalog = [
    {
    "birim":"Yapay Zeka",
    "egitimler":[
        {
        "egitim":"Machine Learning",
        "sure":30
        }
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