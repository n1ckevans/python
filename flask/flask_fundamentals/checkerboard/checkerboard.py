from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def board():
     return render_template("index.html", x= int(6), y=int(6))
    # return render_template("index.html", times=20, color="blue")

@app.route('/<x>')
def boardx(x):
    return render_template("index.html", x=int(x), y=int(6))

@app.route('/<x>/<y>')
def boardxy(x, y):
    return render_template("index.html", x=int(x), y=int(y))

if __name__=="__main__":
    app.run(debug=True)