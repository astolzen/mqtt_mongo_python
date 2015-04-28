#!/bin/python
# Test Insert Data to Mongo

from pymongo import MongoClient
import time

client = MongoClient('mongodb://localhost:27017/')
db = client['test']
collection = db['testcol01']
post = {"date": time.strftime("%c"),
        "topic": "test-topic",
        "message": "test-message"}

post_id = collection.insert(post)

print post_id

