from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template("index.html", times=3, color="blue")

@app.route('/play/<num>')
def play_time(num):
    return render_template("index.html", times=int(num), color="blue")

@app.route('/play/<num>/<color>')
def play_time_color(num, color):
    return render_template("index.html", times=int(num), color=str(color))

if __name__=="__main__":
    app.run(debug=True)