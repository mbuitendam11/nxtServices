from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from forms import ContactUs
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
def business():
    return render_template("business-tax.html")

@app.route("/about-us")
def aboutUs():
    return render_template("about-us.html")

@app.route("/contact-us", methods=["GET", "POST"])
def contactUs():
    form = ContactUs()
    
    if form.validate_on_submit():
        pass

    return render_template("contact-us.html", form=form)

"""@app.route("/success", methods=["POST"])
def success():
    if form.validate:
        firstname = request.form["firstname"]
        lastname = request.form['lastname']
        email = request.form["email"]
        subject = request.form["subject"]
        desc = request.form["desc"]

        my_email = ""
        password = ""

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs=[f"{email}"],
                msg=f"Subject:{subject}\n\n{desc}\nKind regards,\n{firstname}{lastname}"
            )
        return f"Success! Review your email below \n\n Hi {firstname} {lastname}, <br> just confirming your email is {email} and heading {subject} <br> {desc}"
    return redirect(url_for("contactUs"))"""

if __name__ == "__main__":
    app.run(debug=True)