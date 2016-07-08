### When 1M Records were inserted in batches of 200k each into MongoDB

##### 1. File Name : fwjr_prod.json, File Size : 5kB

| Record Count | Time to Write to DB
| -----------  |:-------------------:|
| 200k         | 48s 321ms           | 
| 400k         | 51s 916ms           | 
| 600k         | 53s 35ms            |
| 800k         | 47s 566ms           |
| 1M           | 47s 583ms           |

| Query  | Indexed (Y/N) | Execution Time (Millis)  | Total Docs Examined | Input Stage
| -----  |:-------------:| ------------------------:| -------------------------: | ------------------: |
| db.production.find({"wmaid":500}).explain()  | N | 2927 | 1000000 | COLLSCAN |
| db.production.find({"wmaid":500}).explain() | Y | 11 | 1 | IXSCAN |


##### Total Time : 4m 8s 421ms
##### Time taken for individual inserts = 10m 54s 871ms

------------------------

##### 2. File Name : main_doc.json, File Size : 12kB

| Record Count | Time to Write to DB
| -----------  |:-------------------:|
| 200k         | 1m 18s 313ms        | 
| 400k         | 1m 19s 957ms        | 
| 600k         | 1m 23s 583ms        |
| 800k         | 1m 17s 431ms        |
| 1M           | 1m 15s 937ms        |

| Query  | Indexed (Y/N) | Execution Time (Millis)  | Total Docs Examined | Input Stage
| -----  |:-------------:| ------------------------:| -------------------------: | ------------------: |
| db.production.find({"wmaid":500}).explain()  | N | 5730 | 1158003 | COLLSCAN |
| db.production.find({"wmaid":500}).explain()  | Y | 2    | 1       | IXSCAN   |

##### Total Time : 6m 35s 221ms
##### Time Taken for individual inserts = 12m 0s 014ms
