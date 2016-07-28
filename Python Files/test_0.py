#!/usr/bin/env Python
import json
import random
import string
import pymongo
import copy
import psutil
import os
from pymongo import MongoClient
from pprint import pprint
from datetime import datetime

def init():
    client = MongoClient()
    db = client.code
    doc = loadJSON()

    process = psutil.Process(os.getpid())
    mem_usage, cpu_usage = measureUsage(process)
    print "Memory Usage is {}".format(mem_usage) + " CPU Usage is {}".format(cpu_usage)
 
    loadOne(db, doc)    

    # 1,000,000 documents / 5 = 200,000 documents
    for i in range(5):
        bulkInsert(db, doc, i)

    process = psutil.Process(os.getpid())
    mem_usage, cpu_usage = measureUsage(process)
    print "Memory Usage is {}".format(mem_usage) + " CPU Usage is {}".format(cpu_usage)
 
    # loadMultipleFiles(db, doc)
    # createIndex(db)
    # query(db)
    # deleteCollection(db)

def measureUsage(process):
    mem_usage = process.memory_info()[0] / float(2 ** 20) # In MiB aka Mebibyte
    cpu_usage = psutil.cpu_percent(interval=0.1)
    return mem_usage, cpu_usage

def randomizeDoc(doc, idx, index, x):
    newdoc = copy.deepcopy(doc)
    del newdoc['_id']
            
    rand3 = "".join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
    newdoc["wmaid"] = rand3

    for i in range(len(newdoc["steps"])):
        newdoc["steps"][i]["performance"]["storage"]["writeTotalMB"] = round(random.uniform(200, 400), 2)
        newdoc["steps"][i]["performance"]["storage"]["readPercentageOps"] = random.uniform(1, 2)
        newdoc["steps"][i]["performance"]["storage"]["readMBSec"] = random.random()

        length = len(newdoc["steps"][i]["output"])

        if length > 0:
            for j in range(length):    
                rand1 = "".join([random.choice(string.digits) for n in xrange(5)])
                rand2 = "".join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])

                newdoc["steps"][i]["output"][j]["outputDataset"] = "/Cosmics/Run-" + rand1
                newdoc["steps"][i]["output"][j]["branch_hash"] = rand2 

                runs = len(newdoc["steps"][j]["output"]["runs"])

                if runs > 0:
                    for k in range(runs):
                        rand3 = random.randint(1,19)
                        newdoc["steps"][i]["output"][j]["runs"][k]["runNumber"] = rand3

    for i in range(len(newdoc["LFNArray"])):
        newdoc["LFNArray"][i] = "/store/mc/Run"+str(x*index +idx)+"/file"+str(i)+".root"

    for i in range(len(newdoc["PFNArray"])):
        newdoc["PFNArray"][i] = "root://test.ch/Run"+str(x*index +idx)+"/file"+str(i)+".root"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    return newdoc

def bulkInsert(db, doc, index):
    bulk = db.production.initialize_ordered_bulk_op()
    x = 200000
    begin_time = datetime.now()
    
    for idx in range(x):
        newdoc = randomizeDoc(doc, idx, index, x)
        bulk.insert(newdoc)

    result = bulk.execute()
    end_time = datetime.now()
    difference = end_time - begin_time
    print str(begin_time) + " " + str(end_time) + "\n" + str(difference)    

def createIndex(db):
    print db.production.create_index([("steps.performance.storage", pymongo.ASCENDING)])

def loadJSON():
    with open('../JSON Files/main_doc.json') as data_file:
        doc = json.load(data_file)
    return doc

def loadOne(db, doc):
    cursor = db.production.insert(doc)
    print cursor

def loadMultipleFiles(db, doc):
    begin_time = datetime.now()
    x = 1000000

    for idx in range(x):
        newdoc = randomizeDoc(doc, idx, 1, 0)
        db.production.insert(newdoc)

    end_time = datetime.now()
    difference = end_time - begin_time
    
    print str(begin_time) + " " + str(end_time) + "\n" + str(difference)    
    print("Number of docs", db.production.find({}).count())

def deleteCollection(db):
    cursor = db.production.drop()

def query(db):
    
    # cursor = db.production.find({"wmaid":500}).explain()
    # cursor = db.production.find({'PFNArray':{'$regex':'^root://test.ch/Run214/'}}).explain() # All regex that starts with root:// ....
    # cursor = db.production.find({"$or":[{"PFNArray": { "$regex" : "^root://test.ch/Run430/"} }, { "LFNArray": { "$regex" : "^/store/mc/Run121/"} }]}).explain() # All regex that starts with /store/mc/Run ....
    # cursor = db.production.find({'steps.output.inputDataset':{'$regex':r'^/Cosmics/Run-'}}) # All regex that starts with /store/mc/Run ....
    # cursor = db.production.find({"$or":[{"PFNArray": { "$regex" : "^root://test.ch/Run430/"} }, { "LFNArray": { "$regex" : "^/store/mc/Run121/"} }]}).explain("executionStats")
    
    cursor = db.production.find({'PFNArray':{'$regex':'^root://test.ch/Run214/'}}).explain()

    # cursor = db.production.find({})

    # for document in cursor:
    #     print document

if __name__ == "__main__":
    init()
