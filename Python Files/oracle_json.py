import cx_Oracle, json, random, time, copy, string
from pprint import pprint

def init():
    db, cursor = connect()
    doc = loadJSON()

    cursor.prepare("INSERT INTO testDocument VALUES (SYS_GUID(), SYSTIMESTAMP, :input)")

    for i in range(10):
        clob_value = cursor.var(cx_Oracle.CLOB)
        clob_value.setvalue(0, generateJSON(doc))

        cursor.setinputsizes(input = cx_Oracle.CLOB) # Predefine memory 
        cursor.execute(None, input=clob_value)

        db.commit()
        print (str(cursor.rowcount) + " row(s) inserted")

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

def generateJSON(doc):
    newdoc = copy.deepcopy(doc)
    # del newdoc['_id']

    x = 1
    index = 0

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
        newdoc["LFNArray"][i] = "/store/mc/Run"+str(x*index +i)+"/file"+str(i)+".root"

    for i in range(len(newdoc["PFNArray"])):
        newdoc["PFNArray"][i] = "root://test.ch/Run"+str(x*index +i)+"/file"+str(i)+".root"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    return json.dumps(newdoc)

def closeConnection(cursor, db):
    print ("Closing Database connection")
    cursor.close()
    db.close()

if __name__ == "__main__":
    init()
