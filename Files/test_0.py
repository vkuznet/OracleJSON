#!/usr/bin/env Python
import json, random, string, pymongo
from pymongo import MongoClient
from pprint import pprint
from datetime import datetime

def init():
    client = MongoClient()
    db = client.code
    doc = loadJSON()

    # 1,000,000 documents / 5 = 200,000 documents
    for i in range(5):
        bulkInsert(db, doc, i)
    
    createIndex(db)
    query(db)

    # loadOne(db, doc)
    # deleteCollection(db)
    # loadMultipleFiles(db, doc)

def bulkInsert(db, doc, index):
    bulk = db.production.initialize_ordered_bulk_op()
    x = 200000

    begin_time = datetime.now()

    for idx in range(x):
        newdoc = dict(doc)
        # del newdoc["_id"]

        newdoc["wmaid"] = x*index + idx
        newdoc["steps"][0]["performance"]["storage"]["writeTotalMB"] = round(random.uniform(200, 400), 2)
        newdoc["steps"][0]["performance"]["storage"]["readPercentageOps"] = random.uniform(1, 2)
        newdoc["steps"][0]["performance"]["storage"]["readMBSec"] = random.random()

        rand1 = "".join([random.choice(string.digits) for n in xrange(10)])
        rand2 = "".join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])

        newdoc["steps"][0]["output"][0]["inputDataset"] = "/Cosmics/Run-" + rand1
        newdoc["steps"][0]["output"][0]["branch_hash"] = rand2

        for i in range(len(newdoc["LFNArray"])):
            newdoc["LFNArray"][i] = "/store/mc/Run"+str(idx)+"/file"+str(i)+".root"

        for i in range(len(newdoc["PFNArray"])):
            newdoc["PFNArray"][i] = "root://test.ch/Run"+str(idx)+"/file"+str(i)+".root"

        bulk.insert(newdoc)

    result = bulk.execute()
    end_time = datetime.now()

    difference = end_time - begin_time
    print str(begin_time) + " " + str(end_time) + "\n"
    print difference
    
def createIndex(db):
    print db.production.create_index([("wmaid", pymongo.ASCENDING)])

def loadJSON():
    with open('fwjr_prod.json') as data_file:
        doc = json.load(data_file)
    return doc

def loadOne(db, doc):
    cursor = db.production.insert(doc)
    print cursor

def loadMultipleFiles(db, doc):
    for idx in range():
        newdoc = dict(doc)
        del newdoc["_id"]

        newdoc["wmaid"] = idx
        newdoc["steps"][0]["performance"]["storage"]["writeTotalMB"] = round(random.uniform(200, 400), 2)
        newdoc["steps"][0]["performance"]["storage"]["readPercentageOps"] = random.uniform(1, 2)
        newdoc["steps"][0]["performance"]["storage"]["readMBSec"] = random.random()

        rand1 = "".join([random.choice(string.digits) for n in xrange(5)])
        rand2 = "".join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])

        newdoc["steps"][0]["output"][0]["inputDataset"] = "/Cosmics/Run-" + rand1
        newdoc["steps"][0]["output"][0]["branch_hash"] = rand2

        for i in range(len(newdoc["LFNArray"])):
            newdoc["LFNArray"][i] = "/store/mc/Run"+str(idx)+"/file"+str(i)+".root"

        for i in range(len(newdoc["PFNArray"])):
            newdoc["PFNArray"][i] = "root://test.ch/Run"+str(idx)+"/file"+str(i)+".root"

        db.production.insert(newdoc)
    print("Number of docs", db.production.count())

def deleteCollection(db):
    cursor = db.production.drop()

def query(db):
    
    indexes = db.production.index_information()
    pprint(indexes)

    cursor = db.production.find({"wmaid":500}).explain()
    # cursor = db.production.find({'PFNArray':{'$regex':r'^root://test.ch/R'}}) # All regex that starts with root:// ....
    # cursor = db.production.find({'LFNArray':{'$regex':r'^/store/mc/Run'}}) # All regex that starts with /store/mc/Run ....
    # cursor = db.production.find({'steps.output.inputDataset':{'$regex':r'^/Cosmics/Run-'}}) # All regex that starts with /store/mc/Run ....

    # cursor = db.production.find({"$or":[
    #                                     {"wmaid": {"$gte":2}},
    #                                     {"steps.output.outputLFNs": 3}
    #                                 ]
    #                             })
    
    # cursor = db.production.find({"$or":[{"PFNArray":"/Run0/Test0/"},{"LFNArray":"/Run1/Test1/"}]})

    # for document in cursor:
    #     print document
    pprint(cursor)

if __name__ == "__main__":
    init()
