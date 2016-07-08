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
