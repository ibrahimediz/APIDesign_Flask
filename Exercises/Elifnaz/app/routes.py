from app import app
from flask import render_template

@app.route("/")
@app.route("/index")

def index():
    baslik="Elifnaz"
    birim12={"birim":"test"}
    herhangi = [
        {"div":{"divadi":"ps"},
        "alan":"testing"
        },
        {"div":{"divadi":"smaca"},
        "alan":"testing123"
        }
    ]
    return render_template("index.html", title="", unit=birim12)