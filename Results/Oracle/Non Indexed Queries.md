## Query : Find Records Based on provided LFN Pattern

SELECT M.* 
  FROM test3 p,
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
WHERE lfn = '/store/mc/Run5/file0.root';

### Execution Time : 17m 44s

## Query : Find Records for provided run number

SELECT M.* 
  FROM test3 p,
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
 
### Execution Time : 13m 4s

## Get sum/average/max values

SELECT SUM(M.totalMB) totalMB_sum,
       MAX(M.totalCP) totalCP_max,
       AVG(M.avgEventTime) eventTime_avg,
       MAX(M.peakValueRss) Rss_max
  FROM test3 p,
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

### Execution Time : 12m 46s

## Find Specific wmaid

SELECT test.doc.wmaid FROM testDocument test where test.doc.wmaid = 'kBYyPWEYxev7kuv23frTlG2eqvELodfI';

Execution Time : 11m 6s

## Greater Than Operator

SELECT t.doc.steps.performance 
  FROM test3 t 
    WHERE json_exists(
                      t.doc, 
                      '$.steps.performance.storage[*]?(@.writeTotalMB > $v)' 
                      passing 390 as "v"
                      );

## Starts with Operator / PFN Array Regex

SELECT t.doc.LFNArray , t.doc.PFNArray
  FROM test3 t 
    WHERE json_exists(
                      t.doc, 
                      '$?(@.PFNArray starts with $str)' 
                      passing 'root://test.ch/Run1' as "str"
                      );

### Execution Time : 14m 7s

## Starts with Operator / LFN Array Regex

SELECT t.doc.PFNArray 
  FROM test3 t 
    WHERE json_exists(
                      t.doc, 
                      '$?(@.LFNArray starts with $str)' 
                      passing '/store/mc/Run1' as "str"
                      );

### Execution Time : 13m 26s

## Starts with Operator OR

SELECT t.doc.LFNArray, t.doc.PFNArray 
  FROM test3 t 
    WHERE json_exists(
                      t.doc, 
                      '$?(@.LFNArray starts with "/store/mc/Run1" || 
                      	  @.PFNArray starts with "root://test.ch/Run4")' 
                      );

### Execution Time : 15m 33s

## Find Records based on provided conditions (<= / >=)

SELECT test.doc.steps.performance.storage.writeTotalMB 
  FROM test3 test 
    WHERE json_exists(test.doc, 
                      '$.steps.performance.storage?(@.writeTotalMB > 390 
                      								&& @.writeTotalMB < 400)' 
    				 );

### Execution Time : 17m 26s