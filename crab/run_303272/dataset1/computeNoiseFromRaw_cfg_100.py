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
  fileNames = cms.untracked.vstring('/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/00A847A7-A49E-E711-A5C0-02163E019E8A.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/0296FCEF-F39D-E711-B93D-02163E019C59.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/02C156A5-A49E-E711-A0AD-02163E01A1BD.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/04ECA6AF-A49E-E711-A61F-02163E01A5E1.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/0692B28D-A49E-E711-8B39-02163E011CF7.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/06B07AAC-A49E-E711-A2B2-02163E012AE7.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/089B2C9F-A49E-E711-AEBF-02163E0146B0.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/08FB8590-A49E-E711-AE39-02163E011CF0.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/0CED7D93-A49E-E711-A6F2-02163E019C9C.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/0E976AA0-A49E-E711-9207-02163E0123DD.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/0EB62896-A49E-E711-A919-02163E01A4BF.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/0EF6A6AF-A49E-E711-9DA0-02163E01A5E1.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/10997CB2-A49E-E711-8222-02163E01A56F.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/10E761C5-A49E-E711-8853-02163E01A674.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/1269FD9B-A49E-E711-8DAE-02163E013517.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/1291C8B2-A49E-E711-B2A1-02163E01352E.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/141DBAAB-A49E-E711-B23D-02163E019B6A.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/1471DAA0-A49E-E711-BB2E-02163E019CB3.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/1895F4B8-A49E-E711-89DE-02163E019CC1.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/1A6329A0-A49E-E711-93BA-02163E019CD5.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/1C6F1E9D-A49E-E711-8555-02163E011A88.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/1CC84E9B-A49E-E711-BAF7-02163E0146B8.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/1E3AB2B9-A49E-E711-9C5B-02163E01A545.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/1E6AB1BC-A49E-E711-A5CB-02163E01A52D.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/1E76BBBF-A49E-E711-AA16-02163E01A63D.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/208C5397-A49E-E711-B860-02163E0135FD.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/220C889A-A49E-E711-8B00-02163E01A747.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/22251E96-A49E-E711-9642-02163E019E55.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/22C6AFB3-A49E-E711-92E0-02163E019B6E.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/246C46C5-A49E-E711-BB87-02163E01A52D.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/249392A7-A49E-E711-8223-02163E011B79.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/260A628C-A49E-E711-AFF0-02163E011E91.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/2826E5A4-A49E-E711-ABFA-02163E01249B.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/2A61929C-A49E-E711-8EDD-02163E011A4C.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/2A883B9A-A49E-E711-989A-02163E019D2B.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/2C01A3B7-A49E-E711-A034-02163E01A6F2.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/2CAD83B2-A49E-E711-A138-02163E01A728.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/2CEEBE9F-A49E-E711-9757-02163E01A38B.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/2E346D3D-A79E-E711-80E8-02163E01A527.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/2E3D46A9-A49E-E711-A17E-02163E01A3DE.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/2E3D50C2-A49E-E711-96E6-02163E019BC0.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/2E87A4A1-A49E-E711-BE3D-02163E019CD1.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/2EB7CB46-A89E-E711-8E31-02163E011B79.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/305037A3-A49E-E711-922A-02163E01249B.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/30D856E2-A49E-E711-BF6E-02163E019B24.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/3218EAA8-A49E-E711-A650-02163E019B30.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/328AE3A6-A49E-E711-9BB5-02163E013647.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/32DB9DA0-A49E-E711-A867-02163E019D2A.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/3472089D-A49E-E711-ACCE-02163E0123DD.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/34BCA498-A49E-E711-BD16-02163E01A4BF.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/36AA2E9C-A49E-E711-AB5B-02163E013746.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/385012B1-A49E-E711-B280-02163E012643.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/387E729B-A99E-E711-ABE2-02163E01A7A2.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/3A4C4AC6-A49E-E711-B902-02163E01A674.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/3C73D297-A49E-E711-A602-02163E01A6D6.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/3CA8CA9C-A49E-E711-BF34-02163E013703.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/3CC125CF-A39E-E711-BB90-02163E011E91.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/3E2D7A9D-A49E-E711-83E9-02163E019DC0.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/3E6F87B2-A49E-E711-9182-02163E01A56F.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/405A459E-A49E-E711-A7C3-02163E019B46.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/42059498-A49E-E711-9844-02163E01A38B.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/4250739B-A49E-E711-8AA4-02163E019B9B.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/42CBE18E-A49E-E711-A2E6-02163E011CF0.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/4402A7A9-A49E-E711-A351-02163E019BDF.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/444E7193-A49E-E711-A9C2-02163E01A5FF.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/44C5D3F2-F39D-E711-A55F-02163E01290A.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/46F9FEA8-A49E-E711-A4A2-02163E019BAB.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/48693DA8-A49E-E711-8BDE-02163E019B47.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/48A1B5B6-A49E-E711-9799-02163E01A20C.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/4A34999D-A49E-E711-9811-02163E0141E1.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/4A474A9D-A49E-E711-B741-02163E01A40C.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/4AAAF89F-A49E-E711-B42A-02163E011F1B.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/4ACCE09A-A49E-E711-807A-02163E01412C.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/4E7D049F-A49E-E711-A790-02163E012B4E.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/4EB9F20F-AA9E-E711-B71E-02163E01A47E.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/50E7F3B1-A49E-E711-BC81-02163E019DC5.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/527733A4-A49E-E711-A692-02163E01A2A2.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/52997B9E-A49E-E711-B069-02163E011A4C.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/52E354A3-A49E-E711-93DB-02163E012AC5.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/547E65A5-A49E-E711-9CC9-02163E01A422.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/56573D98-A49E-E711-A5E7-02163E01412C.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/569313C9-AC9E-E711-A395-02163E0133E1.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/5817E196-A49E-E711-A8CF-02163E012AE7.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/5820C5BD-A49E-E711-BC28-02163E01A606.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/5A182393-A49E-E711-9FF4-02163E01A560.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/5A1C7FCE-A49E-E711-AD78-02163E01A76C.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/5A791D97-A49E-E711-95B0-02163E01A560.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/5E68F0AD-A49E-E711-91DE-02163E019B6E.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/5EF411C4-A49E-E711-84D3-02163E019BC0.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/601A3394-A49E-E711-AA9C-02163E01A5FF.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/603990A6-A79E-E711-9556-02163E01A2A2.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/625763AC-A49E-E711-A63C-02163E019D00.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/64F8BBBA-A49E-E711-91AE-02163E01A5E5.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/666053AF-A49E-E711-B42C-02163E019C4A.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/66861793-A49E-E711-8EA3-02163E019C6D.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/66EF3DB3-A49E-E711-92CD-02163E01A69D.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/6AD0F9A3-A49E-E711-9A41-02163E01A708.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/6AF523AF-A49E-E711-8E63-02163E019DC5.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/6C974A94-A49E-E711-98C5-02163E0135C6.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/6E5677A1-A49E-E711-A91B-02163E01A232.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/6ECCBD9E-A49E-E711-A6FB-02163E01A40D.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/70B86EB4-A49E-E711-827D-02163E01A445.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/70BEA79D-A49E-E711-9146-02163E011887.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/70FF7E6E-A79E-E711-9CDE-02163E011B96.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/72DBF2BA-A49E-E711-806F-02163E01A5E5.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/746B67A5-A49E-E711-B064-02163E01A422.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/7627C08E-A49E-E711-8035-02163E0142AB.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/76C055E2-A49E-E711-B921-02163E019B24.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/76D2639A-A49E-E711-94CE-02163E011D9E.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/76F457AC-A49E-E711-AAC0-02163E019D00.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/7833E29F-A49E-E711-8541-02163E01A378.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/7841D19D-A49E-E711-AC97-02163E01A3C8.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/7A4B918B-A49E-E711-B273-02163E0135C6.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/7A5B4CA2-A49E-E711-9DA1-02163E011D5B.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/7A9041A0-A49E-E711-B73E-02163E01A40C.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/7AFB6D9F-A49E-E711-B9D9-02163E01364A.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/7EFF08A7-A49E-E711-9780-02163E019CB3.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/800A758D-A49E-E711-A2B7-02163E01419E.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/80576C99-A49E-E711-A715-02163E013703.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/809AF0AE-A49E-E711-A065-02163E0144C8.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/80D8999A-A49E-E711-93F9-02163E012428.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/82DC59AC-A49E-E711-AD11-02163E014154.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/84ACB394-A49E-E711-96AE-02163E011A88.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/86979AB6-A49E-E711-88F8-02163E01A1B8.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/881A08A6-A49E-E711-8975-02163E01352E.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/88A31EAC-A49E-E711-8CF5-02163E019B6A.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/8A57259A-A49E-E711-88F9-02163E019CA3.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/8C9B5C95-A49E-E711-A929-02163E0134E0.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/8CBCB08E-A49E-E711-BF38-02163E0142AB.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/8E8BA19A-A49E-E711-8CB6-02163E012428.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/8ED2B891-A49E-E711-9AF4-02163E0141AF.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/90449A91-A49E-E711-A202-02163E01A6AA.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/926CE49A-A49E-E711-AA84-02163E0133BF.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/9459DC9A-A49E-E711-ADA0-02163E01A626.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/94738B8B-A49E-E711-A9CD-02163E019BE3.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/948C3BBD-A49E-E711-8257-02163E019D68.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/961F18CF-A39E-E711-B1B6-02163E0139A8.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/964ED3B1-A49E-E711-8844-02163E01A4CA.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/969354A0-A49E-E711-B1D1-02163E01A1BD.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/96B71598-A49E-E711-890B-02163E014555.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/96C0F0AE-A49E-E711-AAD3-02163E0144C8.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/9813389F-A49E-E711-AE87-02163E012AC5.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/986B9AB7-A49E-E711-B1CD-02163E01A602.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/98C9B08E-A49E-E711-BD79-02163E019C6D.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/98D708B0-A49E-E711-A4B3-02163E01A782.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/9A71BF9E-A49E-E711-B0E8-02163E01A40D.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/9AC3628B-A49E-E711-B024-02163E014785.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/9CB08D9E-A49E-E711-B42B-02163E019B46.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/9CB38495-A49E-E711-928E-02163E01A41B.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/A03CA6BB-A79E-E711-B0D1-02163E01A3F3.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/A0886EA5-A49E-E711-B6CF-02163E014668.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/A4AAA8A9-A49E-E711-806D-02163E019BDF.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/A629558B-A49E-E711-B8BB-02163E014785.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/A6419A19-A59E-E711-A04D-02163E014593.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/A6CF32A8-A49E-E711-9B2F-02163E019B47.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/A6FE4C96-A49E-E711-AB09-02163E0145C4.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/A8DC38A2-A49E-E711-9D43-02163E011D5B.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/AA8170B4-A49E-E711-8201-02163E01A445.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/AA8B099E-A49E-E711-9AF3-02163E01A267.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/AAB2679B-A49E-E711-A922-02163E012B4E.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/AC264CA0-A49E-E711-8A20-02163E011BEA.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/ACB0F49F-A49E-E711-BA7E-02163E0141E1.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/AE44EFA0-A49E-E711-A6D8-02163E019CD1.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/AE8BAEA4-A49E-E711-B117-02163E013647.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/B03BEAD9-A49E-E711-82FC-02163E01A782.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/B067B99D-A49E-E711-AB7D-02163E011887.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/B2E89E8F-A49E-E711-8641-02163E011E17.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/B42D4EA3-A49E-E711-985E-02163E014713.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/B623E9B0-A49E-E711-93F7-02163E019C4A.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/B63147B3-A49E-E711-BA62-02163E01A69D.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/B64F56A4-A49E-E711-9D7E-02163E012385.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/B8144E9F-A49E-E711-B13D-02163E019CA3.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/B88149A5-A49E-E711-B7E4-02163E0144E5.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/BAE8FFA8-A49E-E711-910D-02163E019BAB.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/BC984DF1-F39D-E711-8B51-02163E019DD8.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/BE9774AE-A49E-E711-BE5E-02163E01A2DA.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/C04DB5A7-A39E-E711-B84D-02163E0133A5.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/C0530795-A49E-E711-A9D2-02163E0134E0.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/C2FE539B-A49E-E711-ACB7-02163E014713.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/C48B1EBA-A49E-E711-A43B-02163E019D68.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/C4AC959A-A49E-E711-9A69-02163E01A41B.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/C4B753B9-A89E-E711-92E0-02163E0141C4.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/C4C646A7-A49E-E711-9071-02163E011B79.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/C6287AB0-A49E-E711-8D10-02163E01A2A2.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/C68D2ABE-A49E-E711-ADA5-02163E01A655.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/C6CF7EC3-A49E-E711-85BF-02163E019B8E.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/C8E0DA90-A49E-E711-B4EE-02163E013472.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/CA2688AA-A49E-E711-926F-02163E019E3F.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/CA30EEAD-A49E-E711-AE8C-02163E01A4E6.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/CA47EBA8-A49E-E711-8E15-02163E019B30.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/CAEFA2B7-A49E-E711-9D69-02163E01A6F2.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/CC27B4B7-A49E-E711-A9B8-02163E01A602.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/CCFF21A4-A49E-E711-A68E-02163E01A708.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/CE3D14AE-A49E-E711-ADCA-02163E01A4E6.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/CE75BBBF-A49E-E711-B036-02163E01A63D.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/CE8AF2A0-A49E-E711-BF16-02163E014195.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/CE914DB2-A49E-E711-AA51-02163E01A728.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/D01F2CDB-A39E-E711-A76C-02163E01A733.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/D07C379F-A49E-E711-98FD-02163E0144E5.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/D07FF2B8-A49E-E711-9A73-02163E019CC1.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/D27FD8AD-A49E-E711-A987-02163E01A74D.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/D4E02365-A89E-E711-A63C-02163E01A572.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/D6AD16BB-A49E-E711-9E7D-02163E01A545.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/DA7420D2-A49E-E711-A86C-02163E01A76C.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/DA8CA2A1-A49E-E711-B5C8-02163E01A1F0.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/DA980196-A49E-E711-9FA3-02163E019E55.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/DAB905A3-A49E-E711-90C5-02163E011F1B.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/DE5D6FA0-A49E-E711-A533-02163E01A3C8.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/DE8F7B8F-A49E-E711-AE1C-02163E011CF7.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/DE99D58F-A49E-E711-88B7-02163E01A3B6.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/E00145B1-A49E-E711-A3B8-02163E012643.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/E00E01AC-A49E-E711-B7D3-02163E014668.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/E05B29A0-A49E-E711-B766-02163E019CD5.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/E086539B-A49E-E711-AFCF-02163E0133EB.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/E200578F-A49E-E711-BF04-02163E019DE5.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/E27804AB-A49E-E711-87B1-02163E019E3F.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/E28D1198-A49E-E711-BF60-02163E014555.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/E601AF9B-A49E-E711-985C-02163E01A747.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/E6364A99-A49E-E711-BB85-02163E01A597.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/E6DCFC9A-A49E-E711-8335-02163E019B9B.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/E6F2CDA4-A49E-E711-B8C2-02163E01A1F0.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/E8A22E9C-A49E-E711-8A12-02163E013746.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/E8D23687-A49E-E711-B24D-02163E014736.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/E8E324A1-A49E-E711-83E7-02163E01A378.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/EA7673AE-A49E-E711-9845-02163E01A2DA.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/EA87E7BA-A49E-E711-A72B-02163E019B8E.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/EA8E52A3-A49E-E711-86B1-02163E01A267.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/EA8EF893-A49E-E711-A263-02163E0145C4.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/ECB4C69D-A49E-E711-B1F2-02163E019D2B.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/ECB557A7-A49E-E711-833F-02163E019E8A.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/EE091EA4-A49E-E711-AC55-02163E0133BF.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/EE943EA3-A49E-E711-B642-02163E012423.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/EE99C995-A49E-E711-ACD9-02163E01A6D6.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/EEDB3FA6-A49E-E711-91EA-02163E014195.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/F0228A9A-A49E-E711-9B2F-02163E0146B0.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/F232C0B1-A49E-E711-AAE5-02163E01A4CA.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/F2D462A4-A49E-E711-8A79-02163E012385.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/F47079AE-A49E-E711-8A36-02163E014154.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/F632259E-A49E-E711-AE6C-02163E019E86.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/F881D8AD-A49E-E711-B808-02163E01A74D.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/FAED9DB6-A49E-E711-9E15-02163E01A20C.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/FECB7B9C-A49E-E711-80AF-02163E019DC0.root','/store/data/Run2017D/VRRandom1/RAW/v1/000/303/272/00000/FEF9CCBD-A49E-E711-BCD8-02163E01A655.root'),
  eventsToProcess = cms.untracked.VEventRange('303272:394266-303272:414088')
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

