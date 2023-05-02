from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "thisisasecretkey"

@app.route("/hello")
def index():
    flash("What is your Name?")
    return render_template("index.html")


@app.route("/greet", methods=['GET','POST'])
def greet():
    flash("Hello " + str(request.form["name_input"]) + " , nice to meet you!")
    return render_template("index.html")