from flask import Flask
from route.routes import myWeb
from dotenv import dotenv_values as env
from flask_login import LoginManager
from models.model import User

app = Flask(__name__)
app.config["SECRET_KEY"] = env(".env")["SECRET_KEY"]
app.register_blueprint(myWeb)

loginManager = LoginManager()
loginManager.init_app(app)

@loginManager.user_loader
def load_user(user_id):
	return User.get_by_id(user_id)
	

if __name__ == "__main__":
	app.run(debug=True,port=5000)