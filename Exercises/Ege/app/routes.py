from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    baslik = "Ege Ekmekcioglu"
    birimAdi = {"birim": "Ekonomi"}
    egitimler = [
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
    return render_template("index.html", title=baslik, unit=birim)