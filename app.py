from flask import Flask


app = Flask(__name__)

@app.route("/")
def selam():
    return "Hoşgeldiniz"


if __name__ == '__main__':
    app.run(port=4510)