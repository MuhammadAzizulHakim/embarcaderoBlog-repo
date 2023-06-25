import pymongo

# Create a New Test Database
client = pymongo.MongoClient("localhost", 27017)
db = client.test
print(db.name)
print(db.my_collection)

# Insert New Data
db.my_collection.insert_one({"x": 10}).inserted_id
# Insert New Data
print(db.my_collection.insert_one({"x": 8}).inserted_id)
