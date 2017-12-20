import FWCore.ParameterSet.Config as cms

process = cms.Process("Source")

#process.load("DQM.SiStripCommon.MessageLogger_cfi")

process.load("DQM.SiStripCommon.DaqMonitorROOTBackEnd_cfi")

process.load('Configuration.Geometry.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data')


process.SiStripDetInfoFileReader = cms.Service("SiStripDetInfoFileReader")

process.sistripconn = cms.ESProducer("SiStripConnectivity")

process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring('/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/02DA6AA0-A49E-E711-A533-02163E01A3C8.root'),
  eventsToProcess = cms.untracked.VEventRange('303272:61762-303272:81449')
)
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(500) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.load("EventFilter.SiStripRawToDigi.FedChannelDigis_cfi")
process.FedChannelDigis.LegacyUnpacker    = cms.bool(False)
process.FedChannelDigis.UnpackBadChannels = cms.bool(True)
process.FedChannelDigis.DoAPVEmulatorCheck = cms.bool(False)

process.load("DQM.SiStripCommissioningSources.CommissioningHistos_cfi")
process.CommissioningHistos.CommissioningTask = 'PEDESTALS'  # <-- run type taken from event data, but can be overriden

process.p = cms.Path(process.FedChannelDigis*process.CommissioningHistos)

