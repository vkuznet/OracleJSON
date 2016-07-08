#!/usr/bin/env python
from pymongo import MongoClient

import json

# uri = 'mongodb://localhost:8230'
client = MongoClient()
doc = json.load(open('../JSON Files/fwjr_prod.json'))

coll = client['wma']['db']
coll.drop()
coll.insert(doc)

# for doc in coll.find():
#     print(doc)

for idx in range(10):
    ndoc = dict(doc)
    del ndoc['_id']
    ndoc['wmaid'] = idx
    print(ndoc['wmaid'])
    coll.insert(ndoc)

print("number of docs", coll.count())

spec = {'wmaid':1}

for doc in coll.find(spec):
    print(doc)