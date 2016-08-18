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
    # Change database username, password and dbname from login.py to connect
    db, cursor = connect()

    doc = load_json()
    batch_insert(cursor, doc, db)
    
    retrieve(cursor)
    closeConnection(cursor, db)

def batch_insert(cursor, doc, db):
    begin_time = datetime.now()
    cursor.prepare("INSERT INTO test11 VALUES (:1)") 

    for j in range(4):
        document = []
        for i in range(250000):
            json_doc = generateJSON(doc, j, i)
            row = (json_doc,)
            document.append(row)
            print i
        
        cursor.executemany(None, document)
        db.commit()

    print (datetime.now() - begin_time)

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

    run_number = str(250000*index + idx)
    LFN_length = len(newdoc['LFNArray'])
    
    for i in range(LFN_length):
        newdoc['LFNArray'][i] = "/store/mc/Run"+ run_number + "/file"+ str(i)+ ".root"

    PFN_length = len(newdoc['PFNArray'])

    for i in range(PFN_length):
        newdoc['PFNArray'][i] = "root://test.ch/Run"+ run_number + "/file"+ str(i)+ ".root"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    return json.dumps(newdoc)

def get_random_string(length):
    return "".join([random.choice(string.ascii_letters + string.digits) for n in xrange(length)])  

def load_json():
    with open('../json/main_doc.json') as data_file:
        doc = json.load(data_file)
    return doc

def retrieve(cursor):
    cursor.arraysize = 10000;
    cursor.execute("SELECT count(*) FROM test11")

    result = cursor.fetchall()
    for r in result:
        print r

if __name__ == "__main__":
    init()
