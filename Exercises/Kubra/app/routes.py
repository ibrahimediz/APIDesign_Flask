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