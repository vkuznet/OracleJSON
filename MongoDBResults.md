### When 1M Records were inserted in batches of 200k each into MongoDB

##### File Name : fwjr_prod.json, File Size : 5kB

| Record Count  | Time to Write to DB | Reading without Indexing "wmaid" | Reading with Indexing "wmaid"
| ------------- |:-------------:| -----:| -------: |
| 200k      | 48s 321ms | query : db.production.find({"wmaid":500}).explain() | query : db.production.find({"wmaid":500}).explain() |
| 400k      | 51s 916ms     |   totalDocsExamined : 1000000 | totalDocsExamined : 1 |
| 600k      | 53s 35ms     |    executionTimeMillis : 2927 | executionTimeMillis : 11 |
| 800k      | 47s 566ms | inputstage : COLLSCAN | inputstage : IXSCAN |
| 1M        | 47s 583ms | . | . |

##### Total Time : 248s 421ms = 4m 8s 421ms

##### Time taken for individual inserts = 10m 54s 871ms

------------------------

##### File Name : main_doc.json, File Size : 12kB

| Record Count  | Time to Write to DB | Reading without Indexing "wmaid" | Reading with Indexing "wmaid"
| ------------- |:-------------:| -----:| -------: |
| 200k      | 1m 18s 313ms | query :  | query : |
| 400k      | 1m 19s 957ms     |   totalDocsExamined :  | totalDocsExamined :  |
| 600k      | 1m 23s 583ms     |    executionTimeMillis :  | executionTimeMillis :  |
| 800k      | 1m 17s 431ms | inputstage :  | inputstage :  |
| 1M        | 1m 15s 937ms | . | . |


