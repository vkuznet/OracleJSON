#!/usr/bin/env Python
import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.test
# cursor = db.restaurants.aggregate(
# 	[
# 		{"$group": {"_id": "$borough", "count": {"$sum":1}}}
# 	])

# Specify the group by key in the _id field i.e. borough in the above case

# print cursor.deleted_count # Number of results that matched the above criteria
# print cursor.modified_count # Number of results that were modified

# for document in cursor:
# 	print document

print db.restaurants.create_index([
									("cuisine", pymongo.ASCENDING),
									("address.zipcode", pymongo.DESCENDING)
								])

'''
creates a compound index on the "cuisine" field and the "address.zipcode" field. 
The index orders its entries first by ascending "cuisine" values, and then, 
within each "cuisine", by descending "address.zipcode" values.
'''



