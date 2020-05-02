from flask import Flask, render_template, redirect, session, request
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods=['POST', 'GET'])
def index():
    count = session.get('visits') 
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1  # reading and updating session data
    else:
        session['visits'] = 1 # setting session data
    return render_template("index.html", count=count)

@app.route('/reset', methods=['POST', 'GET'])
def delete_visits():
    reset = request.form['reset']
    session.pop('visits', 1)
    return redirect("/")

if __name__=="__main__":
     app.run(debug=True)