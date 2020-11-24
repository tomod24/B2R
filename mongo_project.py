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
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    option = input("Enter Option: ")
    return option


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            print("you have selected option 1")
        elif option == "2":
            print("you have selected option 1")
        elif option == "3":
            print("you have selected option 1")
        elif option == "4":
            print("you have selected option 1")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")


"""we use the connection lines provided in mono.py file to run the request. Then call the loop e.g. main_loop"""

conn = mongo_connect(MONGO_URI)
coll = conn[DATABASE][COLLECTION]
main_loop()