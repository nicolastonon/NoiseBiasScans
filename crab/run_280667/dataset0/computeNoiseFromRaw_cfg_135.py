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

#CHANGED -- use a list to have more than 255 args
list = ['/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/04ABEFF1-8E7A-E611-995E-02163E014384.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/0623B0EC-9F7A-E611-81EC-02163E011FA0.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/0A0C7BF6-A17A-E611-9CEE-02163E014165.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/0C3F7AEC-9F7A-E611-84AA-02163E0144E4.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/0C62CDEE-9F7A-E611-99AF-02163E0143EF.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/0CBE29F0-9F7A-E611-9B3A-02163E011C02.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/1435443E-9F7A-E611-A015-02163E014136.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/144C4E40-9F7A-E611-A094-02163E014789.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/1AD7CDDE-9F7A-E611-8221-FA163E69A996.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/220866EF-9F7A-E611-A918-FA163E2648F7.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/228C2EEE-9F7A-E611-AE1D-02163E011DFF.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/22E9ABEB-9F7A-E611-8C30-02163E0144A4.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/288362F4-9F7A-E611-8B52-02163E0143BC.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/2EB6D935-9F7A-E611-83E7-FA163E7F172A.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/328D6D44-9F7A-E611-83D3-02163E01467C.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/382975EF-9F7A-E611-B2A3-02163E014228.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/3EC4A7F3-9F7A-E611-85BB-FA163ECE34C0.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/40A0EAEB-9F7A-E611-870C-02163E01414A.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/44439FEA-9F7A-E611-9C85-02163E01424A.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/4453D93C-9F7A-E611-859F-02163E0137B2.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/447A70EC-9F7A-E611-9D68-02163E011C96.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/483325EE-9F7A-E611-868C-02163E0142B1.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/484ACFE6-9F7A-E611-A00D-FA163E56E23B.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/4C2129E9-9F7A-E611-8595-FA163EBCC08A.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/4C9B45EE-9F7A-E611-97D8-02163E013937.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/5820E7ED-9F7A-E611-A48A-02163E0133EE.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/58CBD83D-9F7A-E611-B700-02163E0137A2.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/5AD90A00-A57A-E611-8A11-02163E0142D6.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/648244F0-9F7A-E611-B69B-02163E014660.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/6A20CA6B-A07A-E611-9465-FA163E8973D0.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/72DC1238-9F7A-E611-B65B-FA163EB4B66F.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/7421E53C-9F7A-E611-9E0B-02163E014410.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/7450E6ED-9F7A-E611-AA63-02163E0137A4.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/76C374BA-8E7A-E611-9B0C-FA163E9E4DE4.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/78CACDEC-9F7A-E611-B5D7-02163E0137AA.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/7C5566F2-9F7A-E611-BA2C-02163E014596.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/82713AED-9F7A-E611-A831-02163E013422.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/82E787ED-9F7A-E611-AEE0-02163E0140E0.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/840F7FDB-9F7A-E611-A670-FA163EC389EB.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/8495725E-A37A-E611-817B-02163E0141BE.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/8A8293EE-9F7A-E611-B896-02163E014508.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/989257EE-9F7A-E611-A36D-02163E0142A0.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/9A0655F3-9F7A-E611-98FE-02163E01439E.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/9A1057EC-9F7A-E611-873A-02163E0128BC.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/ACC6EAEA-9F7A-E611-9E7D-02163E011EF6.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/AEF140E5-9F7A-E611-BBF8-FA163E8E3D2E.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/B02B7CEB-9F7A-E611-B7E4-02163E0142DE.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/B6C2C3ED-9F7A-E611-AE89-02163E011918.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/BC0955FB-9F7A-E611-AAC2-02163E0143BE.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/BE9DD7F6-9F7A-E611-8D9A-02163E014131.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/C41D2AD8-9F7A-E611-A065-FA163EE7ABB9.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/C69A963D-9F7A-E611-A0C8-02163E0143C5.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/D0B9BD3D-9F7A-E611-86A6-02163E0146B8.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/D26F56EC-9F7A-E611-AD3A-02163E014215.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/D6F46CED-9F7A-E611-A3AB-02163E013705.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/D8C2F63E-9F7A-E611-8302-02163E0142F0.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/DACDE0EC-9F7A-E611-A231-02163E01431F.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/DC6567EF-9F7A-E611-9324-02163E014341.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/DE4BE9EE-9F7A-E611-9611-02163E012ADD.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/E081CDEB-9F7A-E611-B718-02163E011EF8.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/E23B333E-9F7A-E611-8908-02163E0145E5.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/E8B423EC-9F7A-E611-8918-02163E014605.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/EA7155F1-9F7A-E611-9BBF-02163E014642.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/F05783EB-9F7A-E611-8146-02163E014267.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/F4C21102-A07A-E611-923E-02163E0142D6.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/FCAA5F3D-9F7A-E611-8B74-02163E0121DE.root']

process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring( *list ),
  eventsToProcess = cms.untracked.VEventRange('280667:1424567-280667:1515232')
)
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.load("EventFilter.SiStripRawToDigi.FedChannelDigis_cfi")
process.FedChannelDigis.LegacyUnpacker    = cms.bool(False)
process.FedChannelDigis.UnpackBadChannels = cms.bool(True)
process.FedChannelDigis.DoAPVEmulatorCheck = cms.bool(False)

process.load("DQM.SiStripCommissioningSources.CommissioningHistos_cfi")
process.CommissioningHistos.CommissioningTask = 'PEDESTALS'  # <-- run type taken from event data, but can be overriden

process.p = cms.Path(process.FedChannelDigis*process.CommissioningHistos)

