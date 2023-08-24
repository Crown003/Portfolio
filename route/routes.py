from flask import Blueprint,render_template,request
myWeb  = Blueprint("myWebsite",__name__)
from forms.Form import (contactForm,signinForm,signupForm)
from flask_login import login_required
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
	form = contactForm()
	if request.method == "POST":
		if form.validate_on_submit():
			name = form.name.data
			email = form.email.data
			message = form.message.data
			needSomeService = form.needSomeService.data
			data = {"Username":name,"Email":email,"Servicerequired":needSomeService,"Message":message}
			form = contactForm(formdata=None)
	return render_template("contact.html",form=form)


@myWeb.route("/services")
def services():
	return render_template("services.html")
	

@myWeb.route("/signin")
def signin():
	form = signinForm()
	if request.method == "POST":
		if form.validate_on_submit():
			username = form.Username.data
			password = form.Password.data
			form = contactForm(formdata=None)
	return render_template("signin.html",form=form)
	
@myWeb.route("/signup")
def signup():
	return render_template("signup.html")