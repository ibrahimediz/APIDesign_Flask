from app import app
from flask import render_template

@app.route("/")
@app.route("/index")

def index():
    baslik="Kediler"
    altBaslik={"altBaslik":"Kedi Irkları"}
    kediIrklari=[
        {"irk":{"isim":"Ankara Kedisi"},
         "ozellik":"sdfasdfasdf"
        },
        {"irk":{"isim":"Bombay"},
         "ozellik":"klşhjkljl"
        },
        {"irk":{"isim":"Himalayan"},
         "ozellik":"rtwertwert"
        },
        {"irk":{"isim":"Persian"},
         "ozellik":"cvxcvnxcv"
        }
    ]
    return render_template("index.html",title=baslik,unit=altBaslik, kediIrklari=kediIrklari)
    