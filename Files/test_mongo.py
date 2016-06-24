#!/usr/bin/env python
from pymongo import MongoClient

import json

uri = 'mongodb://localhost:8230'
client = MongoClient(uri)
doc = json.load(open('fwjr_prod.json'))

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

# Assingment
# 1. download mongodb - DONE
# 2. load document to DB - DONE
# 3. run client and create 10 documents - DONE 
# 4. load 10 docs in DB - DONE
# 5. query DB
# 6. study MongoDB QL - DONE
