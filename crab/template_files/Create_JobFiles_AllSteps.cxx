/* BASH COLORS */
#define RST   "[0m"
#define KRED  "[31m"
#define KGRN  "[32m"
#define KYEL  "[33m"
#define KBLU  "[34m"
#define KMAG  "[35m"
#define KCYN  "[36m"
#define KWHT  "[37m"
#define FRED(x) KRED x RST
#define FGRN(x) KGRN x RST
#define FYEL(x) KYEL x RST
#define FBLU(x) KBLU x RST
#define FMAG(x) KMAG x RST
#define FCYN(x) KCYN x RST
#define FWHT(x) KWHT x RST
#define BOLD(x) "[1m" x RST
#define UNDL(x) "[4m" x RST

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TH1F.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <TLorentzVector.h>
#include "TTree.h"
#include "TObjString.h"
#include "TSystem.h"
#include "TString.h"
#include "TColor.h"
#include "TCut.h"
#include "TLegend.h"
#include "TLine.h"
#include "THStack.h"
#include "TString.h"
#include "TLegend.h"
#include "TRandom.h"
#include "TLatex.h"
#include "TGraphErrors.h"
#include "TGraphAsymmErrors.h"
#include "TObject.h"
#include "TRandom3.h"
#include "TRandom1.h"
#include "TObjArray.h"
#include "TF1.h"
#include "TLegendEntry.h"
#include "TGaxis.h"
#include "TLeaf.h"
#include "TFractionFitter.h"
#include "TVirtualFitter.h"
#include "TFitResultPtr.h"
#include "TFitResult.h"

#include <iostream>
#include <cstdlib>
#include <iostream>
#include <map>
#include <string>
#include <cmath>
#include <sstream>
#include <fstream>

#include "TMVA/Tools.h"
#include "TMVA/Factory.h"
#include "TMVA/Reader.h"
#include "TMVA/MethodCuts.h"
#include "TMVA/Config.h"

#include <cassert> 	//Can be used to terminate program if argument is not true. Ex : assert(test > 0 && "Error message");
#include <sys/stat.h> // to be able to use mkdir

using namespace std;

//Convert a float into a TString
TString Convert_Number_To_TString(float number)
{
	stringstream ss;
	ss << number;
	TString ts = ss.str();
	return ts;
}

//Convert a TString into a float
float Convert_TString_To_Number(TString ts)
{
	float number = 0;
	string s = ts.Data();
	stringstream ss(s);
	ss >> number;
	return number;
}

//Use stat function (from library sys/stat) to check if a file exists
bool Check_File_Existence(const TString& name)
{
  struct stat buffer;
  return (stat (name.Data(), &buffer) == 0); //true if file exists
}

void Create_all_cfg_files(vector<TString> step_list, TString date, TString run)
{
	TString step_file_name = "./steps_" + date + "_" + run + ".txt";
	ifstream file_step(step_file_name.Data()) ;
	ifstream file_cfg_template("computeNoiseFromRaw_cfg_template.py");

	if(!Check_File_Existence(step_file_name) ) {cout<<BOLD(FRED("File "<<step_file_name<<" not found ! Abort"))<<endl;}
	if(!Check_File_Existence("computeNoiseFromRaw_cfg_template.py") ) {cout<<BOLD(FRED("File computeNoiseFromRaw_cfg_template.py not found ! Abort"))<<endl;}

	for(int istep=0; istep<step_list.size(); istep++)
	{
		//Get back to beginning of file
		file_step.clear();
		file_step.seekg(0, ios::beg);

		TString filename = "./computeNoiseFromRaw_cfg_"+step_list[istep]+".py";

		TString cmd_tmp = "cp ./computeNoiseFromRaw_cfg_template.py " + filename;
		system(cmd_tmp.Data());

		ofstream file_cfg_step(filename.Data());

		string line;
		getline(file_step,line);

		double index = 0, timestamp = 0, run = 0, evtid_begin = 0, evtid_end = 0, HV = 0, nofevt = 0;

		int iter = 0;

		while(HV != Convert_TString_To_Number(step_list[istep]) )
	    {
			getline(file_step,line);
	        std::istringstream iss(line);
	        iss >> index >> timestamp >> run >> evtid_begin >> HV >> nofevt;

			// cout << index <<" "<< timestamp << " " << run <<" "<< evtid_begin <<" "<< HV <<endl;


			getline(file_step,line);
			std::istringstream iss2(line);
			iss2 >> index >> timestamp >> run >> evtid_end >> HV >> nofevt;

			// cout << index <<" "<< timestamp << " " << run <<" "<< evtid_end <<" "<< HV <<endl<<endl;

			iter++;
			if(iter>500)
			{
				cout<<FMAG("Step "<<step_list[istep]<<"V not found in step file -- Ignore !")<<endl;

				break;
			}

			// if(iter > 500) {cout<<"Line "<<__LINE__<<" : "<<FRED("Warning : stuck in this while loop ? Abort")<<endl; return;}
	    }

		iter = 0;
		while(getline(file_cfg_template, line))
		{
			TString ts = line;

			if(ts.Contains("eventsToProcess") )
			{
				int index = ts.Index("'");
				ts.Remove(index);
				ts+= "'" + Convert_Number_To_TString(run) + ":" + Convert_Number_To_TString(evtid_begin) + "-" + Convert_Number_To_TString(run) + ":" + Convert_Number_To_TString(evtid_end) + "')";
			}

			file_cfg_step<<ts<<endl;

			// eventsToProcess = cms.untracked.VEventRange('303272:61762-303272:81449')

			iter++; if(iter > 500) {cout<<"Line "<<__LINE__<<" : "<<FRED("Warning : stuck in this while loop ? Abort")<<endl; return;}
		}

		file_cfg_step.close();
	}

	file_cfg_template.close();
	file_step.close();
}


void Create_all_crab_files(vector<TString> step_list, TString date, TString run, TString version)
{
	TString step_file_name = "./steps_" + date + "_" + run + ".txt";
	ifstream file_step(step_file_name.Data()) ;

	TString crab_template_name = "./crab3_" + date + "_" + run + "_template.py";
	ifstream file_crab_template(crab_template_name.Data() );

	if(!Check_File_Existence(step_file_name) ) {cout<<BOLD(FRED("File "<<step_file_name<<" not found ! Abort"))<<endl;}
	if(!Check_File_Existence(crab_template_name) ) {cout<<BOLD(FRED("File "<<crab_template_name<<" not found ! Abort"))<<endl;}


	for(int istep=0; istep<step_list.size(); istep++)
	{
		//Get back to beginning of file
		file_step.clear();
		file_step.seekg(0, ios::beg);

		TString filename = "./crab3_20170919_303272_"+step_list[istep]+".py";

		TString cmd_tmp = "cp ./crab3_"+date +"_"+run+"_template.py " + filename;
		system(cmd_tmp.Data());

		ofstream file_crab_step(filename.Data());

		string line;
		getline(file_step,line);

		double index = 0, timestamp = 0, run_begin = 0, run_end = 0, evtid = 0, HV = 0, nofevt = 0;
		getline(file_step,line);
		std::istringstream iss(line);
		iss >> index >> timestamp >> run_begin >> evtid >> HV >> nofevt;
		// cout << index <<" "<< timestamp << " " << run_begin <<" "<< evtid <<" "<< HV <<endl;

		int iter = 0;
		while( getline(file_step, line) )
	    {
			std::istringstream iss2(line);
			iss2 >> index >> timestamp >> run_end >> evtid >> HV >> nofevt;

			// cout << index <<" "<< timestamp << " " << run_end <<" "<< evtid <<" "<< HV <<endl<<endl;

			iter++; if(iter > 500) {cout<<"Line "<<__LINE__<<" : "<<FRED("Warning : stuck in this while loop ? Abort")<<endl; return;}
	    }

		iter = 0;
		while(getline(file_crab_template, line))
		{
			TString ts = line;

			if(ts.Contains("requestName") )
			{
				int index = ts.Index("'");
				ts.Remove(index);
				ts+= "'NoiseScan_" + date + "_run" + run + "_" + version;
			}
			else if(ts.Contains("psetName") )
			{
				int index = ts.Index("'");
				ts.Remove(index);
				ts+= "'computeNoiseFromRaw_cfg_" + step_list[istep]  + ".py'";
			}
			else if(ts.Contains("runRange") )
			{
				int index = ts.Index("'");
				ts.Remove(index);
				ts+= "'" + Convert_Number_To_TString(run_begin) + "," + Convert_Number_To_TString(run_end) + "'";
			}

			file_crab_step<<ts<<endl;

			// eventsToProcess = cms.untracked.VEventRange('303272:61762-303272:81449')

			iter++; if(iter > 500) {cout<<"Line "<<__LINE__<<" : "<<FRED("Warning : stuck in this while loop ? Abort")<<endl; return;}
		}

		file_crab_step.close();
	}

	file_crab_template.close();
	file_step.close();
}


int main()
{
	vector<TString> step_list;
	step_list.push_back("10");
	step_list.push_back("20");
	step_list.push_back("30");
	step_list.push_back("40");
	step_list.push_back("50");
	step_list.push_back("60");
	step_list.push_back("70");
	step_list.push_back("80");
	step_list.push_back("90");
	step_list.push_back("100");
	step_list.push_back("110");
	step_list.push_back("120");
	step_list.push_back("130");
	step_list.push_back("140");
	step_list.push_back("150");
	step_list.push_back("160");
	step_list.push_back("170");
	step_list.push_back("180");
	step_list.push_back("190");
	step_list.push_back("200");
	step_list.push_back("210");
	step_list.push_back("225");
	step_list.push_back("240");
	step_list.push_back("255");
	step_list.push_back("270");
	step_list.push_back("285");

	TString date = "20170919", run = "303272", version = "v1";


	Create_all_cfg_files(step_list, date, run);
	Create_all_crab_files(step_list, date, run, version);

	return 0;
}
