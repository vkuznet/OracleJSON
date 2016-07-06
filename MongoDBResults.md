### When 1M Records were inserted in batches of 200k each into MongoDB

##### 1. File Name : fwjr_prod.json, File Size : 5kB

| Record Count  | Time to Write to DB | Reading without Indexing "wmaid" | Reading with Indexing "wmaid"
| ------------- |:-------------:| -----:| -------: |
| 200k      | 48s 321ms | query : db.production.find({"wmaid":500}).explain() | query : db.production.find({"wmaid":500}).explain() |
| 400k      | 51s 916ms     |   totalDocsExamined : 1000000 | totalDocsExamined : 1 |
| 600k      | 53s 35ms     |    executionTimeMillis : 2927 | executionTimeMillis : 11 |
| 800k      | 47s 566ms | inputstage : COLLSCAN | inputstage : IXSCAN |
| 1M        | 47s 583ms | . | . |

##### Total Time : 4m 8s 421ms

##### Time taken for individual inserts = 10m 54s 871ms

------------------------

##### 2. File Name : main_doc.json, File Size : 12kB

| Record Count  | Time to Write to DB | Reading without Indexing "wmaid" | Reading with Indexing "wmaid"
| ------------- |:-------------:| -----:| -------: |
| 200k      | 1m 18s 313ms | query : db.production.find({"wmaid":0KxWiRqzJs09CvewtsbJaKFqwpRWNuxy}).explain()| query : |
| 400k      | 1m 19s 957ms     | totalDocsExamined : 1158003 | totalDocsExamined : 1 |
| 600k      | 1m 23s 583ms     | executionTimeMillis : 5730 | executionTimeMillis : 2 |
| 800k      | 1m 17s 431ms | inputstage : COLLSCAN | inputstage : FETCH |
| 1M        | 1m 15s 937ms | nReturned : 1 | nReturned : 1 |

##### Total Time : 6m 35s 221ms

##### Time Taken for individual inserts = 12m 0s 014ms


### Index Vs Non Index Queries

##### File Name : main_doc.json, File Size : 12kB

| Query | Indexed (Y/N) | Execution Time (Millis)  | Number of Results returned | Total Docs Examined | Total Keys Examined
| ----- :| -------------:| --------------:| ---------- :| ------------- :| -----------:|
| db.production.find({'PFNArray':{'$regex':'^root://test.ch/Run214/'}}).explain("executionStats")  | Y | executionTimeMillis : 19601 | nReturned: 3 | totalDocsExamined: 1158000 |totalKeysExamined: 3474000 |

| db.production.find({"LFNArray":{"$regex":"^/store/mc/Run727/"}}).explain() | Y | executionTimeMillis: 6 | nReturned : 3 | totalDocsExamined: 3 | totalKeysExamined : 13 |

| db.production.find({"$or":[{"PFNArray": { "$regex" : "^root://test.ch/Run430/"} }, { "LFNArray": { "$regex" : "^/store/mc/Run121/"} }]}).explain("executionStats")  | Y | executionTimeMillis : 27715 | nReturned': 6 | totalDocsExamined: 1158006 | totalKeysExamined': 3474013 |

| db.production.find({"steps.performance.storage.writeTotalMB": {"$gte":200,"$lte":250}}).explain() | Y | executionTimeMillis : 115977 | nReturned: 669535 | totalDocsExamined : 1158000 | totalKeysExamined: 3473800 |
