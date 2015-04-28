#!/bin/python
# List Mongo Collection

from pymongo import MongoClient
import time

client = MongoClient('mongodb://localhost:27017/')
db = client['test']
collection = db['testcol01']

print collection.count()

mongo_documents = collection.find()

for this_document in mongo_documents:
    print this_document 


