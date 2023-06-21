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


