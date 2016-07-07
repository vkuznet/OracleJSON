### When 1M Records were inserted in batches of 200k each into MongoDB

##### 1. File Name : fwjr_prod.json, File Size : 5kB

| Record Count | Time to Write to DB
| -----------  |:-------------------:|
| 200k         | 2m 18s 889ms        | 
| 400k         | 2m 13s 664ms        | 
| 600k         | 2m 9s 407ms         |
| 800k         | 2m 14s 204ms        |
| 1M           | 3m 2s 987ms         |

##### Total Time : 11m 57s 151ms
##### Time taken for individual inserts = 17m 56s 501ms

| Query  | Indexed (Y/N) | Execution Time (Millis)  | Total Docs Examined | Total Keys Examined | Input Stage
| -----  |:-------------:| ------------------------:| -------------------------: | ------------------: | --------------: |
| db.production.find({"wmaid":""}).explain() | N | 13299 | 1000001 | 0 | COLLSCAN |
| db.production.find({"wmaid":""}).explain() | Y | 8x | 1 | 1 | IXSCAN |

------------------------

##### 2. File Name : main_doc.json, File Size : 12kB

| Record Count | Time to Write to DB
| -----------  |:-------------------:|
| 200k         | 4m 3s 477ms        | 
| 400k         | 4m 1s 736ms        | 
| 600k         | 4m 32s 460ms        |
| 800k         | 4m 27s 376ms        |
| 1M           | 4m 28s 13ms        |

| Query  | Indexed (Y/N) | Execution Time (Millis)  | Total Docs Examined | Total Keys Examined | Input Stage
| -----  |:-------------:| ------------------------:| -------------------------: | ---------------------: | ------------------: |
| db.production.find({"wmaid":""}).explain()  | N | 17467 | 1000001 | 0 | COLLSCAN |
| db.production.find({"wmaid":""}).explain()  | Y | 16 | 1 | 1 | IXSCAN   |

##### Total Time : 21m 33s 62ms
##### Time Taken for individual inserts = 42m 56s 923ms

### Index Vs Non Index Queries

##### File Name : main_doc.json, File Size : 12kB

| Query  | Indexed (Y/N) | Execution Time (Millis)  | Number of Results returned | Total Docs Examined | Total Keys Examined
| -----  |:-------------:| ------------------------:| -------------------------: | ------------------: | ------------------: |
| db.production.find({'PFNArray':{'$regex':'^root://test.ch/Run214/'}}).explain("executionStats")  | Y | 19601 | 3 | 1158000 | 3474000 |
| db.production.find({'PFNArray':{'$regex':'^root://test.ch/Run214/'}}).explain("executionStats")  | N |  |  |  |  |
| db.production.find({"LFNArray":{"$regex":"^/store/mc/Run727/"}}).explain() | Y | 6 | 3 | 3 | 13 |
| db.production.find({"LFNArray":{"$regex":"^/store/mc/Run727/"}}).explain() | N |  |  |  |  |
| db.production.find({"$or":[{"PFNArray": { "$regex" : "^root://test.ch/Run430/"} }, { "LFNArray": { "$regex" : "^/store/mc/Run121/"} }]}).explain("executionStats")  | Y | 27715 | 6 | 1158006 | 3474013 |
| db.production.find({"$or":[{"PFNArray": { "$regex" : "^root://test.ch/Run430/"} }, { "LFNArray": { "$regex" : "^/store/mc/Run121/"} }]}).explain("executionStats")  | N |  | |  |  |
| db.production.find({"steps.performance.storage.writeTotalMB": {"$gte":200,"$lte":250}}).explain() | Y | 115977 | 669535 | 1158000 | 3473800 |
| db.production.find({"steps.performance.storage.writeTotalMB": {"$gte":200,"$lte":250}}).explain() | N |  |  |  |  |
