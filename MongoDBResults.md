### WHEN 1M RECORDS WERE INSERTED IN BATCHES OF 200K EACH INTO MONGODB

| Record Count  | Time to Write to DB | Reading without Indexing "wmaid" | Reading with Indexing "wmaid"
| ------------- |:-------------:| -----:| -------: |
| 200k      | 48s 321ms | query : db.production.find({"wmaid":500}).explain() | query : db.production.find({"wmaid":500}).explain() |
| 400k      | 51s 916ms     |   totalDocsExamined : 1000000 | totalDocsExamined : 1 |
| 600k      | 53s 35ms     |    executionTimeMillis : 2927 | executionTimeMillis : 11 |
| 800k      | 47s 566ms | inputstage : COLLSCAN | inputstage : IXSCAN |
| 1M        | 47s 583ms | . | . |

#### Total Time : 248s 421ms = 4m 8s 421ms
#### Average File Size : 5kB

#### Time taken for individual inserts = 10m 54s 871ms
