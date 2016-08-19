#!/usr/bin/env Python
# encoding=utf8
import json
import random
import string
import pymongo
import copy
import psutil
import os
import gather_data
import time
from pymongo import MongoClient
from pprint import pprint
from datetime import datetime

def init():
    client = MongoClient()
    db = client.code
    doc = loadJSON() 

    # To insert documents in Bulk in parts of 4
        # loadOne(db, doc)    
        # for i in range(4):
        #     bulkInsert(db, doc, i)

    # To insert documents row-by-row
        # loadOne(db, doc)
        # loadMultipleFiles(db, doc)

    # createIndex(db)
    
    # Query the database
    query(db)

    # To delete the entire collection
    # deleteCollection(db)

def bulkInsert(db, doc, index):
    bulk = db.production.initialize_ordered_bulk_op()

    begin_time = datetime.now()
    
    for idx in range(250000):
        newdoc = randomizeDoc(doc, idx, index)
        bulk.insert(newdoc)

    result = bulk.execute()

    end_time = datetime.now()
    difference = end_time - begin_time
    print str(begin_time) + " " + str(end_time) + "\n" + str(difference)    

def createIndex(db):
    print db.production.create_index([("steps.performance.storage", pymongo.ASCENDING)])

def deleteCollection(db):
    cursor = db.production.drop()

def get_random_string(length):
    return "".join([random.choice(string.ascii_letters + string.digits) for n in xrange(length)])  

def loadJSON():
    with open('../json/main_doc.json') as data_file:
        doc = json.load(data_file)
    return doc

def loadOne(db, doc):
    cursor = db.production.insert(doc)
    print cursor

def loadMultipleFiles(db, doc):
    begin_time = datetime.now()
    x = 1000000

    for idx in range(x):
        newdoc = randomizeDoc(doc, idx, 0)
        db.production.insert(newdoc)

    end_time = datetime.now()
    difference = end_time - begin_time
    
    print str(begin_time) + " " + str(end_time) + "\n" + str(difference)    

def query(db):
    cursor = db.production.find({'PFNArray':'root://test.ch/Run123/file0.root'})
    
    cursor = db.production.find({'steps.output.runs.runNumber':2})
    
    cursor = db.production.find({'steps.site':'T2_US_FNAL_Disk'})
    
    cursor = db.production.aggregate([
                    { "$unwind" : "$steps"},
                    { "$group" : { "_id": None, 
                                   "sum_totalMB": { "$sum" : "$steps.performance.storage.writeTotalMB"},
                                   "max_cp": { "$max" : "$steps.performance.cp.TotalJobCP" },
                                   "avg_eventTime": { "$avg" : "$steps.performance.cp.AvgEventTime"},
                                   "max_valueRss" : { "$max" : "$steps.performance.memory.PeakValueRss"} 
                                 } 
                    }
                ])
    
    cursor = db.production.find({'wmaid':'88JEntUcP6G5rbCGudEO7rakfWjfg5rg'})
    
    cursor = db.production.find({'PFNArray':{'$regex':'^root://test.ch/Run214'}})
    
    cursor = db.production.find({'LFNArray':{'$regex':'^/store/mc/Run727'}})
    
    cursor = db.production.find({"$or":[
                                            {"PFNArray": { "$regex" : "^root://test.ch/Run430/"} }, 
                                            {"LFNArray": { "$regex" : "^/store/mc/Run121/"} }
                                        ]
                                })
    
    cursor = db.production.find({'steps.performance.storage.writeTotalMB':{'$gte': 200, '$lte': 250}})
    
    for d in cursor:
        print d

# Using main_doc.json and randomizing various fields of the JSON document 
def randomizeDoc(doc, idx, index):
    newdoc = copy.deepcopy(doc)
    del newdoc['_id']

    newdoc['wmaid'] = get_random_string(32)

    for i in range(len(newdoc['steps'])):
        storage_key = newdoc['steps'][i]['performance']['storage']

        storage_key['writeTotalMB'] = round(random.uniform(200,400), 2)
        storage_key["readPercentageOps"] = random.uniform(1, 2)
        storage_key["readMBSec"] = random.uniform(0,1)

        steps_key = newdoc['steps'][i]
        
        steps_key['site'] = 'T' + str(random.randint(1,5)) + '_US_FNAL_Disk'
        output_length = len(steps_key['output'])

        if output_length > 0:
            for j in range(output_length):    
                output_key = newdoc['steps'][i]['output'][j]
                output_key['outputDataset'] = '/Cosmics/Run-' + get_random_string(5)
                output_key['branch_hash'] = get_random_string(32)

                run_length = len(output_key["runs"])
                
                if run_length > 0:
                    for k in range(run_length):
                        run_key = newdoc['steps'][i]['output'][j]['runs'][k]
                        run_key['runNumber'] = random.randint(1,19)

    # Ranging from [0-250000], [250001-500000] etc
    run_number = str(250000*index + idx)

    LFN_length = len(newdoc['LFNArray'])
    
    for i in range(LFN_length):
        newdoc['LFNArray'][i] = "/store/mc/Run"+ run_number + "/file"+ str(i)+ ".root"

    PFN_length = len(newdoc['PFNArray'])

    for i in range(PFN_length):
        newdoc['PFNArray'][i] = "root://test.ch/Run"+ run_number + "/file"+ str(i)+ ".root"

    return newdoc

if __name__ == "__main__":
    init()
