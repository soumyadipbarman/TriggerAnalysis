from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config # getUsernameFromSiteDB

config = Configuration()

config.section_("General")
#config.General.requestName = 'ESV_Trigger_Run_v2_JetHT_Run2017F-31Mar2018-v1_12April_1'
#config.General.requestName = 'ESV_Trigger_Run_v2_JetHT_Run2017E-31Mar2018-v1_12April'
#config.General.requestName = 'ESV_Trigger_Run_v2_JetHT_Run2017D-31Mar2018-v1_12April'
#config.General.requestName = 'ESV_Trigger_Run_v2_JetHT_Run2017C-31Mar2018-v1_12April'
#config.General.requestName = 'ESV_Trigger_Run_v2_JetHT_Run2017B-31Mar2018-v1_12April'

config.General.requestName = 'Jet_Charge_JetHT_Run2017B-09Aug2019_UL2017-v1_21Dec'
#config.General.requestName = 'Jet_Charge_JetHT_Run2017C-09Aug2019_UL2017-v1_21Dec'
#config.General.requestName = 'Jet_Charge_JetHT_Run2017D-09Aug2019_UL2017-v1_21Dec'
#config.General.requestName = 'Jet_Charge_JetHT_Run2017E-09Aug2019_UL2017-v1_21Dec'
#config.General.requestName = 'Jet_Charge_JetHT_Run2017F-09Aug2019_UL2017-v1_21Dec'

config.General.workArea = 'crab_GJets'
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.allowUndistributedCMSSW = True
config.JobType.psetName = 'Run_QCD_test_106x_data_cfg.py'
#config.JobType.inputFiles= [
#"/afs/cern.ch/work/t/tsarkar/private/QCD-13/CMSSW_7_6_3/src/Test/QCDEventShape/test/Fall15_25nsV2_MC_PtResolution_AK4PFchs.txt", "/afs/cern.ch/work/t/tsarkar/private/QCD-13/CMSSW_7_6_3/src/Test/QCDEventShape/test/Fall15_25nsV2_MC_SF_AK4PFchs.txt", "/afs/cern.ch/work/t/tsarkar/private/QCD-13/CMSSW_7_6_3/src/Test/QCDEventShape/test/Fall15_25nsV2_DATA_UncertaintySources_AK4PF.txt"
#]
#config.Data.inputDataset = '/JetHT/Run2017B-17Nov2017-v1/MINIAOD'
#config.Data.inputDataset = '/JetHT/Run2017B-12Sep2017-v1/MINIAOD'
#config.Data.inputDataset = '/JetHT/Run2017C-17Nov2017-v1/MINIAOD'
#config.Data.inputDataset = '/JetHT/Run2017D-17Nov2017-v1/MINIAOD'
#config.Data.inputDataset = '/JetHT/Run2017E-17Nov2017-v1/MINIAOD'
#config.Data.inputDataset = '/JetHT/Run2017F-17Nov2017-v1/MINIAOD'

#config.Data.inputDataset = '/JetHT/Run2017F-31Mar2018-v1/MINIAOD'
#config.Data.inputDataset = '/JetHT/Run2017E-31Mar2018-v1/MINIAOD'
#config.Data.inputDataset = '/JetHT/Run2017D-31Mar2018-v1/MINIAOD'
#config.Data.inputDataset = '/JetHT/Run2017C-31Mar2018-v1/MINIAOD'
#config.Data.inputDataset = '/JetHT/Run2017B-31Mar2018-v1/MINIAOD'

#config.Data.inputDataset = '/JetHT/Run2015D-PromptReco-v4/MINIAOD'
#config.Data.inputDataset = '/JetHT/Run2015D-PromptReco-v3/MINIAOD'
#config.Data.inputDataset = '/JetHT/Run2015C_25ns-05Oct2015-v1/MINIAOD'
#config.Data.inputDataset = '/JetHT/Run2015D-16Dec2015-v1/MINIAOD'

config.section_("Data")
config.Data.inputDataset = '/JetHT/Run2017B-09Aug2019_UL2017-v1/MINIAOD'
#config.Data.inputDataset = '/JetHT/Run2017C-09Aug2019_UL2017-v1/MINIAOD'
#config.Data.inputDataset = '/JetHT/Run2017D-09Aug2019_UL2017-v1/MINIAOD'
#config.Data.inputDataset = '/JetHT/Run2017E-09Aug2019_UL2017-v1/MINIAOD'
#config.Data.inputDataset = '/JetHT/Run2017F-09Aug2019_UL2017-v1/MINIAOD'

config.Data.inputDBS = 'global'

#config.Data.splitting = 'Automatic'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 15
#config.Data.unitsPerJob = 200

config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/Legacy_2017/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt'

#config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt'
#config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt'
#config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/PromptReco/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt'
#config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/PromptReco/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt'
#config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/13TeV/Cert_246908-259891_13TeV_PromptReco_Collisions15_25ns_JSON_Silver.txt'
#config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/13TeV/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON.txt'
#config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2.txt'
#config.Data.lumiMask ='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/Reprocessing/Cert_13TeV_16Dec2015ReReco_Collisions15_25ns_JSON_v2.txt'

#config.Data.runRange = '246908-260627' # '193093-194075'
#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.outLFNDirBase = '/store/user/sobarman/JetCharge/Trigger/'
config.Data.publication = False
#config.Data.publishDataName = 'May2015_Data_analysis'

config.section_("Site")
config.Site.storageSite = 'T2_IN_TIFR'
