from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField, DateField, SelectField, DateTimeField
from wtforms.validators import DataRequired, Optional
from flask_ckeditor import CKEditorField

# Contact Us Form

class ContactUs(FlaskForm):
    name = StringField("Your Full Name", validators=[DataRequired()])
    email = EmailField("Email Address", validators=[DataRequired()])
    subject = StringField("Subject", validators=[DataRequired()])
    desc = CKEditorField("How can we help you today?", validators=[DataRequired()])
    submit = SubmitField("Send")