from flask import Blueprint,render_template,request,redirect,flash,session,url_for,abort
myWeb  = Blueprint("myWebsite",__name__)
from forms.Form import (contactForm,signinForm,signupForm)
from models.model import User
from flask_login import login_user,logout_user


@myWeb.route("/")
def home():
	data = {
		"WebDevlopment":
			{
				"firstWeb":
				{
					"Title" : "My First Website",
					"mainImg": 'firstWeb.jpg',
					"techUsedImg":["html.png","css.png","js.png"],
					"linkGithub":"https://github.com/Crown003/Crown.git",
					"linkLive":"https://Crown003.github.io/Crown/",
				},
				"thisPortfolio":
				{
					"Title" :"This Portfoli Website",
					"mainImg":'newProtfolio.jpg',
					"techUsedImg":["flask.png","html.png","css.png","js.png"],
					"linkGithub":"",
					"linkLive":"",
				}
			},
		"SoftwareDevlopment":
			{
				"Test data":
				{
					"Title" : "My First Website",
					"mainImg": 'firstWeb.jpg',
					"techUsedImg":[],
					"linkGithub":"",
					"linkLive":"",
				}
				
			},
		"DataScience & AI":
			{
				"Test data":
				{
					"Title" : "My First Website",
					"mainImg": 'firstWeb.jpg',
					"techUsedImg":[],
					"linkGithub":"",
					"linkLive":"",
				}
				
			},
	}
	return render_template("index.html",data=data)
	
@myWeb.route("/contact",methods=["GET","POST"])
def contact():
	contactform = contactForm()
	if request.method == "POST":
		if contactform.validate_on_submit():
			name =contactform.name.data
			email = contactform.email.data
			message =contactform.message.data
			needSomeService = contactform.needSomeService.data
			data = {"Username":name,"Email":email,"Servicerequired":needSomeService,"Message":message}
			contactform = contactForm(formdata=None)
	return render_template("contact.html",contactform=contactform)


@myWeb.route("/services")
def services():
	return render_template("services.html")
	

@myWeb.route("/signin",methods=["GET","POST"])
def signin():
	form = signinForm()
	if request.method == "POST":
		if form.validate_on_submit():
			username = form.username.data
			password = form.password.data
			check = User.login_valid(username,password)
			form = signinForm(formdata=None)
			if check[0]:
				login_user(check[1])
				return redirect(url_for('myWebsite.home'))
	return render_template("signin.html",form=form)
	
@myWeb.route("/signup",methods=["GET","POST"])
def signup():
	form = signupForm()
	if request.method == "POST":
		if form.validate_on_submit():
			name = form.name.data
			email = form.email.data
			phone = form.phone.data
			password = form.password.data
			try:
				task = User.register(username=name,phone=phone,email=email,password=password)
				if task:
					flash("Signed Up successfully !")
					print("message flashed;")
				else:
					flash("User alredy exist with given details !")
			except Exception as e:
				print(e)
				flash("Oops something wents wrong !  Unable to SignUp.")
			form = signupForm(formdata=None)
	return render_template("signup.html",signupform=form)