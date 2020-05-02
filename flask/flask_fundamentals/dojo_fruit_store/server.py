from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    raspberry = request.form['raspberry']
    strawberry = request.form['strawberry']
    apple = request.form['apple']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']
    customer_name = first_name + " " + last_name
    count = int(apple)+int(strawberry)+int(raspberry)
    print(f"Charging {customer_name} for {count} fruits")
    return render_template("checkout.html", strawberry=strawberry, raspberry=raspberry, apple=apple, first_name=first_name, student_id= student_id, last_name=last_name)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)