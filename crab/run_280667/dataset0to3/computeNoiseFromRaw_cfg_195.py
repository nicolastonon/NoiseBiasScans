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
list = ['/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/04ABEFF1-8E7A-E611-995E-02163E014384.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/0623B0EC-9F7A-E611-81EC-02163E011FA0.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/0A0C7BF6-A17A-E611-9CEE-02163E014165.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/0C3F7AEC-9F7A-E611-84AA-02163E0144E4.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/0C62CDEE-9F7A-E611-99AF-02163E0143EF.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/0CBE29F0-9F7A-E611-9B3A-02163E011C02.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/1435443E-9F7A-E611-A015-02163E014136.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/144C4E40-9F7A-E611-A094-02163E014789.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/1AD7CDDE-9F7A-E611-8221-FA163E69A996.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/220866EF-9F7A-E611-A918-FA163E2648F7.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/228C2EEE-9F7A-E611-AE1D-02163E011DFF.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/22E9ABEB-9F7A-E611-8C30-02163E0144A4.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/288362F4-9F7A-E611-8B52-02163E0143BC.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/2EB6D935-9F7A-E611-83E7-FA163E7F172A.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/328D6D44-9F7A-E611-83D3-02163E01467C.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/382975EF-9F7A-E611-B2A3-02163E014228.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/3EC4A7F3-9F7A-E611-85BB-FA163ECE34C0.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/40A0EAEB-9F7A-E611-870C-02163E01414A.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/44439FEA-9F7A-E611-9C85-02163E01424A.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/4453D93C-9F7A-E611-859F-02163E0137B2.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/447A70EC-9F7A-E611-9D68-02163E011C96.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/483325EE-9F7A-E611-868C-02163E0142B1.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/484ACFE6-9F7A-E611-A00D-FA163E56E23B.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/4C2129E9-9F7A-E611-8595-FA163EBCC08A.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/4C9B45EE-9F7A-E611-97D8-02163E013937.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/5820E7ED-9F7A-E611-A48A-02163E0133EE.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/58CBD83D-9F7A-E611-B700-02163E0137A2.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/5AD90A00-A57A-E611-8A11-02163E0142D6.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/648244F0-9F7A-E611-B69B-02163E014660.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/6A20CA6B-A07A-E611-9465-FA163E8973D0.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/72DC1238-9F7A-E611-B65B-FA163EB4B66F.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/7421E53C-9F7A-E611-9E0B-02163E014410.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/7450E6ED-9F7A-E611-AA63-02163E0137A4.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/76C374BA-8E7A-E611-9B0C-FA163E9E4DE4.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/78CACDEC-9F7A-E611-B5D7-02163E0137AA.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/7C5566F2-9F7A-E611-BA2C-02163E014596.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/82713AED-9F7A-E611-A831-02163E013422.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/82E787ED-9F7A-E611-AEE0-02163E0140E0.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/840F7FDB-9F7A-E611-A670-FA163EC389EB.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/8495725E-A37A-E611-817B-02163E0141BE.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/8A8293EE-9F7A-E611-B896-02163E014508.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/989257EE-9F7A-E611-A36D-02163E0142A0.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/9A0655F3-9F7A-E611-98FE-02163E01439E.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/9A1057EC-9F7A-E611-873A-02163E0128BC.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/ACC6EAEA-9F7A-E611-9E7D-02163E011EF6.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/AEF140E5-9F7A-E611-BBF8-FA163E8E3D2E.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/B02B7CEB-9F7A-E611-B7E4-02163E0142DE.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/B6C2C3ED-9F7A-E611-AE89-02163E011918.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/BC0955FB-9F7A-E611-AAC2-02163E0143BE.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/BE9DD7F6-9F7A-E611-8D9A-02163E014131.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/C41D2AD8-9F7A-E611-A065-FA163EE7ABB9.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/C69A963D-9F7A-E611-A0C8-02163E0143C5.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/D0B9BD3D-9F7A-E611-86A6-02163E0146B8.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/D26F56EC-9F7A-E611-AD3A-02163E014215.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/D6F46CED-9F7A-E611-A3AB-02163E013705.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/D8C2F63E-9F7A-E611-8302-02163E0142F0.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/DACDE0EC-9F7A-E611-A231-02163E01431F.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/DC6567EF-9F7A-E611-9324-02163E014341.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/DE4BE9EE-9F7A-E611-9611-02163E012ADD.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/E081CDEB-9F7A-E611-B718-02163E011EF8.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/E23B333E-9F7A-E611-8908-02163E0145E5.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/E8B423EC-9F7A-E611-8918-02163E014605.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/EA7155F1-9F7A-E611-9BBF-02163E014642.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/F05783EB-9F7A-E611-8146-02163E014267.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/F4C21102-A07A-E611-923E-02163E0142D6.root','/store/data/Run2016G/VRRandom0/RAW/v1/000/280/667/00000/FCAA5F3D-9F7A-E611-8B74-02163E0121DE.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/02477EEF-9F7A-E611-B2A3-02163E014228.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/065EB6EC-9F7A-E611-81EC-02163E011FA0.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/106177FB-9F7A-E611-AAC2-02163E0143BE.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/1865ECED-9F7A-E611-AA63-02163E0137A4.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/1CBBF7F6-9F7A-E611-8D9A-02163E014131.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/2030CEDE-9F7A-E611-8221-FA163E69A996.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/240275F3-9F7A-E611-98FE-02163E01439E.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/26537244-9F7A-E611-83D3-02163E01467C.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/28C457F0-9F7A-E611-B69B-02163E014660.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/2A12B2EB-9F7A-E611-8C30-02163E0144A4.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/30E3C3EE-9F7A-E611-B896-02163E014508.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/3219EE3C-9F7A-E611-9E0B-02163E014410.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/3C295BF1-9F7A-E611-9BBF-02163E014642.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/3E77C2F6-A17A-E611-9CEE-02163E014165.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/40BB4AEE-9F7A-E611-97D8-02163E013937.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/40CD293F-9F7A-E611-BE4F-02163E013579.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/488733F0-9F7A-E611-9B3A-02163E011C02.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/48C6E3EC-9F7A-E611-A231-02163E01431F.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/4A4681EB-9F7A-E611-B7E4-02163E0142DE.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/4C9334EE-9F7A-E611-AE1D-02163E011DFF.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/560E8AEB-9F7A-E611-8146-02163E014267.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/5ADB5BEE-9F7A-E611-A36D-02163E0142A0.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/5EB674EC-9F7A-E611-9D68-02163E011C96.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/60B85440-9F7A-E611-A094-02163E014789.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/68609D3D-9F7A-E611-A0C8-02163E0143C5.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/6A6368EF-9F7A-E611-A918-FA163E2648F7.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/6AD8EDEA-9F7A-E611-9E7D-02163E011EF6.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/6CEB633D-9F7A-E611-8B74-02163E0121DE.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/6E18483E-9F7A-E611-A015-02163E014136.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/6E1D43ED-9F7A-E611-A831-02163E013422.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/746DD4EC-9F7A-E611-B5D7-02163E0137AA.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/7474EB3D-9F7A-E611-B700-02163E0137A2.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/785941E5-9F7A-E611-BBF8-FA163E8E3D2E.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/8045DA35-9F7A-E611-83E7-FA163E7F172A.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/86061684-A37A-E611-8C3E-02163E014328.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/8E3C75BA-8E7A-E611-9B0C-FA163E9E4DE4.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/8EB3CFE6-9F7A-E611-A00D-FA163E56E23B.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/90D9F8F1-8E7A-E611-995E-02163E014384.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/96655BEC-9F7A-E611-873A-02163E0128BC.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/9C5329EE-9F7A-E611-868C-02163E0142B1.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/9C715602-A07A-E611-923E-02163E0142D6.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/A64CADF3-9F7A-E611-85BB-FA163ECE34C0.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/AAF56AF2-9F7A-E611-BA2C-02163E014596.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/AE3171ED-9F7A-E611-A3AB-02163E013705.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/B27F2AD8-9F7A-E611-A065-FA163EE7ABB9.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/B41DF1EE-9F7A-E611-9611-02163E012ADD.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/B6186CF4-9F7A-E611-8B52-02163E0143BC.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/B8AE5C70-A07A-E611-9465-FA163E8973D0.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/BCA05D3E-9F7A-E611-8908-02163E0145E5.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/BE82FB3E-9F7A-E611-8302-02163E0142F0.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/C2A96FEF-9F7A-E611-9324-02163E014341.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/C2AFCAED-9F7A-E611-AE89-02163E011918.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/C468ECED-9F7A-E611-A48A-02163E0133EE.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/C48D7FDB-9F7A-E611-A670-FA163EC389EB.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/C69AD0EE-9F7A-E611-99AF-02163E0143EF.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/C8CEA3EA-9F7A-E611-9C85-02163E01424A.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/CCA029E9-9F7A-E611-8595-FA163EBCC08A.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/D8D12FEC-9F7A-E611-8918-02163E014605.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/E0EB80EC-9F7A-E611-84AA-02163E0144E4.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/E49ADD3C-9F7A-E611-859F-02163E0137B2.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/E4DC4FEC-9F7A-E611-B718-02163E011EF8.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/E818C43D-9F7A-E611-86A6-02163E0146B8.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/EA09F0EB-9F7A-E611-870C-02163E01414A.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/ECB194ED-9F7A-E611-AEE0-02163E0140E0.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/F2DC64EC-9F7A-E611-AD3A-02163E014215.root','/store/data/Run2016G/VRRandom1/RAW/v1/000/280/667/00000/F42C1338-9F7A-E611-B65B-FA163EB4B66F.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/02775CF0-9F7A-E611-A419-02163E012A14.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/04B687F2-9F7A-E611-AF4C-FA163E0562EF.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/0C8498BD-8E7A-E611-A5A2-02163E0146B3.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/128A2EF1-9F7A-E611-9BCA-02163E014770.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/12E110EF-9F7A-E611-A43E-02163E01350A.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/1A232DED-9F7A-E611-BAC0-02163E0142B9.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/1AEA6EE9-9F7A-E611-8C1D-FA163EFB0A02.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/34B7072A-8F7A-E611-B21E-FA163EBCFA64.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/362EDBEF-9F7A-E611-BD0A-02163E0135C6.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/364FCEBD-A47A-E611-8ECB-02163E01412A.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/36E975EF-9F7A-E611-A964-02163E013750.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/3E8B04EE-9F7A-E611-8078-02163E011D78.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/403B15EF-9F7A-E611-A58F-02163E014616.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/4A17F6EB-9F7A-E611-A180-02163E0141EE.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/4A935911-A07A-E611-A121-02163E014398.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/58464703-A07A-E611-A7EB-02163E01456B.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/5A25CAEA-9F7A-E611-A66E-FA163E31002F.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/5C299622-A07A-E611-8A5D-02163E0135A6.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/5CF180ED-9F7A-E611-A7EB-02163E0136B2.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/60716996-9E7A-E611-9634-FA163E1D9629.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/60DF16F7-9F7A-E611-B238-02163E013570.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/627618EE-9F7A-E611-9637-02163E011E35.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/685213EE-9F7A-E611-863C-02163E01423F.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/6A1EEF0C-A07A-E611-91CF-FA163EB8C719.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/6C065AEF-9F7A-E611-BD20-02163E011F6B.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/72241CE6-9F7A-E611-AF16-FA163E8EC4F9.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/72E7531F-A37A-E611-8756-02163E0144A3.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/76C3D5ED-9F7A-E611-9BDC-02163E011C33.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/7C085929-A07A-E611-9058-02163E01473D.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/7C8A0E04-A27A-E611-A21E-02163E011C96.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/7E89E9E8-9F7A-E611-B215-FA163E95B499.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/7EE35CEE-9F7A-E611-8675-02163E01428A.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/8476A8C5-8E7A-E611-9BED-02163E0134E9.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/84FA85EE-9F7A-E611-A2CC-02163E0119FD.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/8C482CED-9F7A-E611-9291-02163E014164.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/8E0F9BF6-9F7A-E611-90DA-02163E01191B.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/8E9475F1-9F7A-E611-8C4E-FA163ED6B597.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/9A03BCEE-9F7A-E611-B2FF-02163E01210E.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/9AD9EDEB-9F7A-E611-A748-02163E014333.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/9EB026E7-9F7A-E611-A251-FA163EEB7B34.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/A08100E5-9F7A-E611-8A0B-FA163E06F9DB.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/ACD091EE-9F7A-E611-9339-02163E01463C.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/AE1420F2-9F7A-E611-B5AE-02163E01224B.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/B22D8EEE-9F7A-E611-9515-02163E011F43.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/B256EFE6-9F7A-E611-A319-FA163E9C2B99.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/BC20ECED-9F7A-E611-B7E9-02163E0142F9.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/BCB585FB-9F7A-E611-9359-02163E0144D2.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/C84D2EF5-9F7A-E611-8746-02163E014667.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/C8A7F9ED-9F7A-E611-BA73-02163E01457B.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/CA87BAEB-9F7A-E611-B6C0-02163E0141DB.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/CC8F73EC-9F7A-E611-AAA8-02163E0142E3.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/CCC439E7-9F7A-E611-A5B6-FA163E37EA05.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/CEA0AA01-A07A-E611-920C-02163E0143F2.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/D040FA14-A07A-E611-98EA-02163E014315.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/D047CBCC-A17A-E611-9DC5-02163E013860.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/D07D42F9-9F7A-E611-B830-02163E0135FC.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/D0C9EA09-A07A-E611-B3C7-02163E0138BA.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/D2B504E4-9F7A-E611-A07F-FA163E8DF240.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/D440C3ED-9F7A-E611-8FD7-02163E0144CE.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/DE4D2DEF-9F7A-E611-AEDB-FA163EF21E30.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/DEC97BF7-9F7A-E611-AC91-02163E0145F6.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/E0186BEE-9F7A-E611-9B5A-02163E012710.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/E256801B-A07A-E611-BDF0-02163E01445D.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/F064DCEE-9F7A-E611-B056-02163E013942.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/F07165EA-9F7A-E611-8AF5-FA163E299959.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/FA5A99EB-9F7A-E611-92CE-02163E014219.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/FA5B22EE-9F7A-E611-BEB7-02163E0137C6.root','/store/data/Run2016G/VRRandom2/RAW/v1/000/280/667/00000/FC3F83ED-9F7A-E611-A798-02163E0133C9.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/042BC1EE-9F7A-E611-B2FF-02163E01210E.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/04811BEE-9F7A-E611-863C-02163E01423F.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/100666EA-9F7A-E611-8AF5-FA163E299959.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/1047BA22-A07A-E611-8A5D-02163E0135A6.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/184EF80C-A07A-E611-91CF-FA163EB8C719.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/18B50115-A07A-E611-98EA-02163E014315.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/20936FE9-9F7A-E611-8C1D-FA163EFB0A02.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/20F4F0ED-9F7A-E611-B7E9-02163E0142F9.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/281032ED-9F7A-E611-9291-02163E014164.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/28B798EE-9F7A-E611-9339-02163E01463C.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/28FA8CEE-9F7A-E611-A2CC-02163E0119FD.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/2A679EEB-9F7A-E611-92CE-02163E014219.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/2CD714EF-9F7A-E611-A43E-02163E01350A.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/32A8FAEB-9F7A-E611-A180-02163E0141EE.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/34073BF5-9F7A-E611-8746-02163E014667.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/3A39A2F6-9F7A-E611-90DA-02163E01191B.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/3A5163F0-9F7A-E611-A419-02163E012A14.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/3E45E0EE-9F7A-E611-B056-02163E013942.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/40580A2A-8F7A-E611-B21E-FA163EBCFA64.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/42BFCAEA-9F7A-E611-A66E-FA163E31002F.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/44751CE6-9F7A-E611-AF16-FA163E8EC4F9.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/44DFC8ED-9F7A-E611-8FD7-02163E0144CE.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/502697BD-A47A-E611-8131-FA163E8973D0.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/520F62EE-9F7A-E611-8675-02163E01428A.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/526A11EE-9F7A-E611-8078-02163E011D78.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/5AFD77F1-9F7A-E611-8C4E-FA163ED6B597.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/602C5EEF-9F7A-E611-BD20-02163E011F6B.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/645365F1-A27A-E611-9C37-FA163E56E23B.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/66006829-A07A-E611-9058-02163E01473D.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/6EF6A6F1-9F7A-E611-9BCA-02163E014770.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/72C1F1EB-9F7A-E611-A748-02163E014333.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/781B7AEF-9F7A-E611-A964-02163E013750.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/78776FEE-9F7A-E611-9B5A-02163E012710.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/78FA911B-A07A-E611-BDF0-02163E01445D.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/7C5089F2-9F7A-E611-AF4C-FA163E0562EF.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/806DD9D4-A17A-E611-B97D-02163E0143B4.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/808AAF01-A07A-E611-920C-02163E0143F2.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/841646F9-9F7A-E611-B830-02163E0135FC.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/849DEF09-A07A-E611-B3C7-02163E0138BA.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/84B027E7-9F7A-E611-A251-FA163EEB7B34.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/86722EEF-9F7A-E611-AEDB-FA163EF21E30.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/9AC40AE4-9F7A-E611-A07F-FA163E8DF240.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/9AD526EE-9F7A-E611-BEB7-02163E0137C6.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/A01082F7-9F7A-E611-AC91-02163E0145F6.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/AA11EAE8-9F7A-E611-B215-FA163E95B499.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/B4BB94EE-9F7A-E611-9515-02163E011F43.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/B67E1CF7-9F7A-E611-B238-02163E013570.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/BCD65D11-A07A-E611-A121-02163E014398.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/C2315318-A27A-E611-936E-02163E011DEC.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/C66D31ED-9F7A-E611-BAC0-02163E0142B9.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/C677B0C5-8E7A-E611-9BED-02163E0134E9.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/C68B78EC-9F7A-E611-AAA8-02163E0142E3.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/CC65D4FB-9F7A-E611-9359-02163E0144D2.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/CCDF8403-A07A-E611-A7EB-02163E01456B.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/D03988ED-9F7A-E611-A798-02163E0133C9.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/D6AD1CEE-9F7A-E611-9637-02163E011E35.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/D80B16E5-9F7A-E611-8A0B-FA163E06F9DB.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/D8569FBD-8E7A-E611-A5A2-02163E0146B3.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/DACF00EE-9F7A-E611-BA73-02163E01457B.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/DC29E9EF-9F7A-E611-BD0A-02163E0135C6.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/E2844FE7-9F7A-E611-A5B6-FA163E37EA05.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/E86D21EF-9F7A-E611-A58F-02163E014616.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/E8C0EFE6-9F7A-E611-A319-FA163E9C2B99.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/E8E7BEEB-9F7A-E611-B6C0-02163E0141DB.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/ECFD84ED-9F7A-E611-A7EB-02163E0136B2.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/F0AF6D96-9E7A-E611-9634-FA163E1D9629.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/F29285F2-9F7A-E611-B5AE-02163E01224B.root','/store/data/Run2016G/VRRandom3/RAW/v1/000/280/667/00000/FE12DBED-9F7A-E611-9BDC-02163E011C33.root']

process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring( *list ),
  eventsToProcess = cms.untracked.VEventRange('280667:1000244-280667:1090415')
)
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.load("EventFilter.SiStripRawToDigi.FedChannelDigis_cfi")
process.FedChannelDigis.LegacyUnpacker    = cms.bool(False)
process.FedChannelDigis.UnpackBadChannels = cms.bool(True)
process.FedChannelDigis.DoAPVEmulatorCheck = cms.bool(False)

process.load("DQM.SiStripCommissioningSources.CommissioningHistos_cfi")
process.CommissioningHistos.CommissioningTask = 'PEDESTALS'  # <-- run type taken from event data, but can be overriden

process.p = cms.Path(process.FedChannelDigis*process.CommissioningHistos)

