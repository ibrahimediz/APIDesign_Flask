from app import app
from flask import render_template

@app.route("/")
@app.route("/index")

def index():
    baslik="Kediler"
    altBaslik={"altBaslik":"Kedi Irkları"}
    kediIrklari=[
        {"irk":{"isim":"Ankara Kedisi"},
         "ozellik":""
        },
        {"irk":{"isim":"Bombay"},
         "ozellik":""
        },
        {"irk":{"isim":"Himalayan"},
         "ozellik":""
        },
        {"irk":{"isim":"Persian"},
         "ozellik":""
        }
    ]
    return render_template("index.html")