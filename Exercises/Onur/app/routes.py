from app import app

port = 30001
counter = 0

@app.route("/")
@app.route("/index")
def index():
    global counter
    counter += 1
    print(counter)
    return """
    <html>
        <head>
            <title>Hello World</title>
        </head>
        <body>
            <h1>Welcome!</h1>
            <p>You are our {}th visitor today.</p>
        </body>
    </html>
    """.format(counter)
    # return "Hello World!\nYou are our " + str(counter) + "th visitor today."