from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField,PasswordField,IntegerField,BooleanField,EmailField)
from wtforms.validators import InputRequired


class contactForm(FlaskForm):
	name = StringField('Name : ', validators=[InputRequired()])
	email = EmailField('Email : ',validators=[InputRequired()])
	message = TextAreaField("Message : ",validators=[InputRequired()])
	needSomeService = BooleanField("Need some service ?")

class signinForm(FlaskForm):
	username = StringField('Username or Email : ', validators=[InputRequired()])
	password = PasswordField("Password : ",validators=[InputRequired()])

class signupForm(FlaskForm):
	name = StringField('Name : ', validators=[InputRequired()])
	email = EmailField('Email : ',validators=[InputRequired()])
	phone = IntegerField("Contact number : ")
	password = PasswordField("Password : ",validators=[InputRequired()])