### Index Vs Non Index Queries

##### File Name : main_doc.json, File Size : 12kB

| Query  | Indexed (Y/N) | Execution Time (Millis)  | Number of Results returned | Total Docs Examined | Total Keys Examined
| -----  |:-------------:| ------------------------:| -------------------------: | ------------------: | ------------------: |
| db.production.find({'PFNArray':'root://test.ch/Run123/file0.root'}).explain("executionStats")  | Y | 0 | 1 | 1 | 1 |
| db.production.find({'PFNArray':'root://test.ch/Run123/file0.root'}).explain("executionStats")  | N | 15663 | 1  | 1000001  | 0 |
| db.production.find({'steps.output.runs.runNumber':2}).explain("executionStats")  | Y | 9429 | 103146 | 103146 | 103146 |
| db.production.find({'steps.output.runs.runNumber':2}).explain("executionStats")  | N | 30103 | 103146  | 1000001  | 0 |
| db.production.find({'steps.site':'T2_US_FNAL_Disk'}).explain("executionStats")  | Y | 10160 | 487629 | 487629 | 487629 |
| db.production.find({'steps.site':'T2_US_FNAL_Disk'}).explain("executionStats")  | N | 15527 | 487629 | 1000001 | 0 |
| db.production.aggregate(<br> [ {"$unwind" : "$steps"}, <br> { "$group" : <br> &nbsp;&nbsp;&nbsp;&nbsp;{ "_id": None, <br> &nbsp;&nbsp;&nbsp;&nbsp; "sum_totalMB": { "$sum" : "$steps.performance.storage.writeTotalMB"}, <br> &nbsp;&nbsp;&nbsp;&nbsp; "max_cp": { "$max" : "$steps.performance.cp.TotalJobCP" }, <br> &nbsp;&nbsp;&nbsp;&nbsp; "avg_eventTime": { "$avg" : "$steps.performance.cp.AvgEventTime"}, <br> &nbsp;&nbsp;&nbsp;&nbsp; "max_valueRss" : { "$max" : "$steps.performance.memory.PeakValueRss" } <br> } <br> } ], <br> { explain : True }); | Y | 83697 |  |  |  |
| db.production.aggregate(<br> [ {"$unwind" : "$steps"}, <br> { "$group" : <br> &nbsp;&nbsp;&nbsp;&nbsp;{ "_id": None, <br> &nbsp;&nbsp;&nbsp;&nbsp; "sum_totalMB": { "$sum" : "$steps.performance.storage.writeTotalMB"}, <br> &nbsp;&nbsp;&nbsp;&nbsp; "max_cp": { "$max" : "$steps.performance.cp.TotalJobCP" }, <br> &nbsp;&nbsp;&nbsp;&nbsp; "avg_eventTime": { "$avg" : "$steps.performance.cp.AvgEventTime"}, <br> &nbsp;&nbsp;&nbsp;&nbsp; "max_valueRss" : { "$max" : "$steps.performance.memory.PeakValueRss" } <br> } <br> } ], <br> { explain : True }); | N | 79532 |  |  |  |
| db.production.find({'wmaid':'FjXHNvwzC8T8GiwZD3uxmXw7uZSSAKRB'}).explain("executionStats")  | Y | 18 | 1 | 1 | 1 |
| db.production.find({'wmaid':'FjXHNvwzC8T8GiwZD3uxmXw7uZSSAKRB'}).explain("executionStats")  | N | 19813 | 1 | 1000001 | 0 |
| db.production.find({'PFNArray':{'$regex':'^root://test.ch/Run214/'}}).explain("executionStats")  | Y | 6587 | 1 | 1000000 | 3000000 |
| db.production.find({'PFNArray':{'$regex':'^root://test.ch/Run214/'}}).explain("executionStats")  | N | 24067 | 1  | 1000001  | 0 |
| db.production.find({"LFNArray":{"$regex":"^/store/mc/Run727/"}}).explain("executionStats") | Y | 6 | 1 | 1 | 5 |
| db.production.find({"LFNArray":{"$regex":"^/store/mc/Run727/"}}).explain("executionStats") | N | 13221  | 1  | 1000001  | 0 |
| db.production.find(<br> { "$or": <br>&nbsp;&nbsp;&nbsp;&nbsp; [ {"PFNArray": { "$regex" : "^root://test.ch/Run430/"} }, <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; { "LFNArray": { "$regex" : "^/store/mc/Run121/"} } ] <br> }).explain("executionStats")  | Y | 16511 | 2 | 1000002 | 3000005 |
| db.production.find(<br> { "$or": <br>&nbsp;&nbsp;&nbsp;&nbsp; [ {"PFNArray": { "$regex" : "^root://test.ch/Run430/"} }, <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; { "LFNArray": { "$regex" : "^/store/mc/Run121/"} } ] <br> }).explain("executionStats")  | N | 11702 | 2 | 1000001  | 0 |
| db.production.find(<br> {"steps.performance.storage.writeTotalMB": <br>&nbsp;&nbsp;&nbsp;&nbsp; {"$gte":200,"$lte":250} <br> }).explain("executionStats") | Y | 34204 | 578293 | 1000000 | 2999860 |
| db.production.find({"steps.performance.storage.writeTotalMB": {"$gte":200,"$lte":250}}).explain("executionStats") | N | 12083 | 578293  | 1000001  | 0  |
