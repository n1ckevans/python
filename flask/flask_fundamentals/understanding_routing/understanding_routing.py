from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say_name(name):
    return "Hi " + str(name) + "!"

@app.route('/repeat/<num>/<name>')
def repeat(num, name):
    return str(name) * int(num)

@app.route('/<path>')
def not_found(path):
    return render_template("404.html")

if __name__=="__main__":
    app.run(debug=True)