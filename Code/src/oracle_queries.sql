# Create Table 

CREATE TABLE testDocument
   (doc CLOB
    CONSTRAINT ensure_json CHECK (doc IS JSON));

# Insert using Declaring a variable

DECLARE 
  DOC2 CLOB;
BEGIN
  DOC2 := '{ }';
  INSERT INTO testDocument VALUES(DOC2);
END;

# To check allocated storage
SELECT * FROM user_ts_quotas;

# Find Records Based on provided LFN Pattern
SELECT M.* 
  FROM testDocument p, 
       json_table( 
        p.doc, 
        '$' 
        columns ( 
          wmaid varchar2(2000 char) path '$.wmaid',
          meta_data varchar2(2000 char) format json with wrapper path '$.meta_data',
          nested path '$.LFNArray[*]' 
          columns (  
            lfn varchar2(2000 char) path '$' 
          )
        ) 
      ) M 
WHERE lfn = '/store/mc/Run3212/file0.root';

# Comparison Query Operator
SELECT M.*
  FROM testDocument p,
      json_table(
        p.doc,
        '$'
        columns (
          nested path '$.steps.performance.storage[*]'
          columns (
            writeTotalMB number path '$.writeTotalMB'
            )
          )
      ) M
  WHERE writeTotalMB > 350;

# Comparison Query Operator 2
select t.doc.steps.performance 
  from testDocument t 
    where json_exists(
                      t.doc, 
                      '$.steps.performance.storage[*]?(@.writeTotalMB > $v)' 
                      passing 350 as "v"
                      );


# Find Records for provided run number

SELECT M.* 
  FROM testDocument p,
       json_table(
        p.doc,
        '$'
        columns (
          names varchar2(2000 char) format json with wrapper path '$.LFNArray',
          nested path '$.steps.output.runs[*]'
          columns ( 
            runNumber VARCHAR path '$.runNumber'
          )
        )
      ) M
  WHERE runNumber = 2;

# Get sum/average/max values

SELECT SUM(M.totalMB) totalMB_sum,
       MAX(M.totalCP) totalCP_max,
       AVG(M.avgEventTime) eventTime_avg,
       MAX(M.peakValueRss) Rss_max
  FROM testDocument p,
       json_table(
        p.doc,
        '$.steps.performance'
        columns (
          totalMB number path '$.storage.writeTotalMB',
          totalCP number path '$.cp.TotalJobCP',
          avgEventTime number path '$.cp.AvgEventTime',
          peakValueRss number path '$.memory.PeakValueRss'
        )
      ) M;

# Find Specific wmaid

# Before Indexing
# Average Time = 00:05:23.49
SELECT test.doc.wmaid FROM testDocument test WHERE test.doc.wmaid = '6EdJHilenQlpIDt5NQwIULsuuA0ABObE';

# Create Index
CREATE INDEX index_wmaid ON testDocument test (test.doc.wmaid);

# After Indexing
# Average Time = 00:00:00.03
SELECT test.doc.wmaid FROM testDocument test WHERE test.doc.wmaid = '6EdJHilenQlpIDt5NQwIULsuuA0ABObE';

# Greater Than Operator
select t.doc.steps.performance 
  from testDocument t 
    where json_exists(
                      t.doc, 
                      '$.steps.performance.storage[*]?(@.writeTotalMB > $v)' 
                      passing 350 as "v"
                      );

# Starts with Operator / PFN Array Regex
select t.doc.LFNArray , t.doc.PFNArray
  from testDocument t 
    where json_exists(
                      t.doc, 
                      '$?(@.PFNArray starts with $str)' 
                      passing 'root://test.ch/Run452' as "str"
                      );

# Starts with Operator / LFN Array Regex
select t.doc.PFNArray 
  from testDocument t 
    where json_exists(
                      t.doc, 
                      '$?(@.LFNArray starts with $str)' 
                      passing '/store/mc/Run214432' as "str"
                      );

# Starts with Operator OR
select t.doc.LFNArray, t.doc.PFNArray 
  from testDocument t 
    where json_exists(
                      t.doc, 
                      '$?(@.LFNArray starts with "/store/mc/Run1" || 
                      	  @.PFNArray starts with "root://test.ch/Run4")' 
                      );


# Find Records based on provided conditions (<= / >=)
select test.doc.steps.performance.storage.writeTotalMB 
  from testDocument test 
    where json_exists(test.doc, 
                      '$.steps.performance.storage?(@.writeTotalMB > 390 
                      								&& @.writeTotalMB < 400)' 
    				 );

# Select first 5 rows of PFNArray
SELECT json_query(doc, '$.PFNArray') FROM testDocument FETCH FIRST 5 ROWS ONLY

# Select a particular index of an array
# Result : NO OUTPUT
SELECT json_query(doc, '$.PFNArray[0]') FROM testDocument FETCH FIRST 5 ROWS ONLY

JSON_QUERY(DOC,'$.PFNARRAY[0]')
--------------------------------------------------------------------------------


# Run the same query with a "WITH WRAPPER" clause and results are obtained
SELECT json_query(doc, '$.PFNArray[0]' WITH WRAPPER) FROM testDocument FETCH FIRST 5 ROWS ONLY;

JSON_QUERY(DOC,'$.PFNARRAY[0]'WITHWRAPPER)
--------------------------------------------------------------------------------
["root://test.ch/Run396/file0.root"]
["root://test.ch/Run397/file0.root"]
["root://test.ch/Run398/file0.root"]
["root://test.ch/Run399/file0.root"]
["root://test.ch/Run400/file0.root"]


# WHERE clause without any result
SELECT * FROM testDocument test 
  WHERE json_query(doc, '$.PFNArray[0]' WITH WRAPPER) 
          = 'root://test.ch/Run396/file0.root';

no rows selected


# WHERE clause with a result
SELECT json_query(doc, '$.PFNArray[0]' WITH WRAPPER) FROM testDocument test 
  WHERE json_query(doc, '$.PFNArray' WITH WRAPPER) 
          = '["root://test.ch/Run396/file0.root"]';

JSON_QUERY(DOC,'$.PFNARRAY[0]'WITHWRAPPER)
--------------------------------------------------------------------------------
["root://test.ch/Run396/file0.root"]


# json_textcontains 
SELECT count(*) FROM testDocument WHERE json_textcontains(doc, '$.PFNArray[0]', 'root://test.ch/Run396/file0.root')

ERROR at line 1:
ORA-40469: JSON path expression in JSON_TEXTCONTAINS() is invalid

(JSON_TEXTCONTAINS does not support array_step)

# Simplified Dot Notation 
SELECT test.doc.PFNArray FROM testDocument test FETCH FIRST 5 ROWS ONLY;

PFNARRAY
--------------------------------------------------------------------------------
["root://test.ch/Run396/file0.root","root://test.ch/Run396/file1.root","root://t
est.ch/Run396/file2.root"]

["root://test.ch/Run397/file0.root","root://test.ch/Run397/file1.root","root://t
est.ch/Run397/file2.root"]

["root://test.ch/Run398/file0.root","root://test.ch/Run398/file1.root","root://t
est.ch/Run398/file2.root"]

["root://test.ch/Run399/file0.root","root://test.ch/Run399/file1.root","root://t
est.ch/Run399/file2.root"]

PFNARRAY
--------------------------------------------------------------------------------

["root://test.ch/Run400/file0.root","root://test.ch/Run400/file1.root","root://t
est.ch/Run400/file2.root"]

# Simplified Dot Notation for particular index of an array
SELECT test.doc.PFNArray[0] FROM testDocument test FETCH FIRST 5 ROWS ONLY;

SELECT test.doc.PFNArray[0] FROM testDocument test FETCH FIRST 5 ROWS ONLY
                        *
ERROR at line 1:
ORA-00923: FROM keyword not found where expected