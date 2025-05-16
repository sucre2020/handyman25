from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()


db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')

client = MongoClient(f"mongodb+srv://{db_username}:{db_password}@cluster0.yoczwia.mongodb.net/sangisang?retryWrites=true&w=majority&appName=Cluster0")
db = client['sangisang']

handymen_collection = db["handymen"]


# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
