from flask import Blueprint,render_template
myWeb  = Blueprint("myWebsite",__name__)

@myWeb.route("/")
def home():
	return render_template("index.html")
	
@myWeb.route("/contact")
def contact():
	return render_template("contact.html")