from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from forms import ContactUs
import os, smtplib


app = Flask(__name__)
app.config['SECRET_KEY'] = "os.environ.get('FLASK_KEY')"
Bootstrap5(app)

@app.route("/", methods=["GET", "POST"])
def index():
    form = ContactUs()
        
    if form.validate_on_submit():
        name = form.name.data,
        email = form.email.data,
        subject = form.subject.data,
        desc = form.desc.data,

        my_email = os.environ.get('email')
        password = os.environ.get('Password')

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

        
        return redirect(url_for('index'))
    
    return render_template("index.html", form=form)

@app.route("/personal-tax")
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
        name = form.name.data,
        email = form.email.data,
        subject = form.subject.data,
        desc = form.desc.data,

        my_email = os.environ.get('email')
        password = os.environ.get('Password')

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs=[f"{my_email}"],
                msg=f"Subject:{subject[0]}\n\n{desc[0]}\n\nEmail:{email[0]}Name:\n\n{name[0]}"
            )
            connection.sendmail(
                from_addr=my_email, 
                to_addrs=[f"{email[0]}"],
                msg=f"Subject:Thanks for enquiring!\n\nThanks for enquiring with Nxt Services. A rep will be in touch about next steps.\n\nKind regards,\nNxt Team"
            )

        return redirect(url_for('index'))

    return render_template("contact-us.html", form=form)

@app.route("/Whoops")
def building():
    return render_template("404.html")

if __name__ == "__main__":
    app.run(debug=True)