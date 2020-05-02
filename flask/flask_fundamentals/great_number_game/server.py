from flask import Flask, render_template, redirect, session, request
import os, random, ctypes

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.static_folder = 'static'

winners = []

@app.route('/', methods=['POST', 'GET'])
def index():
    if not session.get('number'):
        session['number'] = random.randint(1,100)
    print(session['number'])
    return render_template("index.html")

@app.route('/user_guess', methods=['POST', 'GET'])
def user_guess():
    if not request.form['guess'].isdigit() or (int(request.form['guess']) < int(0)) or (int(request.form['guess']) > int(100)):
        return redirect("/")
 
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1  # reading and updating session data
    else:
        session['visits'] = 1 # setting session data
    count = session.get('visits') 

    if count == int(5):
        session.clear()
        return render_template("lose.html")
  
    if session['number'] == int(request.form['guess']):
        return render_template("correct.html", number=session['number'], count=count)
    elif session['number'] > int(request.form['guess']):
        return render_template("low.html", number=session['number'], count=count)
    elif session['number'] < int(request.form['guess']):
        return render_template("high.html", number=session['number'], count=count)

@app.route('/leaderboard', methods=['POST', 'GET'])
def post_score():
    winners.append({
        "name": request.form["name"],
        "count": session.get("visits")
    })
    print(winners[0]['name'])
    return render_template("leaderboard.html", winners=winners)

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect("/")

if __name__=="__main__":
     app.run(debug=True)