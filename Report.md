# Weekly Report

## Week 1

* Downloaded MongoDB
* Understood the Python Client and ran certain functions
* Wrote a Python Script to open a JSON File and load it to MongoDB
* Randomized certain fields of the test document file (WMAID, LFNArray, PFNArray, BRANCH_HASH ...)
* Uploaded the above Randomized Documents to MongoDB (insert_many)
* Studied MongoDB's Query Language
* Read and worked out different types of queries on the data (OR, AND, REGEX, Greater Than, EXISTS, ELEM MATCH ...)
* Performed Indexing on a few fields and noticed the difference in the time to run queries

## Week 2

* Bulk Write for 1M Documents tested
* Single Test Performed on Read Query
* Tests conducted for
..* 1M records inserted in batches of 200k for file size 5kB
..* 1M records inserted in batches of 200k for file size 12kB
..* Look Up time for a query when that field was 
....* Indexed
....* Not Indexed
..* Indexed vs Non Indexed Queries Tested
