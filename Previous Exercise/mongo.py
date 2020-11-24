import os
import pymongo
#if os.path.exists("env.py"):
#    import env


MONGO_URI = "mongodb+srv://tomod24:Ludacris247@mybookdb.zflml.mongodb.net/books2review?retryWrites=true&w=majority"
DATABASE = "books2review"
COLLECTION = "books"



def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

coll.update_one({"title": "episode V"}, {"$set": {"title": "Episode V"}})

documents = coll.find()

for doc in documents:
    print(doc)