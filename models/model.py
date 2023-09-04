import datetime
import uuid
from flask import session, flash
# from tools.security import verify_password_hash,generate_password_hash
from Databases.Database import Connection
from flask_login import UserMixin

class User(UserMixin):
	Database = Connection.connect()
	def __init__(self, username, email, password,phone,_id=None):
		self.username = username
		self.email = email
		self.password = password
		self.phone = phone
		self._id = uuid.uuid4().hex if _id is None else _id
	def is_authenticated(self):
		return True
	def is_active(self):
		return True
	def is_anonymous(self):
		return False
	def get_id(self):
		return self._id
		
	@classmethod
	def get_by_username(cls, username):
		data = cls.Database.find_one({"username": username})
		if data is not None:
			return cls(**data)
			
	@classmethod
	def get_by_email(cls, email):
		data = cls.Database.find_one({"email": email})
		if data is not None:
			return cls(**data)

	@classmethod
	def get_by_id(cls, _id):
		data = cls.Database.find_one({"_id": _id})
		if data is not None:
			return cls(**data)
			
	@staticmethod	
	def login_valid(email, password):
		verify_user = User.get_by_email(email) 
		if verify_user is not None:
			k = verify_user.password == password
			return [k,verify_user]
		return False

	@classmethod
	def register(cls, username, email, phone,password):
		user = cls.get_by_email(email)
		if user is None:
			new_user = cls( username=username,email=email,phone=phone,password=password)
			new_user.save_to_mongo()
			session["id"] = new_user._id
			return True
		else:
			return False
		
	def json(self):
		return {
            "username": self.username,
            "email": self.email,
            "_id": self._id,
            "password": self.password,
            "phone":self.phone
        }
        
	def save_to_mongo(self):
		self.Database.insert_one(self.json())