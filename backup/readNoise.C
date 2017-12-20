#include <TFile.h>
#include <TDirectory.h>
#include <TList.h>
#include <TProfile.h>
#include <TIterator.h>
#include <TObject.h>
#include <iostream>
#include <string>
#include <TH1F.h>
#include <TF1.h>
#include <TH1I.h>
#include <TCanvas.h>
#include <TH2F.h>
#include <TGraphErrors.h>
#include <TFunction.h>
#include <TROOT.h>
#include "TMath.h"
#include "TTree.h"
#include <iostream>
#include <map>
#include <exception>
#include "fedKey.h"
#include "TPaveStats.h"

#include "mapFedkeyToDetid.h"

#define StripsPerApv 128
#define MinNoise 0
#define MaxNoise 10

using namespace std;

//TFile* myFile;
TH1F* myDist;
TH1F* myDisttrimmed;
TH1F* myDisttrimmedTwice;

//TH1F* myDistAPV2            = new TH1F("testDistribution2",  "test distribution2", 100, MinNoise, MaxNoise);
TH1F* fitFunctionChi2NDF    = new TH1F("fitFunctionChi2NDF", "fitFunctionChi2ND" , 500,        0,       10);
TF1*  myFitFunction         = new TF1("mygaus", "gaus", MinNoise, MaxNoise);
TF1* trimmedFunction        = new TF1("trimmedgaus","gaus", MinNoise,MaxNoise);
TF1* trimmedFunctionTwice   = new TF1("trimmedgausTwice","gaus", MinNoise,MaxNoise);


double theDetId[2]         ;
double theGaussNoise[2]    ;
double theGaussNoiseErr[2] ;
double theGaussNoiseChi2[2]; 

int noapvs=11892;
int detIDidx =0;


std::map<TString , TString> mapVoltsToRunId;
void fillMapVoltsToRunId(){
  mapVoltsToRunId["0"]  = "300";
  mapVoltsToRunId["1"]  = "20";
  mapVoltsToRunId["2"]  = "35";
  mapVoltsToRunId["3"]  = "45";
  mapVoltsToRunId["4"]  = "55";
  mapVoltsToRunId["5"]  = "65";
}


void fitProfile(TProfile* myProfile, int& fedKey) {
  //cout<<"fedKey "<<fedKey<<endl;
  
  TFile * myFile3          = new TFile("noiseControlPlots.root", "recreate");
    
  bool makeGaussPlot = true;


  for (unsigned int iApv=0; iApv<2; ++iApv) {
    
    myDist = new TH1F(Form("testDistribution_APV%i", iApv), "test distribution", 200, MinNoise, MaxNoise);
    myDisttrimmed = new TH1F(Form("testDistribution_APV%i_trimmed", iApv),  "test trimmed distribution", 100, MinNoise, MaxNoise);
 

    unsigned int firstStrip=1+(iApv*StripsPerApv);
    unsigned int lastStrip=StripsPerApv+firstStrip;

    //
    /// Performing Fit for Full Noise Distribution
    //    
    for (unsigned int iStrip=firstStrip; iStrip<lastStrip; iStrip++) 
      {      
	myDist->Fill(myProfile->GetBinContent(iStrip));
      }
    myDist->Fit(myFitFunction, "q0");
    
  
    //
    /// Trimming Fit down to +/- 3 Sigma
    //
    
    for (unsigned int iStrip=firstStrip; iStrip<lastStrip; iStrip++) 
      {
	if( (myProfile->GetBinContent(iStrip)<(myFitFunction->GetParameter(1)+3.0*myFitFunction->GetParameter(2)) ) &&  (myProfile->GetBinContent(iStrip)>(myFitFunction->GetParameter(1)-3.0*myFitFunction->GetParameter(2))) )
	  {
	    myDisttrimmed->Fill(myProfile->GetBinContent(iStrip));
	  }
	else continue;
      }
    myDisttrimmed->Fit(trimmedFunction,"q0");
    

 
    
    if (mapFedkeyToDeviceid.find(fedKey)==mapFedkeyToDeviceid.end()) 
    {
		std::cerr << "error: unknown fed key: " << fedKey << std::endl;
		return;
    } 
    

    double normChi2   = trimmedFunction->GetChisquare()/trimmedFunction->GetNDF() ;
    
    if(iApv == 0){
      theDetId[0]          = mapFedkeyToDeviceid[fedKey]*10+mapFedkeyAPV0[fedKey];
      theGaussNoise[0]     = trimmedFunction->GetParameter(1);
      theGaussNoiseErr[0]  = trimmedFunction->GetParError(1);
      theGaussNoiseChi2[0] = normChi2; 
    }
    if(iApv == 1){
      theDetId[1]          = mapFedkeyToDeviceid[fedKey]*10+mapFedkeyAPV1[fedKey];
      theGaussNoise[1]     = trimmedFunction->GetParameter(1);
      theGaussNoiseErr[1]  = trimmedFunction->GetParError(1);
      theGaussNoiseChi2[1] = normChi2; 
    }

    if((fedKey == 145764) && makeGaussPlot){
      TCanvas *c112 = new TCanvas("c112", "plots112",400,100,800,600);
      c112->SetFillColor(10);
      c112->SetFillStyle(4000);
      c112->SetBorderSize(2);

      cout << "Making Gauss plot" << endl;
      TFile *f = new TFile("gauss.root","RECREATE");   
      c112 = new TCanvas();
      c112->cd();
      myDisttrimmed->Draw();
      myDisttrimmed->Fit(trimmedFunction,"q");
	  myDisttrimmed->Write();
      c112->SaveAs("myGaussTest.png");
	  myDist->Write();
	  f->Close();
      makeGaussPlot = false;
      
    }
    
    myDist->Write();
	myDisttrimmed->Write();
    delete myDist;
    delete myDisttrimmed;
    delete myDisttrimmedTwice;
    
    fitFunctionChi2NDF->Fill(normChi2);
    //trimmedFunction->GetParameter(1); // Mean Noise
    //trimmedFunction->GetParError(1);  // Error on noise
  }


  myFile3->cd();
  fitFunctionChi2NDF->Write();
  myProfile->Write();
  myFile3->Close();
  delete myFile3;
 }


void loopProfiles(TDirectory* thisDirectory, TString runnum, TH1I* histoDetId, TH1F* histoNoiseMean, TH1F* histoNoiseError, TH1F* histoNoiseChi2) {
  
  TProfile* myProfile;
  TList*    myList     = thisDirectory->GetListOfKeys();
  TIter*    myIter     = new TIter(myList);
  TObject*  loopObject = NULL;
  int       scanResult;
  int       fedKey, laserChannel;
  char      plotType[20];
  
  
  while ( (loopObject = myIter->Next()) ) {
    // Convert TObject to a TDirectory 
    thisDirectory->GetObject(loopObject->GetTitle(), myProfile);
    if (myProfile) {
      scanResult=sscanf(myProfile->GetTitle(), "ExpertHisto_Pedestals_FedKey0x%x_LldChannel%d_%s", &fedKey, &laserChannel, plotType);
      if ((std::string(plotType)==std::string("Noise"))&&(scanResult==3)) {
	//Pedestals
	// std::cout << plotType << "  " << myProfile->GetTitle() << std::endl; // debug
	if(detIDidx%1000==0) cout<<detIDidx<<endl;
	detIDidx++;
	fitProfile(myProfile, fedKey);
	//cout << "fill " << detIDidx << "  " <<  theDetId[0] << endl;
	histoDetId->SetBinContent(      detIDidx,  theDetId[0]          );
	histoNoiseMean->SetBinContent(  detIDidx,  theGaussNoise[0]     );
	histoNoiseError->SetBinContent( detIDidx,  theGaussNoiseErr[0]  );
	histoNoiseChi2->SetBinContent(  detIDidx,  theGaussNoiseChi2[0] );
	detIDidx++;
	//cout << "fill " << detIDidx << " " << theDetId[1] << endl;
	histoDetId->SetBinContent(      detIDidx,  theDetId[1]          );
	histoNoiseMean->SetBinContent(  detIDidx,  theGaussNoise[1]     );
	histoNoiseError->SetBinContent( detIDidx,  theGaussNoiseErr[1]  );
	histoNoiseChi2->SetBinContent(  detIDidx,  theGaussNoiseChi2[1] );
      }
    }
  }
  
 
  
}

void loopDirectory(TDirectory* thisDirectory, TString runnum, TH1I* histoDetId, TH1F* histoNoiseMean, TH1F* histoNoiseError, TH1F* histoNoiseChi2) {
  TList*      myList=thisDirectory->GetListOfKeys();
  TIter*      myIter=new TIter(myList);
  TObject*    loopObject = NULL;
  TDirectory* nextDirectory;
  int nSubDirectories=0;

  while ( (loopObject = myIter->Next()) ) {
    // Convert TObject to a TDirectory
	//cout<<loopObject->GetTitle()<<endl;
    thisDirectory->GetObject(loopObject->GetTitle(), nextDirectory);
    if (nextDirectory) {
      loopDirectory(nextDirectory, runnum, histoDetId, histoNoiseMean, histoNoiseError, histoNoiseChi2);
      nSubDirectories++;
    }
  }

  if (nSubDirectories==0) loopProfiles(thisDirectory, runnum, histoDetId, histoNoiseMean, histoNoiseError, histoNoiseChi2);
}

void readOneNoise(TString runnum) {


  cout << "process run " << runnum << "  corresponding to a bias voltage of " << mapVoltsToRunId[runnum] << endl;
  //TString noisefile = "rfio:////castor/cern.ch/user/c/cbarth/noiseana/TOB/SiStripCommissioningClient_00"+runnum+".root";
    
  //TString noisefile = "/opt/cmssw/Data/BIAS-SCAN-DEC-2010/tob"+mapVoltsToRunId[runnum]+".root";
  //TString noisefile = "/castor/cern.ch/user/m/msegala/"+mapVoltsToRunId[runnum]+".root";
  
  TString noisefile = "root://eoscms//eos/cms/store/group/dpg_tracker_strip/comm_tracker/Strip/RadMonitoring/NoiseBiasScan/Sep2012/TIB/TIB_203243_300.root";
  //TString noisefile = "root://eoscms//eos/cms/store/group/dpg_tracker_strip/comm_tracker/Strip/RadMonitoring/NoiseBiasScan/2017/VRRandom0/crab_NoiseScan_20170919_run303272_v1_20/171208_143531/0000/SiStripCommissioningSource_1.root";


  // const char * clientFileName = "rfio:////castor/cern.ch/user/c/cbarth/noiseana/TECm/SiStripCommissioningClient_00"+runnum+".root";
  
  
  TString theOutputName = "noise_"+mapVoltsToRunId[runnum]+"_3Sigma.root";
  TFile *   myFile2     = new TFile(theOutputName.Data(), "recreate");
  
  TH1I * histoDetId          = new TH1I("histoDetId"    , "histoDetId" , noapvs, 0.5, noapvs-0.5);
  TH1F * histoNoiseMean      = new TH1F("NoiseMean"     , "NoiseMean"  , noapvs, 0.5, noapvs-0.5);
  TH1F * histoNoiseError     = new TH1F("NoiseError"    , "NoiseError" , noapvs, 0.5, noapvs-0.5);
  TH1F * histoNoiseChi2      = new TH1F("NoiseChi2"     , "NoiseChi2"  , noapvs, 0.5, noapvs-0.5);
  
  //cout << noisefile << endl;
  TFile * myFile = TFile::Open(noisefile);

    //  TFile * myFile = new TFile(clientFileName);
  //myFile->cd();
  // myFile = new TFile("TIBClient.root");
  //  cout << " noisefile name " << clientFileName << endl;
  
  //TDirectory* baseDirectory=myFile->GetDirectory("/DQMData/Collate/SiStrip/ControlView/");
  myFile->cd("/DQMData/SiStrip/ControlView");
  TDirectory* baseDirectory= gDirectory;
  if(!baseDirectory) {cerr<<"Did not found the directory"<<endl; return;}
  loopDirectory(baseDirectory, runnum, histoDetId, histoNoiseMean, histoNoiseError, histoNoiseChi2); 
    
  cout << "finished" << endl;
  // myFile2->Close();
  myFile2->cd();
  cout << " histoDetId title " << histoDetId->GetTitle() << endl;
  histoDetId->Write();
  cout << "wrote histo det id " << endl;
  histoNoiseMean->Write();
  cout << "wrote histo noisemean" << endl;
  histoNoiseError->Write();
  cout << " wrote his error " << endl;
  histoNoiseChi2->Write();
  cout << " wrote his chi2 " << endl;
  
  myFile2->Close();
  cout << "closed fout" << endl;

  //myFile->Close();
  //cout << "closed fin" << endl;

  //  delete histoDetId;
  //  delete histoNoiseMean;
  //  delete histoNoiseError;
  //  delete histoNoiseChi2;
  detIDidx=0; 
  cout << "deleted objects " << endl;
}

void readNoise() {
  

  fillMapVoltsToRunId();
  loadMapFedkeyToDeviceid("fedkeys.txt");

  cout << "start processing" <<endl;

  //readOneNoise("134116");
  //readOneNoise("134180");

  readOneNoise("0");


}
