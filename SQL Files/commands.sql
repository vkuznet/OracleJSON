# Find Records Based on provided LFN Pattern
# unique index

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

select M.*
  from testDocument p,
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
  where writeTotalMB > 350;


select t.doc.steps.performance 
  from testDocument t 
    where json_exists(
                      t.doc, 
                      '$.steps.performance.storage[*]?(@.writeTotalMB > $v)' 
                      passing 350 as "v"
                      );


# Find Records for provided run number
# index

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
# index

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

------------

create index write_total_mb
  on testDocument (test.doc.steps.performance.storage.writeTotalMB);
  
explain plan for select t.doc.steps.performance 
  from testDocument t 
    where json_exists(
                      t.doc, 
                      '$.steps.performance.storage[*]?(@.writeTotalMB > $v)' 
                      passing 350 as "v"
                      );

select * from table(dbms_xplan.display);

select index_name from user_indexes;

drop index write_total_mb;

create bitmap index write_total_mb 
  on testDocument (json_exists(doc, '$.steps.performance.storage.writeTotalMB'));
  
explain plan for select t.doc.steps.performance 
  from testDocument t 
    where json_exists(
                      t.doc, 
                      '$.steps.performance.storage[*]?(@.writeTotalMB > $v)' 
                      passing 350 as "v"
                      );

select * from table(dbms_xplan.display);

select json_query(doc, '$.steps.performance.storage.writeTotalMB' with wrapper) from testDocument test;

create index MB on testDocument (json_query(doc, '$.steps.performance.storage.writeTotalMB' with wrapper));

explain plan for select M.*
  from testDocument p,
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
  where writeTotalMB > 350;


