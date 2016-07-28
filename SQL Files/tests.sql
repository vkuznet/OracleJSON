1. SQL> SELECT json_query(doc, '$.PFNArray') FROM testDocument FETCH FIRST 5 ROWS ONLY

JSON_QUERY(DOC,'$.PFNARRAY')
--------------------------------------------------------------------------------
["root://test.ch/Run396/file0.root","root://test.ch/Run396/file1.root","root://t
est.ch/Run396/file2.root"]

["root://test.ch/Run397/file0.root","root://test.ch/Run397/file1.root","root://t
est.ch/Run397/file2.root"]

["root://test.ch/Run398/file0.root","root://test.ch/Run398/file1.root","root://t
est.ch/Run398/file2.root"]

["root://test.ch/Run399/file0.root","root://test.ch/Run399/file1.root","root://t
est.ch/Run399/file2.root"]

JSON_QUERY(DOC,'$.PFNARRAY')
--------------------------------------------------------------------------------

["root://test.ch/Run400/file0.root","root://test.ch/Run400/file1.root","root://t
est.ch/Run400/file2.root"]


2. SQL> SELECT json_query(doc, '$.PFNArray[0]') FROM testDocument FETCH FIRST 5 ROWS ONLY

JSON_QUERY(DOC,'$.PFNARRAY[0]')
--------------------------------------------------------------------------------


3. SQL> SELECT json_query(doc, '$.PFNArray[0]' WITH WRAPPER) FROM testDocument FETCH FIRST 5 ROWS ONLY;

JSON_QUERY(DOC,'$.PFNARRAY[0]'WITHWRAPPER)
--------------------------------------------------------------------------------
["root://test.ch/Run396/file0.root"]
["root://test.ch/Run397/file0.root"]
["root://test.ch/Run398/file0.root"]
["root://test.ch/Run399/file0.root"]
["root://test.ch/Run400/file0.root"]


4. SQL> SELECT * FROM testDocument test WHERE json_query(doc, '$.PFNArray[0]' WITH WRAPPER) = 'root://test.ch/Run396/file0.root';

no rows selected


5. SQL> SELECT json_query(doc, '$.PFNArray[0]' WITH WRAPPER) FROM testDocument test WHERE json_query(doc, '$.PFNArray' WITH WRAPPER) = '["root://test.ch/Run396/file0.root"]';

JSON_QUERY(DOC,'$.PFNARRAY[0]'WITHWRAPPER)
--------------------------------------------------------------------------------
["root://test.ch/Run396/file0.root"]


6. SELECT count(*) FROM testDocument WHERE json_textcontains(doc, '$.PFNArray[0]', 'root://test.ch/Run396/file0.root')
*
ERROR at line 1:
ORA-40469: JSON path expression in JSON_TEXTCONTAINS() is invalid

(JSON_TEXTCONTAINS does not support array_step)


7. SQL> SELECT * FROM testDocument test WHERE json_query(doc, '$.PFNArray[0]') = 'root://test.ch/Run396/file0.root';

no rows selected


8. SQL> SELECT test.doc.PFNArray FROM testDocument test FETCH FIRST 5 ROWS ONLY;

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

9. SQL> SELECT test.doc.PFNArray[0] FROM testDocument test FETCH FIRST 5 ROWS ONLY;
SELECT test.doc.PFNArray[0] FROM testDocument test FETCH FIRST 5 ROWS ONLY
                        *
ERROR at line 1:
ORA-00923: FROM keyword not found where expected

10. SQL> SELECT test.doc.PFNArray.[0] FROM testDocument test FETCH FIRST 5 ROWS ONLY;
SELECT test.doc.PFNArray.[0] FROM testDocument test FETCH FIRST 5 ROWS ONLY
                         *
ERROR at line 1:
ORA-01747: invalid user.table.column, table.column, or column specification



11. SQL> SELECT test.doc.PFNArray.0 FROM testDocument test FETCH FIRST 5 ROWS ONLY;
SELECT test.doc.PFNArray.0 FROM testDocument test FETCH FIRST 5 ROWS ONLY
                        *
ERROR at line 1:
ORA-00923: FROM keyword not found where expected


----------------------------------------------------

SELECT test.doc.wmaid from testDocument test fetch first 5 rows only;

SELECT json_query(doc, '$.LFNArray') from testDocument test where json_value(doc, '$.wmaid') = 'SC4RaGTH2zqqX8sTR5ovQrkiD5cYvBFl';

select test.doc.LFNArray from test3 test;

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
            site varchar2(2000 char) path '$'
          )
        )
      ) M
WHERE site = '/store/unmerged/logs/prod/2016/6/22/jen_a_ACDC_task_BTV-RunIISpring16DR80-00021__v1_T_160620_220004_4878/BTV-RunIISpring16DR80-00021_1/10010/0/3b11f8ea-3792-11e6-900f-001e67abefa8-748-0-logArchive.tar.gz';

select json_query(doc, '$.steps.output.runs.runNumber' with wrapper) from test3 test where json_exists(doc, '$.steps.output.runs.runNumber');

SELECT t.*
  FROM test3 test,
       json_table(
        test.doc,
        '$.main[*]'
        columns (
          steps varchar2(2000) format json with wrapper path '$.steps[*]',
          nested path '$.steps[*]'
          columns (
            output integer path '$.output',
            nested path '$.site[*]'
            columns ( 
              abc number(10) path '$'
            )
          )
        )
      ) t 
  WHERE abc = 1;
  
insert into test3 values('{ "main" : 
                                    [ { 
                                        "steps" : [ 
                                                    {"site":[1,2,4], "output":9},
                                                    {"site":[5,6,7], "output":12} 
                                                  ]                                     
                                      },
                                      {
                                        "steps" : [
                                                    {"site":[8,9,10], "output":15}
                                                  ]
                                      }
                                    ]
                            }');


insert into test3 values('{"steps":[{"site":[1,2,4],"output":9},{"site":[5,6,7], "output":12},{"site":[8,9,10], "output":15}]}');

truncate table test3;

select test.doc.LFNArray from testDocument test fetch first 5 rows only;

select count(*) from test3;

---------------------------------------
