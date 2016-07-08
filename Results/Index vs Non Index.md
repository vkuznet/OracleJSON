### Index Vs Non Index Queries

##### File Name : main_doc.json, File Size : 12kB

| Query  | Indexed (Y/N) | Execution Time (Millis)  | Number of Results returned | Total Docs Examined | Total Keys Examined
| -----  |:-------------:| ------------------------:| -------------------------: | ------------------: | ------------------: |
| db.production.find({'PFNArray':{'$regex':'^root://test.ch/Run214/'}}).explain("executionStats")  | Y | 6587 | 1 | 1000000 | 3000000 |
| db.production.find({'PFNArray':{'$regex':'^root://test.ch/Run214/'}}).explain("executionStats")  | N | 24067 | 1  | 1000001  | 0 |
| db.production.find({"LFNArray":{"$regex":"^/store/mc/Run727/"}}).explain() | Y | 6 | 1 | 1 | 5 |
| db.production.find({"LFNArray":{"$regex":"^/store/mc/Run727/"}}).explain() | N | 13221  | 1  | 1000001  | 0 |
| db.production.find({"$or":[{"PFNArray": { "$regex" : "^root://test.ch/Run430/"} }, { "LFNArray": { "$regex" : "^/store/mc/Run121/"} }]}).explain("executionStats")  | Y | 16511 | 2 | 1000002 | 3000005 |
| db.production.find({"$or":[{"PFNArray": { "$regex" : "^root://test.ch/Run430/"} }, { "LFNArray": { "$regex" : "^/store/mc/Run121/"} }]}).explain("executionStats")  | N | 11702 | 2 | 1000001  | 0 |
| db.production.find({"steps.performance.storage.writeTotalMB": {"$gte":200,"$lte":250}}).explain() | Y | 34204 | 578293 | 1000000 | 2999860 |
| db.production.find({"steps.performance.storage.writeTotalMB": {"$gte":200,"$lte":250}}).explain() | N | 12083 | 578293  | 1000001  | 0  |
