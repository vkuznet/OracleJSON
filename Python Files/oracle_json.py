import cx_Oracle, json, random, time, copy, string
from pprint import pprint
from datetime import datetime

def init():
    db, cursor = connect()
    doc = loadJSON()

    begin_time = datetime.now()
    cursor.prepare("INSERT INTO testDocument VALUES (SYS_GUID(), SYSTIMESTAMP, :1)") 

    # When one loop was run for 500k documents at once, an error occurred
    # array size too large and thus, 2 loops were run
    for j in range(2):
        document = []
        for i in range(250000):
            json_doc = generateJSON(doc, j, i)
            row = (json_doc,)
            document.append(row)
            # print (str(cursor.rowcount) + " row(s) inserted")
            print i
        cursor.executemany(None, document)
        db.commit()

    end_time = datetime.now()
    difference = end_time - begin_time
    print str(begin_time) + " " + str(end_time) + "\n" + str(difference)

    # retrieve(cursor)
    closeConnection(cursor, db)

def connect():
    username, password, dbname = getLoginDetails()
    db = cx_Oracle.connect(username, password, dbname)
    cursor = db.cursor()
    return db, cursor

def getLoginDetails():
    username = 'sbaveja'
    password = ''
    dbname = 'devdb12'
    return username, password, dbname

def loadJSON():
    with open('../JSON Files/main_doc.json') as data_file:
        doc = json.load(data_file)
    return doc

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

    for i in range(len(newdoc["LFNArray"])):
        newdoc["LFNArray"][i] = "/store/mc/Run"+str(x*index +idx)+"/file"+str(i)+".root"

    for i in range(len(newdoc["PFNArray"])):
        newdoc["PFNArray"][i] = "root://test.ch/Run"+str(x*index +idx)+"/file"+str(i)+".root"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    return json.dumps(newdoc)

def insert(cursor, json_doc):
    clob_value = cursor.var(cx_Oracle.CLOB)
    clob_value.setvalue(0, json_doc)
    cursor.setinputsizes(input = cx_Oracle.CLOB) # Predefine memory 
    cursor.execute(None, input=clob_value)

def retrieve(cursor):
    cursor.execute("SELECT test.doc.wmaid FROM testDocument test")
    result = cursor.fetchall()
    for r in result:
        print r

def closeConnection(cursor, db):
    print ("Closing Database connection")
    cursor.close()
    db.close()

if __name__ == "__main__":
    init()
