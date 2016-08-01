# Weekly Report

## Week 1 (20th June to 26th June)

* Downloaded MongoDB
* Understood the Python Client and ran certain functions
* Wrote a Python Script to open a JSON File and load it to MongoDB
* Randomized certain fields of the test document file (WMAID, LFNArray, PFNArray, BRANCH_HASH ...)
* Uploaded the above Randomized Documents to MongoDB (insert_many)
* Studied MongoDB's Query Language
* Read and worked out different types of queries on the data (OR, AND, REGEX, Greater Than, EXISTS, ELEM MATCH ...)
* Performed Indexing on a few fields and noticed the difference in the time to run queries

## Week 2 (27th June to 3rd July)

* Bulk Write for 1M Documents tested
* Single Test Performed on Read Query
* Tests conducted for
  * 1M records inserted in batches of 200k for file size 5kB
  * 1M records inserted in batches of 200k for file size 12kB
  * Look Up time for a query when that field was 
    * Indexed
    * Not Indexed
  * Indexed vs Non Indexed Queries Tested

## Week 3 (4th July to 10th July)

* Due to a major change in the code, the results from the tests were re-evaluated and the tables were updated again.
* Tests were carried out
  * Single vs Bulk Insert
  * Indexed vs Non Indexed
* It was seen that the time taken to input the 1M documents in MongoDB increased dramatically

#### Eariler
```
Total Time : 4m 8s 421ms
Time taken for individual inserts = 10m 54s 871ms
```

#### Now
```
Total Time : 11m 57s 151ms
Time taken for individual inserts = 17m 56s 501ms
```

#### - Need to see how can this time be reduced

* Identified errors in the code where the same JSON document was being created and the randomize function wasn't working correctly. 
* To solve the issue, learnt more about copy and deepcopy function in Python
* Added a To Do list and 2nd Week report

* Read more about psutil() library in Python to measure CPU/RAM Usage but I need to still work upon that by creating another script that will accept PID of the process it needs to monitor.

* Setup Oracle SQL Developer Tools
* Added TNS Names and got the connection to devdb12 working
* Inserted 1 JSON Document successfully
* Had issues with getting the tnsnames.ora file. Solved it by securely copying it from lxplus to a local folder. 
* Had issues with inserting a JSON as a string more than 4000 characters. Had to create a PL/SQL Procedure and declare a variable as CLOB and update that variable

## Week 4 (11th July to 17th July)

* Faced a lot of errors while installing cx_Oracle and finally managed to install it with the help of Kate
* Steps to install : [Github Gist Document link](https://gist.github.com/sartaj10/03936b3dc5f9d0499f93e06cc12eb52e)
* After installing cx_Oracle, in the process of creating a Python script to load documents into Oracle automatically
*

## Week 5 (18th July to 24th July)

*

## Week 6 (25th July to 31st July)

* Prepared a list of queries to be run in Oracle over the week

![](https://github.com/sartaj10/OracleJSON/blob/master/Screenshots/preparedQuery_1.png)

![](https://github.com/sartaj10/OracleJSON/blob/master/Screenshots/preparedQuery_2.png)

* Faced an error ORA 600 which is an internal error in Oracle stating that "No more data to be read from socket"

* To resolve that, asked for access to Oracle 12.2 (Beta) database and checked if I was getting the same issues in this version of the database or not

* **Conclusion** : No such error was observed in 12.2 and along with that, simplified notation worked properly with arrays

#### Count ID select
![Alt text](https://github.com/sartaj10/OracleJSON/blob/master/Screenshots/countID.png "count id")

#### WMAID Execution Plan
![Alt text](https://github.com/sartaj10/OracleJSON/blob/master/Screenshots/wmaid_explainPlan.png "wmaid execution plan")

## Week 7 (1st August to 7th August)



## Week 8 (8th August to 14th August)



## Week 9 (15th August to 19th August)

