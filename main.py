from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from forms import ContactUs
import os, smtplib


app = Flask(__name__)
app.config['SECRET_KEY'] = "os.environ.get('FLASK_KEY')"
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
    ## Need to work on this section, currently a built form and then html form is not set up for WTForms
    if form.validate_on_submit():
        name = form.name.data,
        email = form.email.data,
        subject = form.subject.data,
        desc = form.desc.data,

        my_email = ""
        password = ""

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs=[f"{my_email}"],
                msg=f"Subject:{subject[0]}\n\n{desc[0]}\nEmail:{email[0]}Kind regards,\n{name[0]}"
            )
            connection.sendmail(
                from_addr=my_email, 
                to_addrs=[f"{email[0]}"],
                msg=f"Subject:Thanks for enquiring!\n\nThanks for enquiring with Nxt Services. A rep will be in touch about next steps."
            )

        return f"Success! Review your email below \n\n Hi {name[0]}, <br> just confirming your email is {email[0]} and heading {subject[0]} <br> {desc[0]}"

    return render_template("contact-us.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)