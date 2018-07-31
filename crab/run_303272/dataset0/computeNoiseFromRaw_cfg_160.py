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
  fileNames = cms.untracked.vstring('/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/0003DB9A-A49E-E711-807A-02163E01412C.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/024888A1-A49E-E711-B5C8-02163E01A1F0.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/025D13A2-A49E-E711-9D43-02163E011D5B.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/0260F89B-A49E-E711-8DAE-02163E013517.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/02BBABBF-A49E-E711-AA16-02163E01A63D.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/02DA6AA0-A49E-E711-A533-02163E01A3C8.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/040E5995-A49E-E711-928E-02163E01A41B.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/043F518F-A49E-E711-AE1C-02163E011CF7.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/0A157AB2-A49E-E711-A138-02163E01A728.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/0A2016BB-A49E-E711-9E7D-02163E01A545.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/0A6C62A5-A49E-E711-9CC9-02163E01A422.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/0CA93DB3-A49E-E711-BA62-02163E01A69D.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/0E29D1A9-A79E-E711-AE4C-02163E01A527.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/0EC767A5-A49E-E711-B6CF-02163E014668.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/10F355C5-A49E-E711-8853-02163E01A674.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/127BAFA0-A49E-E711-BB2E-02163E019CB3.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/12D7EF9F-A49E-E711-B42A-02163E011F1B.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/14A77093-A49E-E711-A9C2-02163E01A5FF.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/14B2BF9D-A49E-E711-B1F2-02163E019D2B.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/1652E6A2-A49E-E711-90C5-02163E011F1B.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/16FD30A3-A49E-E711-B642-02163E012423.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/182955B5-A99E-E711-B0CC-02163E01A5FF.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/187D9DA0-A49E-E711-A867-02163E019D2A.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/1A803AB3-A49E-E711-92CD-02163E01A69D.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/1C461796-A49E-E711-A919-02163E01A4BF.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/2212729B-A49E-E711-8AA4-02163E019B9B.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/229FF2A6-A49E-E711-9780-02163E019CB3.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/22B853A5-A49E-E711-A0AD-02163E01A1BD.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/2416ACBF-A49E-E711-B036-02163E01A63D.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/24184DF1-F39D-E711-8B51-02163E019DD8.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/24758CB7-A49E-E711-9D69-02163E01A6F2.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/248CA6A9-A49E-E711-A351-02163E019BDF.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/262DDA96-A49E-E711-A8CF-02163E012AE7.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/263C1AA2-A49E-E711-9DA1-02163E011D5B.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/268627A0-A49E-E711-93BA-02163E019CD5.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/282A34AC-A49E-E711-AD11-02163E014154.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/2A590AD2-A49E-E711-A86C-02163E01A76C.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/2E29EC9E-A49E-E711-A790-02163E012B4E.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/2E2B219F-A49E-E711-AE87-02163E012AC5.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/2EA00398-A49E-E711-890B-02163E014555.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/3288A6A9-A49E-E711-806D-02163E019BDF.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/32E1958E-A49E-E711-8035-02163E0142AB.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/3485C59A-A49E-E711-ADA0-02163E01A626.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/34C4589B-A49E-E711-A922-02163E012B4E.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/360F9198-A49E-E711-9844-02163E01A38B.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/3A34FDAD-A49E-E711-9845-02163E01A2DA.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/3AA96F9E-A49E-E711-B069-02163E011A4C.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/3C8E919A-A49E-E711-8CB6-02163E012428.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/3CEB039E-A49E-E711-9AF3-02163E01A267.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/3E7A1D9E-A49E-E711-AE6C-02163E019E86.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/3EA9F7A8-A49E-E711-910D-02163E019BAB.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/40B7EFAF-A49E-E711-A4B3-02163E01A782.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/40E9179C-A49E-E711-8A12-02163E013746.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/4203489B-A49E-E711-BAF7-02163E0146B8.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/423904A4-A49E-E711-A68E-02163E01A708.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/4242FCEF-F39D-E711-B93D-02163E019C59.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/42C7A295-A49E-E711-9FA3-02163E019E55.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/4414CD8F-A49E-E711-88B7-02163E01A3B6.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/448ADBB0-A49E-E711-93F7-02163E019C4A.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/44CFCABD-A49E-E711-BCD8-02163E01A655.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/46BC45A9-A49E-E711-A17E-02163E01A3DE.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/46F6C495-A49E-E711-ACD9-02163E01A6D6.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/48528BB7-A49E-E711-A034-02163E01A6F2.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/48745D8C-A49E-E711-AFF0-02163E011E91.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/489443C2-A49E-E711-96E6-02163E019BC0.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/4A389598-A49E-E711-BD16-02163E01A4BF.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/4A70B09F-A49E-E711-BA7E-02163E0141E1.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/4A77D9BA-A49E-E711-A72B-02163E019B8E.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/4A94919A-A49E-E711-9A69-02163E01A41B.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/4C113AA5-A49E-E711-B7E4-02163E0144E5.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/4CA2139F-A49E-E711-AEBF-02163E0146B0.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/4CA6848E-A49E-E711-BF38-02163E0142AB.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/4EE994B6-A49E-E711-9E15-02163E01A20C.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/50548A8B-A49E-E711-A9CD-02163E019BE3.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/505C5595-A49E-E711-A929-02163E0134E0.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/50AA49A3-A49E-E711-93DB-02163E012AC5.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/5243CCAD-A49E-E711-8A36-02163E014154.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/565FF1B8-A49E-E711-89DE-02163E019CC1.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/5690EBAB-A49E-E711-B7D3-02163E014668.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/56B0C0D9-A49E-E711-82FC-02163E01A782.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/56CAFFAD-A49E-E711-BE5E-02163E01A2DA.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/583195B9-A49E-E711-9C5B-02163E01A545.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/58AD728D-A49E-E711-A2B7-02163E01419E.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/58F3949D-A49E-E711-9146-02163E011887.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/5A1978B0-A49E-E711-8D10-02163E01A2A2.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/5A28BDB1-A49E-E711-8844-02163E01A4CA.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/5A329AB6-A49E-E711-9799-02163E01A20C.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/5A7AAE9B-A49E-E711-985C-02163E01A747.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/5A863B99-A49E-E711-BB85-02163E01A597.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/5AA6888B-A49E-E711-B273-02163E0135C6.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/5AFF0BBE-A49E-E711-ADA5-02163E01A655.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/5C05F5CE-AC9E-E711-834A-02163E019D35.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/5C4983AA-A49E-E711-926F-02163E019E3F.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/5CF81B9F-A49E-E711-98FD-02163E0144E5.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/5E28498B-A49E-E711-B8BB-02163E014785.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/5E8C799C-A49E-E711-80AF-02163E019DC0.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/5E9F42AC-A49E-E711-AAC0-02163E019D00.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/60437BC3-A49E-E711-85BF-02163E019B8E.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/621BB7AD-A49E-E711-A987-02163E01A74D.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/621C33A4-A49E-E711-A692-02163E01A2A2.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/6484439D-A49E-E711-B741-02163E01A40C.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/64EA92A1-A49E-E711-BE3D-02163E019CD1.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/6A233AC5-A49E-E711-BB87-02163E01A52D.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/6A326EB4-A49E-E711-827D-02163E01A445.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/6A768458-A69E-E711-BAF9-02163E01A63C.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/6AC9D1A0-A49E-E711-BF16-02163E014195.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/6C6F95B7-A49E-E711-B1CD-02163E01A602.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/6CD949C6-A49E-E711-B902-02163E01A674.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/6E0B6F90-A49E-E711-AE39-02163E011CF0.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/701EAD8D-A49E-E711-8B39-02163E011CF7.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/705AFEAA-A49E-E711-87B1-02163E019E3F.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/7206DDA0-A49E-E711-A6D8-02163E019CD1.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/7286BBBA-A49E-E711-91AE-02163E01A5E5.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/74478D9E-A49E-E711-B42B-02163E019B46.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/74E44BAC-A49E-E711-A63C-02163E019D00.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/7625D297-A49E-E711-A602-02163E01A6D6.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/76495FA5-A49E-E711-B064-02163E01A422.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/76B8A5A4-A49E-E711-B117-02163E013647.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/76BEEEC3-A49E-E711-84D3-02163E019BC0.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/78515B8B-A49E-E711-B024-02163E014785.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/786496AB-A49E-E711-B23D-02163E019B6A.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/78B28D9D-A49E-E711-9811-02163E0141E1.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/7A179CAF-A49E-E711-A61F-02163E01A5E1.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/7A30FC9A-A49E-E711-8335-02163E019B9B.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/7A60A9B3-A49E-E711-92E0-02163E019B6E.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/7A62F1A5-A49E-E711-8975-02163E01352E.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/7A8617AC-A49E-E711-8CF5-02163E019B6A.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/7A99E6BA-A49E-E711-806F-02163E01A5E5.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/7C329594-A49E-E711-96AE-02163E011A88.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/7E45D5AD-A49E-E711-AE8C-02163E01A4E6.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/7E96B7B1-A49E-E711-AAE5-02163E01A4CA.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/828FD190-A49E-E711-B4EE-02163E013472.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/84D3E09F-A49E-E711-8541-02163E01A378.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/863125A6-A49E-E711-91EA-02163E014195.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/86327D93-A49E-E711-A6F2-02163E019C9C.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/864AB08E-A49E-E711-BD79-02163E019C6D.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/88680AA1-A49E-E711-83E7-02163E01A378.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/88B1899C-A49E-E711-8EDD-02163E011A4C.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/88E53AA8-A49E-E711-8BDE-02163E019B47.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/8A8417B2-A49E-E711-B2A1-02163E01352E.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/8ADE449E-A49E-E711-A7C3-02163E019B46.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/8CE14DA4-A49E-E711-8A79-02163E012385.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/92DA449F-A49E-E711-8A20-02163E011BEA.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/94436DAC-A49E-E711-A2B2-02163E012AE7.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/9448C4E1-A49E-E711-B921-02163E019B24.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/94AA1B97-A49E-E711-95B0-02163E01A560.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/94C88091-A49E-E711-A202-02163E01A6AA.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/968849A7-A49E-E711-833F-02163E019E8A.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/96A972B2-A49E-E711-9182-02163E01A56F.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/96C41496-A49E-E711-9642-02163E019E55.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/985AF89C-A49E-E711-ACCE-02163E0123DD.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/988C568F-A49E-E711-BF04-02163E019DE5.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/9ED6D7A4-A49E-E711-ABFA-02163E01249B.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/A409E8B0-A49E-E711-B280-02163E012643.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/A68BB69F-A49E-E711-9757-02163E01A38B.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/A6D6479B-A49E-E711-ACB7-02163E014713.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/A81BBE9C-A49E-E711-BF34-02163E013703.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/AA65E2B8-A49E-E711-9A73-02163E019CC1.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/AA6D49A4-A49E-E711-9D7E-02163E012385.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/ACDD409F-A49E-E711-B9D9-02163E01364A.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/ACF612AE-AA9E-E711-AE76-02163E019C29.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/AEE6EFAD-A49E-E711-91DE-02163E019B6E.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/B0B1B99E-A49E-E711-B0E8-02163E01A40D.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/B271F393-A49E-E711-A263-02163E0145C4.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/B43D6EB4-A49E-E711-8201-02163E01A445.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/B4444996-A49E-E711-AB09-02163E0145C4.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/B4C602CF-A39E-E711-BB90-02163E011E91.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/B6947DCE-A49E-E711-AD78-02163E01A76C.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/B6C02DA7-A49E-E711-9071-02163E011B79.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/B80913BD-A49E-E711-8257-02163E019D68.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/B887789D-A49E-E711-83E9-02163E019DC0.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/B8DC0395-A49E-E711-A9D2-02163E0134E0.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/BC0A4BB2-A49E-E711-AA51-02163E01A728.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/BC17A6A4-A49E-E711-B8C2-02163E01A1F0.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/BCAEF6A8-A49E-E711-A4A2-02163E019BAB.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/BE7FDCAE-A49E-E711-8E63-02163E019DC5.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/BEC584A7-A49E-E711-8223-02163E011B79.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/C0121393-A49E-E711-8EA3-02163E019C6D.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/C032DDA3-A49E-E711-9A41-02163E01A708.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/C0412648-A89E-E711-8D6E-02163E011E17.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/C0E2F99F-A49E-E711-B73E-02163E01A40C.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/C22FA6BD-A49E-E711-BC28-02163E01A606.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/C26ED6A8-A49E-E711-8E15-02163E019B30.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/C270BFAE-A49E-E711-A065-02163E0144C8.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/C2B6898F-A49E-E711-8641-02163E011E17.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/C4D1B7AD-A49E-E711-B808-02163E01A74D.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/C65E379A-A49E-E711-94CE-02163E011D9E.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/C8456A19-A59E-E711-A04D-02163E014593.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/C8B718A4-A49E-E711-AC55-02163E0133BF.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/C8C5989D-A49E-E711-AB7D-02163E011887.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/C8FF3094-A49E-E711-AA9C-02163E01A5FF.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/CA72BFAE-A49E-E711-AAD3-02163E0144C8.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/CC5665A0-A49E-E711-9207-02163E0123DD.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/CC6B6F23-A89E-E711-8CBE-02163E01419E.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/CCF3CE46-A79E-E711-B527-02163E01419E.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/CE14936D-A89E-E711-A393-02163E011B96.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/CE862293-A49E-E711-9FF4-02163E01A560.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/D0CA26A3-A49E-E711-922A-02163E01249B.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/D0D1DAA6-A49E-E711-9BB5-02163E013647.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/D0E2679A-A49E-E711-9B2F-02163E0146B0.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/D202409B-A49E-E711-AFCF-02163E0133EB.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/D2383E94-A49E-E711-98C5-02163E0135C6.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/D2B670B6-A49E-E711-88F8-02163E01A1B8.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/D479CE9D-A49E-E711-AC97-02163E01A3C8.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/D4A35899-A49E-E711-A715-02163E013703.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/D4B3249A-A49E-E711-88F9-02163E019CA3.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/D62732A8-A49E-E711-9B2F-02163E019B47.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/D6EE179C-A49E-E711-AB5B-02163E013746.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/D8522687-A49E-E711-B24D-02163E014736.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/D87E27A0-A49E-E711-B766-02163E019CD5.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/D8E6C3E1-A49E-E711-BF6E-02163E019B24.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/D8EEDF9A-A49E-E711-AA84-02163E0133BF.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/DCF596BC-AC9E-E711-AB78-02163E01475B.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/DCFE46A7-A49E-E711-A5C0-02163E019E8A.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/E404879A-A49E-E711-8B00-02163E01A747.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/E426D58E-A49E-E711-A2E6-02163E011CF0.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/E442381E-F69D-E711-97FB-02163E01A657.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/E4459AAF-A49E-E711-9DA0-02163E01A5E1.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/E4F91CBA-A49E-E711-A43B-02163E019D68.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/E6BC50A3-A49E-E711-86B1-02163E01A267.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/E8630398-A49E-E711-BF60-02163E014555.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/E89EB2B7-A49E-E711-A9B8-02163E01A602.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/E8AA0FAE-A49E-E711-ADCA-02163E01A4E6.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/EAD240A3-A49E-E711-985E-02163E014713.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/EAE0B291-A49E-E711-9AF4-02163E0141AF.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/EE39879C-A49E-E711-8555-02163E011A88.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/EE40289A-A49E-E711-989A-02163E019D2B.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/EE5F3997-A49E-E711-B860-02163E0135FD.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/EE92F0B1-A49E-E711-BC81-02163E019DC5.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/EEB9AFBC-A49E-E711-A5CB-02163E01A52D.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/F022B89E-A49E-E711-A6FB-02163E01A40D.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/F41D409F-A49E-E711-B13D-02163E019CA3.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/F4E96FB2-A49E-E711-8222-02163E01A56F.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/F69857A1-A49E-E711-A91B-02163E01A232.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/F6A13998-A49E-E711-A5E7-02163E01412C.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/F6DC8D9A-A49E-E711-93F9-02163E012428.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/F819E8B0-A49E-E711-A3B8-02163E012643.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/F838D6A8-A49E-E711-A650-02163E019B30.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/F8442F96-A79E-E711-A5EB-02163E0135C6.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/F87102DB-A39E-E711-A76C-02163E01A733.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/F88942A0-A49E-E711-B1D1-02163E01A1BD.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/FC883769-A79E-E711-AD07-02163E01A2A2.root','/store/data/Run2017D/VRRandom0/RAW/v1/000/303/272/00000/FCCA2FAF-A49E-E711-B42C-02163E019C4A.root'),
  eventsToProcess = cms.untracked.VEventRange('303272:541162-303272:560827')
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

