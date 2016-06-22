#!/usr/bin/env Python
import json, random, string
from pymongo import MongoClient

client = MongoClient()
db = client.code

with open('fwjr_prod.json') as data_file:
    doc = json.load(data_file)

cursor = db.production.insert(doc)

for idx in range(3):
    newdoc = dict(doc)
    del newdoc["_id"]
    newdoc["wmaid"] = idx

    newdoc["steps"][0]["performance"]["storage"]["writeTotalMB"] = round(random.uniform(200, 400), 2)
    newdoc["steps"][0]["performance"]["storage"]["readPercentageOps"] = random.uniform(1, 2)
    newdoc["steps"][0]["performance"]["storage"]["readMBSec"] = random.random()

    rand1 = "".join([random.choice(string.ascii_letters + string.digits) for n in xrange(5)])
    rand2 = "".join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])

    newdoc["steps"][0]["output"][0]["inputDataset"] = "/Cosmics/Run-" + rand1
    newdoc["steps"][0]["output"][0]["branch_hash"] = rand2

    for i in range(len(newdoc["LFNArray"])):
        newdoc["LFNArray"][i] = "/store/mc/Run"+str(idx)+"/file"+str(i)+".root"

    for i in range(len(newdoc["PFNArray"])):
        newdoc["PFNArray"][i] = "root://test.ch/Run"+str(idx)+"/file"+str(i)+".root"

    db.production.insert(newdoc)

print("Number of docs", db.production.count())

# cursor = db.production.drop()
