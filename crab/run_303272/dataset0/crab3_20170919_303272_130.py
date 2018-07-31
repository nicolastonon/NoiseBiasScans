from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'NoiseScan_20170919_run303272_v1_130'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'computeNoiseFromRaw_cfg_130.py'
config.JobType.outputFiles = ['SiStripCommissioningSource.root']
config.JobType.scriptExe = 'scriptExe.sh'
config.JobType.maxMemoryMB = 3000

config.Data.inputDataset = '/VRRandom0/Run2017D-v1/RAW' #second dataset
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 500 #Change to optimize file size
#config.Data.lumiMask = 'NoiseScan_20170919_run303272_JSON.txt'
config.Data.runRange = '303272,303314'
config.Data.outLFNDirBase = '/store/group/dpg_tracker_strip/comm_tracker/Strip/RadMonitoring/NoiseBiasScan/2017/dataset0'
config.Data.publication = False
#config.Data.outputDatasetTag = ''


#Else, runs where the data are located (may be busy)
config.Data.ignoreLocality = True

#config.Site.storageSite = 'T2_FR_IPHC'
config.Site.storageSite = 'T2_CH_CERN'
