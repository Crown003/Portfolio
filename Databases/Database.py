from pymongo import MongoClient
from dotenv import dotenv_values as env
import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8'] 

class Connection:
	url =env(".env")["DATABASE_STRING"]
	@classmethod	
	def connect(cls):
		try:
			client = MongoClient(cls.url)
			db = client["MyWeb"]
			collection = db["users"]
			print("connected successfully !")
			return collection
		except Exception as e:
			print("unable to connect server.")
			print(e)
			
