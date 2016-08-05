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

| db.production.aggregate([
                    { "$unwind" : "$steps"},
                    { "$group" : { "_id": None, 
                                   "sum_totalMB": { "$sum" : "$steps.performance.storage.writeTotalMB"},
                                   "max_cp": { "$max" : "$steps.performance.cp.TotalJobCP" },
                                   "avg_eventTime": { "$avg" : "$steps.performance.cp.AvgEventTime"},
                                   "max_valueRss" : { "$max" : "$steps.performance.memory.PeakValueRss"} 
                                 } 
                    }
                ],
                {
                    explain : True
                });  | Y | 83697 |  |  |  |
| db.production.aggregate([
                    { "$unwind" : "$steps"},
                    { "$group" : { "_id": None, 
                                   "sum_totalMB": { "$sum" : "$steps.performance.storage.writeTotalMB"},
                                   "max_cp": { "$max" : "$steps.performance.cp.TotalJobCP" },
                                   "avg_eventTime": { "$avg" : "$steps.performance.cp.AvgEventTime"},
                                   "max_valueRss" : { "$max" : "$steps.performance.memory.PeakValueRss"} 
                                 } 
                    }
                ],
                {
                    explain : True
                });  | N | 79532 |  |  |  |


| db.production.find({'PFNArray':{'$regex':'^root://test.ch/Run214/'}}).explain("executionStats")  | Y | 6587 | 1 | 1000000 | 3000000 |
| db.production.find({'PFNArray':{'$regex':'^root://test.ch/Run214/'}}).explain("executionStats")  | N | 24067 | 1  | 1000001  | 0 |

| db.production.find({"LFNArray":{"$regex":"^/store/mc/Run727/"}}).explain() | Y | 6 | 1 | 1 | 5 |
| db.production.find({"LFNArray":{"$regex":"^/store/mc/Run727/"}}).explain() | N | 13221  | 1  | 1000001  | 0 |

| db.production.find({"$or":[{"PFNArray": { "$regex" : "^root://test.ch/Run430/"} }, { "LFNArray": { "$regex" : "^/store/mc/Run121/"} }]}).explain("executionStats")  | Y | 16511 | 2 | 1000002 | 3000005 |
| db.production.find({"$or":[{"PFNArray": { "$regex" : "^root://test.ch/Run430/"} }, { "LFNArray": { "$regex" : "^/store/mc/Run121/"} }]}).explain("executionStats")  | N | 11702 | 2 | 1000001  | 0 |

| db.production.find({"steps.performance.storage.writeTotalMB": {"$gte":200,"$lte":250}}).explain() | Y | 34204 | 578293 | 1000000 | 2999860 |
| db.production.find({"steps.performance.storage.writeTotalMB": {"$gte":200,"$lte":250}}).explain() | N | 12083 | 578293  | 1000001  | 0  |
