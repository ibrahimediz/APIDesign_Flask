from app import app
from flask import render_template
@app.route("/")
@app.route("/index")
def index():
    baslik="Petstore"
    birim={"birim":"animal"}
    egitimler = [
        {"animal":{"variety":"golden"},
        "color":"dark brown"
        },
        {"animal":{"variety":"bulldog"},
        "color":"black"
        },
        {"animal":{"variety":"terrier"},
        "color":"white"
        },
        {"animal":{"variety":"pitbull"},
        "color":"white"
        },
        {"animal":{"variety":"spaniel"},
        "color":"brown"
        }
    ]
    
    return render_template("index.html",title="",unit=birim)