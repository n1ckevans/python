from flask import Flask, render_template, redirect, session, request
import os, random, ctypes, datetime

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.static_folder = 'static'

activities = []

@app.route('/', methods=['POST', 'GET'])
def index():
    if not session.get('gold'):
        session['gold'] = 0
        session['activities'] = ""
    return render_template("index.html")

@app.route('/process_money', methods=['POST', 'GET'])
def gold():
    if request.form['type'] == 'farm':
        num = random.randint(10,20)
        session['gold'] += num
        session['activities'] += f"Earned {num} gold from farm! {datetime.datetime.now()}" +'\n'
 
    elif request.form['type'] == 'cave':
        num = random.randint(5,10)
        session['gold'] += num
        session['activities'] += f"Earned {num} gold from cave! {datetime.datetime.now()}"+'\n'

    elif request.form['type'] == 'house':
        num = random.randint(2,5)
        session['gold'] += num
        session['activities'] += f"Earned {num} gold from house! {datetime.datetime.now()}"+'\n'
        
    elif request.form['type'] == 'casino':
        num = random.randint(-50,50)
        session['gold'] += num
        if num <= 0:
            session['activities'] += f"Lost {num} gold from casino! {datetime.datetime.now()}"+'\n'
        else:
            session['activities'] += f"Earned {num} gold from casino! {datetime.datetime.now()}"+'\n'
    return redirect('/')

if __name__=="__main__":
     app.run(debug=True)