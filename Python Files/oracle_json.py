#!/usr/bin/env Python
import cx_Oracle
import json
import random
import time
import copy
import string
import login
from pprint import pprint
from datetime import datetime

def init():
    db, cursor = connect()
    doc = load_json()
    batch_insert(cursor, doc, db)
    # retrieve(cursor)
    closeConnection(cursor, db)

def batch_insert(cursor, doc, db):
    begin_time = datetime.now()
    cursor.prepare("INSERT INTO testDocument VALUES (SYS_GUID(), SYSTIMESTAMP, :1)") 

    for j in range(1):
        document = []
        for i in range(50):
            json_doc = generateJSON(doc, j, i)
            row = (json_doc,)
            document.append(row)
            # print i
        cursor.executemany(None, document)
        db.commit()

    end_time = datetime.now()
    difference = end_time - begin_time
    print str(begin_time) + " " + str(end_time) + "\n" + str(difference)

def closeConnection(cursor, db):
    print ("Closing Database connection")
    cursor.close()
    db.close()

def connect():
    username = login.get_credentials()['username']
    password = login.get_credentials()['password']
    dbname = login.get_credentials()['dbname']

    db = cx_Oracle.connect(username, password, dbname)
    cursor = db.cursor()
    return db, cursor

def generateJSON(doc, index, idx):
    newdoc = copy.deepcopy(doc)
    # del newdoc['_id']
    x = 250000

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

                runs = len(newdoc["steps"][i]["output"][j]["runs"])
                print runs

                if runs > 0:
                    for k in range(runs):
                        rand3 = random.randint(1,19)
                        newdoc["steps"][i]["output"][j]["runs"][k]["runNumber"] = rand3

    for i in range(len(newdoc["LFNArray"])):
        newdoc["LFNArray"][i] = "/store/mc/Run"+str(x*index +idx)+"/file"+str(i)+".root"

    for i in range(len(newdoc["PFNArray"])):
        newdoc["PFNArray"][i] = "root://test.ch/Run"+str(x*index +idx)+"/file"+str(i)+".root"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    return json.dumps(newdoc)

def load_json():
    with open('../JSON Files/main_doc.json') as data_file:
        doc = json.load(data_file)
    return doc

def retrieve(cursor):

    begin_time = datetime.now()
    cursor.arraysize = 10000;
    cursor.execute("SELECT test.doc.wmaid FROM testDocument test")
    result = cursor.fetchall()

    end_time = datetime.now()
    difference = end_time - begin_time
    print str(begin_time) + " " + str(end_time) + "\n" + str(difference)
    print len(result)

if __name__ == "__main__":
    init()