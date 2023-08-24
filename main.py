from flask import Flask
from route.routes import myWeb
from dotenv import dotenv_values as env

app = Flask(__name__)
app.config["SECRET_KEY"] = env(".env")["SECRET_KEY"]
app.register_blueprint(myWeb)


if __name__ == "__main__":
	app.run(debug=True,port=5000)