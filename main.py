from flask import Flask
from route.routes import myWeb

app = Flask(__name__)
app.register_blueprint(myWeb)


if __name__ == "__main__":
	app.run(debug=True,port=5000)