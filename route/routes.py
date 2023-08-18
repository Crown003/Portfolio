from flask import Blueprint,render_template
myWeb  = Blueprint("myWebsite",__name__)

@myWeb.route("/")
def home():
	data = {
		"WebDevlopment":
			{
				"firstWeb":
				{
					"Title" : "My First Website",
					"mainImg": './images/firstWeb.jpg',
					"techUsedImg":[],
					"link":[]
				},
				"thisPortfolio":
				{
					"Title" :"This Portfoli Website",
					"mainImg":'./images/newProtfolio.jpg',
					"techUsedImg":[],
					"link":[],
				}		
			},
		"SoftwareDevlopment":
			{
				"Test data":
				{
					"Title" : "My First Website",
					"mainImg": './images/firstWeb.jpg',
					"techUsedImg":[],
					"link":[]
				}
				
			},
		"DataScience & AI":
			{
				"Test data":
				{
					"Title" : "My First Website",
					"mainImg": './images/firstWeb.jpg',
					"techUsedImg":[],
					"link":[]
				}
				
			},
	}
	return render_template("index.html",data=data)
	
@myWeb.route("/contact")
def contact():
	return render_template("contact.html")