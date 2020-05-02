from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect("/show")	# changed this line!
    
# adding this method
@app.route("/show")
def show_user():
    freturn render_template('show.html')

if __name__ == "__main__":
    app.run(debug=True)