# Create Table 

CREATE TABLE j_purchaseorder
   (id          RAW (16) NOT NULL,
    date_loaded TIMESTAMP (6) WITH TIME ZONE,
    po_document CLOB
    CONSTRAINT ensure_json CHECK (po_document IS JSON));

# Insert Statement but valid for string literals upto 4000 characters

INSERT INTO j_purchaseorder
  VALUES (
    SYS_GUID(),
    SYSTIMESTAMP,
    '{"PONumber"             : 1600,
      "Reference"            : "ABULL-20140421",
      "Requestor"            : "Alexis Bull",
      "User"                 : "ABULL",
      "CostCenter"           : "A50",
      "ShippingInstructions" : {"name"   : "Alexis Bull",
                                "Address": {"street"  : "200 Sporting Green",
                                            "city"    : "South San Francisco",
                                            "state"   : "CA",
                                            "zipCode" : 99236,
                                            "country" : "United States of America"},
                                "Phone" : [{"type" : "Office", "number" : "909-555-7307"},
                                           {"type" : "Mobile", "number" : "415-555-1234"}]},
      "Special Instructions" : null,
      "AllowPartialShipment" : true,
      "LineItems"            : [{"ItemNumber" : 1,
                                 "Part"       : {"Description" : "One Magic Christmas",
                                                 "UnitPrice"   : 19.95,
                                                 "UPCCode"     : 13131092899},
                                 "Quantity"   : 9.0},
                                {"ItemNumber" : 2,
                                 "Part"       : {"Description" : "Lethal Weapon",
                                                 "UnitPrice"   : 19.95,
                                                 "UPCCode"     : 85391628927},
                                 "Quantity"   : 5.0}]}'
          );

# Insert using Declaring a variable

DECLARE 
  DOC2 varchar2(32767);
BEGIN
  DOC2 := '{
    "LFNArray": [
        "/store/unmerged/logs/prod/2016/6/22/jen_a_ACDC_task_BTV-RunIISpring16DR80-00021__v1_T_160620_220004_4878/BTV-RunIISpring16DR80-00021_1/10010/0/3b11f8ea-3792-11e6-900f-001e67abefa8-748-0-logArchive.tar.gz",
        "/store/unmerged/RunIISpring16DR80/QCD_Pt_170to250_bcToE_TuneCUETP8M1_13TeV_pythia8/DQMIO/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/710010/1AC95D11-4C38-E611-A806-0025905A6104.root",
        "/store/unmerged/RunIISpring16DR80/QCD_Pt_170to250_bcToE_TuneCUETP8M1_13TeV_pythia8/GEN-SIM-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/10003/9ED12B93-2E33-E611-85AE-003048D25BA6.root",
        "/store/unmerged/RunIISpring16DR80/QCD_Pt_170to250_bcToE_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/710010/BC705011-4C38-E611-A806-0025905A6104.root"
    ],
    "LFNArrayRef": [
        "fallbackFiles",
        "outputLFNs",
        "lfn",
        "skippedFiles",
        "inputLFNs"
    ],
    "PFNArray": [
        "root://cmsdcadisk01.fnal.gov//dcache/uscmsdisk/store/unmerged/RunIISpring16DR80/QCD_Pt_170to250_bcToE_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/710010/BC705011-4C38-E611-A806-0025905A6104.root",
        "root://cmsdcadisk01.fnal.gov//dcache/uscmsdisk/store/unmerged/RunIISpring16DR80/QCD_Pt_170to250_bcToE_TuneCUETP8M1_13TeV_pythia8/DQMIO/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/710010/1AC95D11-4C38-E611-A806-0025905A6104.root",
        "root://cmsxrootd-site.fnal.gov//store/unmerged/RunIISpring16DR80/QCD_Pt_170to250_bcToE_TuneCUETP8M1_13TeV_pythia8/GEN-SIM-RAW/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/10003/9ED12B93-2E33-E611-85AE-003048D25BA6.root"
    ],
    "PFNArrayRef": [
        "inputPFNs",
        "outputPFNs",
        "pfn"
    ],
    "fallbackFiles": [],
    "meta_data": {
        "agent_ver": "1.0.14.patch3",
        "fwjr_id": "4975595-0",
        "host": "vocms0310.cern.ch",
        "jobstate": "success",
        "jobtype": "Processing",
        "ts": 1466585035
    },
    "skippedFiles": [],
    "steps": [
        {
            "analysis": {},
            "cleanup": {},
            "errors": [],
            "input": [],
            "logs": {},
            "name": "stageOut1",
            "output": [],
            "performance": {
                "cp": {},
                "memory": {},
                "multicore": {},
                "storage": {}
            },
            "site": "T1_US_FNAL_Disk",
            "start": 1466584802,
            "status": 0,
            "stop": 1466584805
        },
        {
            "analysis": {},
            "cleanup": {},
            "errors": [],
            "input": [],
            "logs": {},
            "name": "logArch1",
            "output": [
                {
                    "adler32": "ec27d92f",
                    "cksum": "1166227312",
                    "events": 0,
                    "inputLFNs": [],
                    "inputPFNs": [],
                    "merged": false,
                    "module_label": "logArchive",
                    "outputLFNs": [
                        0
                    ],
                    "outputPFNs": [],
                    "runs": [],
                    "size": 0
                }
            ],
            "performance": {
                "cp": {},
                "memory": {},
                "multicore": {},
                "storage": {}
            },
            "site": "T1_US_FNAL_Disk",
            "start": 1466584805,
            "status": 0,
            "stop": 1466584808
        },
        {
            "analysis": {},
            "cleanup": {},
            "errors": [],
            "input": [
                {
                    "catalog": "",
                    "events": 376,
                    "guid": "9ED12B93-2E33-E611-85AE-003048D25BA6",
                    "input_source_class": "PoolSource",
                    "input_type": "primaryFiles",
                    "lfn": 2,
                    "module_label": "source",
                    "pfn": 2,
                    "runs": [
                        {
                            "lumis": [
                                50067,
                                50068
                            ],
                            "runNumber": 1
                        }
                    ]
                }
            ],
            "logs": {},
            "name": "cmsRun1",
            "output": [
                {
                    "StageOutCommand": "stageout-xrdcp-fnal",
                    "acquisitionEra": "RunIISpring16DR80",
                    "adler32": "ca385b20",
                    "applicationName": "cmsRun",
                    "applicationVersion": "CMSSW_8_0_3_patch2",
                    "branch_hash": "e07ad8b6ceaf76a6d6cdb63efb51c301",
                    "catalog": "",
                    "cksum": "1237646870",
                    "configURL": "https://cmsweb.cern.ch/couchdb;;reqmgr_config_cache;;0a90d2e0d1f9bd415382cf9365675d40",
                    "events": 376,
                    "globalTag": "80X_mcRun2_asymptotic_2016_v3",
                    "guid": "BC705011-4C38-E611-A806-0025905A6104",
                    "inputLFNs": [
                        2
                    ],
                    "inputPFNs": [
                        2
                    ],
                    "merged": false,
                    "module_label": "AODSIMoutput",
                    "ouput_module_class": "PoolOutputModule",
                    "outputDataset": "/QCD_Pt_170to250_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISpring16DR80-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/AODSIM",
                    "outputLFNs": [
                        3
                    ],
                    "outputPFNs": [
                        0
                    ],
                    "prep_id": "BTV-RunIISpring16DR80-00021",
                    "processingStr": "PUSpring16_80X_mcRun2_asymptotic_2016_v3",
                    "processingVer": 3,
                    "runs": [
                        {
                            "lumis": [
                                50067,
                                50068
                            ],
                            "runNumber": 1
                        }
                    ],
                    "size": 97337631,
                    "validStatus": "PRODUCTION"
                },
                {
                    "StageOutCommand": "stageout-xrdcp-fnal",
                    "acquisitionEra": "RunIISpring16DR80",
                    "adler32": "30f47935",
                    "applicationName": "cmsRun",
                    "applicationVersion": "CMSSW_8_0_3_patch2",
                    "branch_hash": "d41d8cd98f00b204e9800998ecf8427e",
                    "catalog": "",
                    "cksum": "1257252450",
                    "configURL": "https://cmsweb.cern.ch/couchdb;;reqmgr_config_cache;;0a90d2e0d1f9bd415382cf9365675d40",
                    "events": 0,
                    "globalTag": "80X_mcRun2_asymptotic_2016_v3",
                    "guid": "1AC95D11-4C38-E611-A806-0025905A6104",
                    "inputLFNs": [
                        2
                    ],
                    "inputPFNs": [
                        2
                    ],
                    "merged": false,
                    "module_label": "DQMoutput",
                    "ouput_module_class": "DQMRootOutputModule",
                    "outputDataset": "/QCD_Pt_170to250_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISpring16DR80-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3/DQMIO",
                    "outputLFNs": [
                        1
                    ],
                    "outputPFNs": [
                        1
                    ],
                    "prep_id": "BTV-RunIISpring16DR80-00021",
                    "processingStr": "PUSpring16_80X_mcRun2_asymptotic_2016_v3",
                    "processingVer": 3,
                    "runs": [
                        {
                            "lumis": [
                                50067,
                                50068
                            ],
                            "runNumber": 1
                        }
                    ],
                    "size": 2017769,
                    "validStatus": "PRODUCTION"
                }
            ],
            "performance": {
                "cp": {
                    "AvgEventTime": 9.77535,
                    "EventThroughput": 0.0995888,
                    "MaxEventTime": 38.4722,
                    "MinEventTime": 2.45711,
                    "TotalJobCP": 3704.66,
                    "TotalJobTime": 3793.72,
                    "TotalLoopCP": 3687.17
                },
                "memory": {
                    "PeakValueRss": 1464.2,
                    "PeakValueVsize": 2086.71
                },
                "multicore": {},
                "storage": {
                    "readAveragekB": 5593.4638592,
                    "readCachePercentageOps": 0,
                    "readMBSec": 0.0297415265043,
                    "readMaxMSec": 1927.03,
                    "readNumOps": 18,
                    "readPercentageOps": 2.22222222222,
                    "readTotalMB": 218.494682,
                    "readTotalSecs": 0,
                    "writeTotalMB": 92.8285,
                    "writeTotalSecs": 1726030
                }
            },
            "site": "T1_US_FNAL_Disk",
            "start": 1466580879,
            "status": 0,
            "stop": 1466584802
        }
    ],
    "stype": "avroio",
    "task": "/jen_a_ACDC_task_BTV-RunIISpring16DR80-00021__v1_T_160620_220004_4878/BTV-RunIISpring16DR80-00021_1",
    "wmaid": "053eda099bee7fdc3e63fab9304e2f85",
    "wmats": 1466585168.408134
}';
  INSERT INTO testDocument VALUES(SYS_GUID(), SYSTIMESTAMP, DOC2);
END;

