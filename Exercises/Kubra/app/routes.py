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