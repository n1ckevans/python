from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_user():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    gender = request.form['gender']
    comments = request.form['comments']
    vehicle = request.form['vehicle']
    return render_template("result.html", name=name, location=location, language=language, comments=comments, gender=gender, vehicle=vehicle)

if __name__=="__main__":
    app.run(debug=True)