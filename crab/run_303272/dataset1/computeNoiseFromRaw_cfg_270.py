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
  fileNames = cms.untracked.vstring('/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/0063FD0C-E89D-E711-A592-02163E01350D.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/0281C3FE-E79D-E711-AEC1-02163E01A22C.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/02AE0107-E89D-E711-BF7B-02163E014410.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/0409D102-E89D-E711-8467-02163E01A4AE.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/042F9D0B-E89D-E711-B541-02163E014135.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/061AD9C7-E99D-E711-B7F0-02163E011F9C.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/06841703-E89D-E711-9B34-02163E019CB3.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/0E499008-E89D-E711-8D93-02163E01A1D6.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/149F1023-E29D-E711-9A60-02163E019DF8.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/1C40A4B8-E29D-E711-803B-02163E014208.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/1E6F0102-E89D-E711-9AB3-02163E01A34E.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/1EEBD50B-E89D-E711-AAF9-02163E01360E.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/26B5221A-E89D-E711-959C-02163E011EA7.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/26DDFE01-E89D-E711-86F1-02163E014704.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/26F29807-E89D-E711-94D8-02163E013722.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/2ECAE376-E99D-E711-9F5D-02163E01A6D8.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/2EE4E728-E29D-E711-B602-02163E011C77.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/3482293B-EA9D-E711-BF9B-02163E01446B.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/349BF8FF-E79D-E711-99E0-02163E01340C.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/38453728-E29D-E711-BD3D-02163E0142E2.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/38806108-E89D-E711-9866-02163E013731.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/4AC98BB5-E29D-E711-B459-02163E01A3E2.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/4C4A530B-E89D-E711-AFD7-02163E01A5E1.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/4E081601-E89D-E711-A28E-02163E01A682.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/50171BFF-E79D-E711-927D-02163E011B0A.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/52918905-E89D-E711-B030-02163E01A1D6.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/52C4C702-E89D-E711-8E1F-02163E01A2C7.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/56979CB6-E29D-E711-B3A6-02163E01350D.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/5E01110C-E89D-E711-AA05-02163E01420B.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/5E2D2701-E89D-E711-8058-02163E01A710.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/5E814DFF-E79D-E711-AE29-02163E019D97.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/5E83DA06-E89D-E711-9540-02163E011DE1.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/5EDF3C21-E29D-E711-867D-02163E01A3D2.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/643A4002-E89D-E711-B9E9-02163E01A3B0.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/6EA930FD-E79D-E711-A500-02163E019B36.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/705ECB05-E89D-E711-8011-02163E01360E.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/7E1F28FD-E79D-E711-ABBC-02163E019DE5.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/7E67CF08-E89D-E711-BB06-02163E0122DF.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/7EEE3903-E89D-E711-93CC-02163E01A2E4.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/808F4CB7-E29D-E711-A0D7-02163E011E02.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/84A55C0F-E89D-E711-A561-02163E0145C0.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/8A837BFD-E79D-E711-9159-02163E01A731.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/8AEF7F00-E89D-E711-B26D-02163E013422.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/8C02C613-E89D-E711-9D86-02163E013731.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/90122E0B-E89D-E711-A1B3-02163E0145C0.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/9055AF0A-E89D-E711-BC14-02163E014135.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/90E2BBBC-E29D-E711-9172-02163E012806.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/925E8902-E89D-E711-A36E-02163E012428.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/92E2D37E-E39D-E711-9BA9-02163E0120CA.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/98758C00-E89D-E711-9980-02163E01A626.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/9A4F5421-E29D-E711-A781-02163E01A63D.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/9CAEB4FF-E79D-E711-B7A1-02163E019CF4.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/A04BD3B8-E29D-E711-8C69-02163E011FC7.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/A4E7D100-E89D-E711-9B61-02163E014725.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/AAD20E14-E89D-E711-83AB-02163E012B44.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/B0BD9802-E89D-E711-9C5C-02163E011A68.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/B2861600-E89D-E711-81AC-02163E019B9A.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/B29A5A0C-E89D-E711-A45B-02163E011E20.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/B2E3CE03-E89D-E711-9EF3-02163E01A1F6.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/BA727903-E89D-E711-8BC9-02163E0128C3.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/C2BFF9EF-E99D-E711-986E-02163E01A34E.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/C87646FC-E79D-E711-A4AE-02163E01A507.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/CC6D3AB8-E29D-E711-813C-02163E013746.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/CCD82A02-E89D-E711-BB9C-02163E019CB3.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/CE2FD607-E89D-E711-A5FE-02163E012AD7.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/CE49BC0C-E89D-E711-8E2F-02163E01420B.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/CEF415A8-F79D-E711-A813-02163E012A4A.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/D652EFFF-E79D-E711-B969-02163E01A657.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/D6BFCAFD-E79D-E711-9B3F-02163E01A4B1.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/E0B8DA12-E89D-E711-B592-02163E012222.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/E405FAC0-E29D-E711-BD01-02163E0136E8.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/E872660B-E89D-E711-8337-02163E01A2C7.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/EE623C03-E89D-E711-B033-02163E011A68.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/EE6A6252-E89D-E711-B010-02163E012A4A.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/F0840200-E89D-E711-A559-02163E019B9A.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/314/00000/FE38305B-E39D-E711-B551-02163E012806.root'),
  eventsToProcess = cms.untracked.VEventRange('303314:151583-303314:170284')
)
#Dataset0 : '/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/02DA6AA0-A49E-E711-A533-02163E01A3C8.root'
#Dataset1 : '/store/data/Run2017D/VRRandom1/RAW/v1/000/303/261/00000/003371CD-619D-E711-89EB-02163E0146CD.root'


process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(500) )

process.load("EventFilter.SiStripRawToDigi.FedChannelDigis_cfi")
process.FedChannelDigis.LegacyUnpacker    = cms.bool(False)
process.FedChannelDigis.UnpackBadChannels = cms.bool(True)
process.FedChannelDigis.DoAPVEmulatorCheck = cms.bool(False)

process.load("DQM.SiStripCommissioningSources.CommissioningHistos_cfi")
process.CommissioningHistos.CommissioningTask = 'PEDESTALS'  # <-- run type taken from event data, but can be overriden

process.p = cms.Path(process.FedChannelDigis*process.CommissioningHistos)

