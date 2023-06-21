
"""
    ilk flask uygulamanızı yazmak ve başlatmak için port numarasını 4527 kullanabilirsiniz.
    Hoşgeldiniz mesajı yerine isim ve soyisminizi yazmanız yeterlidir. 
"""
    
from flask import Flask


app = Flask(__name__)

@app.route("/")
def selam():
    return "Hoşgeldiniz"


if __name__ == '__main__':
    app.run(port=4510)