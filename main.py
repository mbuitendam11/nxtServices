from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
import os, smtplib


app = Flask(__name__)
Bootstrap5(app)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/peronsal-tax")
def personal():
    return render_template("personal-tax.html")

@app.route("/business-tax")
def personal():
    return render_template("business-tax.html")

@app.route("/about-us")
def personal():
    return render_template("about-us.html")

@app.route("/contact-us")
def personal():
    return render_template("contact-us.html")

if __name__ == "__main__":
    app.run(debug=True)