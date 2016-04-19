# OracleJSON
CMS summer openlab project to test JSON support in Oracle DB

## Project description
Based on CMS FWJR data structure (commonly used by various CMS DMWM tools)
a candidate should perform the following tasks:

1. create ORACLE DB schema
2. insert JSON documents into ORACLE DB
3. measure injection rate, both CPU/RAM metrics, single vs bulk insert
4. perform random document update and measure time for update in-place
5. index size for different fields, e.g. string (LFNs), numeric (CPU)
6. index size on nested structures vs flatten structures which will require to perform tasks #1-3 for both structures
7. use and report on ORACLE Query Language for querying JSON docs. It would be nice to look at
  - query composition, constrains, look-up within arrays, arrays of dicts, etc.
  - query aggregation
  - compare performance between MongoDB QL and ORACLE one

Examples of JSON we deal with:

```
# general JSON structure
{key: {k0:v,
       k1:{key1:v1,
           key2:v2,
           key3:{key:v}},
       k2:[{key1:v}, {key2:v}]
      }
}
```

```
# CMS FWJR data structure
{"meta_data": {"agent_ver": "1.0.14.pre5",
               "fwjr_id": "1-0",
               "host": "a.b.com",
               "jobtype": "Processing",
               "jobstate": "success",
               "ts": 1456500229},
 "LFNArray": ["/store/file1.root",
              "/store/file2.root",
              "/lfn/fallbackfile.root", "/lfn/skipedfile.root"],
 "LFNArrayRef": ["fallbackFiles",
                 "outputLFNs",
                 "lfn",
                 "skippedFiles",
                 "inputLFNs"],
 "PFNArray": ["root://file1.root",
              "root://file2.root",
              ],
 "PFNArrayRef": ["inputPFNs", "outputPFNs", "pfn"],  # list of keys whose value is referencing fileArray index

 "steps": [{"name": "cmsRun1",
             "analysis": {},
             "cleanup": {},
             "logs": {},
             "errors": [
                   {
                       "details": "An exception",
                       "type": "Fatal Exception",
                       "exitCode": 8001
                   }
               ],
             "input": [{"catalog": "",
                        "events": 6893,
                        "guid": "E8099605-8853-E011-A848-0030487A18F2",
                        "input_source_class": "PoolSource",
                        "input_type": "primaryFiles",
                        "lfn": 0,
                        "module_label": "source",
                        "pfn": 0,
                        "runs": [{"lumis": [164, 165],
                                  "runNumber": 160960}]}],
             "output": [{"StageOutCommand": "rfcp-CERN",
                         "acquisitionEra": "CMSSW_7_0_0_pre11",
                         "adler32": "e503b8b9",
                         "applicationName": "cmsRun",
                         "applicationVersion": "CMSSW_7_0_0_pre11",
                         "async_dest": "",
                         "branch_hash": "c1e135af4ac2eb2b803bb6487be2c80f",
                         "catalog": "",
                         "cksum": "2641269665",
                         "configURL": "https://hostname/couchdb",
                         "events": 0,
                         "globalTag": "GR_R_62_V3::All",
                         "guid": "ECCFE421-08CB-E511-9F4C-02163E017804",
                         "inputDataset": "/Cosmics/Run2011A-v1/RAW",
                         "inputLFNs": [0],
                         "inputPFNs": [0],
                         "location": "",
                         "merged": False,
                         "module_label": "ALCARECOStreamDtCalib",
                         "ouput_module_class": "PoolOutputModule",
                         "outputDataset": "/Cosmics/CMSSW_7_0_0/ALCARECO",
                         "outputLFNs": [1],
                         "outputPFNs": [1],
                         "prep_id": "",
                         "processingStr": "RECOCOSD_TaskChain_Data_pile_up_test",
                         "processingVer": 1,
                         "runs": [{"lumis": [164, 165],
                                   "runNumber": 160960}],
                         "size": 647376,
                         "user_dn": "",
                         "user_vogroup": "DEFAULT",
                         "user_vorole": "DEFAULT",
                         "validStatus": "PRODUCTION",
                         "SEName": "srm-cms.cern.ch",
                         "PNN": "T2_CERN_CH",
                         "GUID": "",
                         "StageOutCommand": "srmv2-lcg"}],
              "performance": {
                  "storage": {
                    "readAveragekB": 77.8474891246,
                    "readCachePercentageOps": 0.0,
                    "readMBSec": 0.0438598972596,
                    "readMaxMSec": 4832.84,
                    "readNumOps": 97620.0,
                    "readPercentageOps": 1.00032780168,
                    "readTotalMB": 7423.792,
                    "readTotalSecs": 0.0,
                    "writeTotalMB": 357.624,
                    "writeTotalSecs": 575158.0},
                    "memory": {
                       "PeakValueRss": 0.0,
                       "PeakValueVsize": 0.0
                    },
                   "cpu": {
                       "TotalJobCPU": 0.39894,
                       "AvgEventCPU": -2.0, # for ("-nan")
                       "MaxEventCPU": 0.0,
                       "AvgEventTime": -1.0, # for ("inf")
                       "MinEventCPU": 0.0,
                       "TotalEventCPU": 0.0,
                       "TotalJobTime": 26.4577,
                       "MinEventTime": 0.0,
                       "MaxEventTime": 0.0
                   }},
              "site": "T2_CH_CERN",
              "start": 1454569735,
              "status": 0,
              "stop": 1454569736}
            ],
"fallbackFiles": [0],
"skippedFiles": [1],
"task": "/Task/RECOCOSD"}
```

## References:
Oracle JSON support
https://docs.oracle.com/database/121/ADXDB/json.htm#ADXDB6251

JSON data in the database is textual, but the text can be stored using data
type BLOB, as well as VARCHAR2 or CLOB. When possible, Oracle recommends that
you use BLOB storage. In particular, doing so obviates the need for any
character-set conversion.

MongoDB QL: https://docs.mongodb.org/manual/tutorial/query-documents/
