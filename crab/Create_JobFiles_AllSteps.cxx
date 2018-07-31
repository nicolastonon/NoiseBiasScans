/**
Nicolas Tonon, IPHC
12/2017
*/

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

#include "../Helper_Functions.h"

using namespace std;


//-------------------------
 //   ####  ######  ####     ###### # #      ######  ####
 //  #    # #      #    #    #      # #      #      #
 //  #      #####  #         #####  # #      #####   ####
 //  #      #      #  ###    #      # #      #           #
 //  #    # #      #    #    #      # #      #      #    #
 //   ####  #       ####     #      # ###### ######  ####
 //-------------------------

/**
 * Create config .py files for all Vsteps, for given run/date
 */
void Create_all_cfg_files(TString date, TString stepfile_run, vector<TString> v_datasets, bool get_list_of_datafiles_from_textfile)
{
	mkdir( ("run_"+stepfile_run+"/").Data(), 0777); //Create directory if inexistant


	TString step_file_name = "./Vstep_lists/steps_" + date + "_" + stepfile_run + ".txt";
	if(!Check_File_Existence(step_file_name) ) {cout<<FRED("Missing Vstep file "<<step_file_name<<" !")<<endl; return;}
	ifstream file_step(step_file_name.Data()) ;
	ifstream file_cfg_template("computeNoiseFromRaw_cfg_template.py");

	if(!Check_File_Existence(step_file_name) ) {cout<<BOLD(FRED("File "<<step_file_name<<" not found ! Abort"))<<endl;}
	if(!Check_File_Existence("computeNoiseFromRaw_cfg_template.py") ) {cout<<BOLD(FRED("File computeNoiseFromRaw_cfg_template.py not found ! Abort"))<<endl;}

	for(int istep=0; istep<step_list.size(); istep++)
	{
		if(!step_isUsed[istep]) {continue;}

		//Get back to beginning of file
		file_step.clear();
		file_step.seekg(0, ios::beg);

		//Get back to beginning of file
		file_cfg_template.clear();
		file_cfg_template.seekg(0, ios::beg);

		TString filename = "./run_"+stepfile_run+"/computeNoiseFromRaw_cfg_"+step_list[istep]+".py";

		TString cmd_tmp = "cp ./computeNoiseFromRaw_cfg_template.py " + filename;
		system(cmd_tmp.Data());

		ofstream file_cfg_step(filename.Data());

		string line;
		getline(file_step,line); //Read first line (contains titles of columns)

		double index = 0, timestamp = 0, run = 0, evtid_begin = 0, evtid_end = 0, HV = 0, nofevt = 0;

		int iter = 0;

		//Read step file, just to find nof events corresponding to begin and end of Vstep
		while(HV != Convert_TString_To_Number(step_list[istep]) )
	    {
			getline(file_step,line);
	        std::istringstream iss(line);
	        iss >> index >> timestamp >> run >> evtid_begin >> HV >> nofevt;

			// cout<<"--- Looking for step "<<step_list[istep]<<endl;
			// cout<<"---> HV = "<<HV<<endl;
			// cout << index <<" "<< timestamp << " " << run <<" "<< evtid_begin <<" "<< HV <<endl;


			getline(file_step,line);
			std::istringstream iss2(line);
			iss2 >> index >> timestamp >> run >> evtid_end >> HV >> nofevt;

			// cout << index <<" "<< timestamp << " " << run <<" "<< evtid_end <<" "<< HV <<endl<<endl;

			iter++;
			if(iter>200)
			{
				cout<<FMAG("Step "<<step_list[istep]<<"V not found in step file -- Ignore !")<<endl;
				cout<<"Check step file : if step does exist, make sure that the 1rst line of file contains titles"<<endl;


				evtid_begin = evtid_end = 0;

				break;
			}

			// if(iter > 500) {cout<<"Line "<<__LINE__<<" : "<<FRED("Warning : stuck in this while loop ? Abort")<<endl; return;}
		}

		iter = 0;
		//Open template cfg file, copy it and modify some lines
		while(getline(file_cfg_template, line))
		{
			if(evtid_end == 0) {break;} //Vstep not found, don't fill file

			TString ts = line;

			if(ts.Contains("eventsToProcess") ) //Line to modify (event numbers)
			{
				int index = ts.Index("'");
				ts.Remove(index);
				ts+= "'" + Convert_Number_To_TString(run) + ":" + Convert_Number_To_TString(evtid_begin) + "-" + Convert_Number_To_TString(run) + ":" + Convert_Number_To_TString(evtid_end) + "')";
			}
			//Line to replace (list of files)
			//Read .txt file containing all input files
			else if(get_list_of_datafiles_from_textfile && ts.Contains("list = []") )
			{
				int index = ts.Index("[");
				ts.Remove(index); ts+= "[";

				for(int idataset=0; idataset<v_datasets.size(); idataset++)
				{
					if(idataset>0 ) {ts+= ",";} //If many datasets, need to concatenate them with a simple comma

					TString listfile_name = "list_files/run_"+Convert_Number_To_TString(run)+"/"+v_datasets[idataset]+".txt";
					if(!Check_File_Existence(listfile_name) )
					{
						cout<<BOLD(FRED("File "<<listfile_name<<" not found !"))<<endl;
					}

					ifstream file_list( listfile_name.Data() );

					while(getline(file_list, line) )
					{
						ts+= line;
					}

					file_list.close();
				}

				ts+= "]";
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





/*
███████ ██    ██ ██████  ███    ███ ██ ████████     ████████  ██████      ██████   █████  ████████  ██████ ██   ██
██      ██    ██ ██   ██ ████  ████ ██    ██           ██    ██    ██     ██   ██ ██   ██    ██    ██      ██   ██
███████ ██    ██ ██████  ██ ████ ██ ██    ██           ██    ██    ██     ██████  ███████    ██    ██      ███████
     ██ ██    ██ ██   ██ ██  ██  ██ ██    ██           ██    ██    ██     ██   ██ ██   ██    ██    ██      ██   ██
███████  ██████  ██████  ██      ██ ██    ██           ██     ██████      ██████  ██   ██    ██     ██████ ██   ██
*/


void Submit_All_To_Batch(TString path_cfg_files, TString run, TString outputdir)
{
	if(path_cfg_files == "")
	{
		cout<<BOLD(FRED("Need to specify relative path of cfg files ! Abort"))<<endl;
		cout<<"-- Ex : ./Create_JobFiles_AllSteps.exe ."<<endl;
	}

	cout<<FYEL("--- Going to submit all jobs to CERN's batch")<<endl;
	cout<<FYEL("#Make sure you have run the 'voms' command & copied the proxy to your home")<<endl;
	cout<<FYEL("#Make sure you have configured 'cmsRun_batch_eos' properly")<<endl;

	path_cfg_files.Remove(TString::kTrailing, '/'); //Remove '/' char at end of TString if present

	//Create proxy
	TString cmd = "voms-proxy-init --voms cms --valid 168:00";
	system(cmd.Data());

	//Get proxy name
	cmd = "ls -l /tmp/x509up_u* | grep ntonon";
	TString proxy_name = GetStdoutFromCommand(cmd);
	int index = proxy_name.Index("x509");
	proxy_name.Remove(0, index); //Keep only the proxy string
	cout<<"#proxy name : "<<proxy_name<<endl;

	//Copy proxy locally
	cmd = "cp /tmp/" + proxy_name + " ~";
	system(cmd.Data());

	//For each Vstep, send job to batch
	for(int istep=0; istep<step_list.size(); istep++)
	{
		if(!step_isUsed[istep]) {continue;} //If step doesn't exist for this run

		cout<<endl<<step_list[istep]<< " V :"<<endl;

		if(Find_Path_EOS_File(outputdir, run, step_list[istep]) != "")
		{
			cout<<"Root file already exists ; not resubmitting this job !"<<endl; continue;
		}

		//Cp cfg file locally
		cmd = "cp " + path_cfg_files + "/computeNoiseFromRaw_cfg_"+step_list[istep] + ".py .";
		system(cmd.Data());

		//Send job to batch
		cmd = "bsub -q8nh cmsRun_batch_eos computeNoiseFromRaw_cfg_"+step_list[istep]+".py " + proxy_name + " SiStripCommissioningSource_"+step_list[istep]+".root " + outputdir;
		system(cmd.Data());
	}

	return;
}




/*

//------------------------------------------
 //  ####  #####    ##   #####     ###### # #      ######  ####
 // #    # #    #  #  #  #    #    #      # #      #      #
 // #      #    # #    # #####     #####  # #      #####   ####
 // #      #####  ###### #    #    #      # #      #           #
 // #    # #   #  #    # #    #    #      # #      #      #    #
 //  ####  #    # #    # #####     #      # ###### ######  ####
 //------------------------------------------

//Create all the crab3 files for all Vsteps, foor given run/date
void Create_all_crab_files(TString date, TString run, TString version)
{
	mkdir( ("run_"+run+"/").Data(), 0777); //Create directory if inexistant

	TString step_file_name = "./Vstep_lists/steps_" + date + "_" + run + ".txt";
	ifstream file_step(step_file_name.Data()) ;

	TString crab_template_name = "./crab3_" + date + "_" + run + "_template.py";
	ifstream file_crab_template(crab_template_name.Data() );

	if(!Check_File_Existence(step_file_name) ) {cout<<BOLD(FRED("File "<<step_file_name<<" not found ! Abort"))<<endl;}
	if(!Check_File_Existence(crab_template_name) ) {cout<<BOLD(FRED("File "<<crab_template_name<<" not found ! Abort"))<<endl;}


	for(int istep=0; istep<step_list.size(); istep++)
	{
		if(!step_isUsed[istep]) {continue;}

		//Get back to beginning of file
		file_step.clear();
		file_step.seekg(0, ios::beg);

		//Get back to beginning of file
		file_crab_template.clear();
		file_crab_template.seekg(0, ios::beg);

		TString filename = "./run_"+run+"/crab3_20170919_303272_"+step_list[istep]+".py";

		TString cmd_tmp = "cp " + crab_template_name + " " + filename;
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
				ts+= "'NoiseScan_" + date + "_run" + run + "_" + version + "_" + step_list[istep] +  "'";
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








//------------------------------------------
 //  ####  #    # #####  #    # # #####
 // #      #    # #    # ##  ## #   #
 //  ####  #    # #####  # ## # #   #
 //      # #    # #    # #    # #   #
 // #    # #    # #    # #    # #   #
 //  ####   ####  #####  #    # #   #
//------------------------------------------


void Submit_All_toCrab(TString path)
{
	cout<<FBLU("--- To submit jobs : ./Create_JobFiles_AllSteps.exe [path_to_crab_files]")<<endl;

	path.Remove(TString::kTrailing, '/'); //Remove '/' char at end of TString if present

	for(int istep=0; istep<step_list.size(); istep++)
	{
		if(!step_isUsed[istep]) {continue;}

		cout<<FYEL("--- Submitting job "<<step_list[istep]<<"V to crab")<<endl;
		TString crabfile_name = "crab3_20170919_303272_"+step_list[istep]+".py";
		TString configfile_name = "computeNoiseFromRaw_cfg_"+step_list[istep]+".py";
		if(!Check_File_Existence(path+"/"+crabfile_name) ) {cout<<FRED("Crab file "<<path<<"/"<<crabfile_name<<" not found !")<<endl; continue;}
		if(!Check_File_Existence(path+"/"+configfile_name) ) {cout<<FRED("Crab file "<<path<<"/"<<configfile_name<<" not found !")<<endl; continue;}

		TString cmd = "cp "+ path+"/"+crabfile_name + " ."; system(cmd); //Copy locally crab file to submit
		cmd = "cp "+ path+"/"+configfile_name + " ."; system(cmd); //Copy locally cfg file to submit

		cmd = "crab submit ./" + crabfile_name; system(cmd); //Submit tmp crab file

		cmd = "rm ./" + crabfile_name + "*"; system(cmd); //Remove tmp crab file
		cmd = "rm ./" + configfile_name + "*"; system(cmd); //Remove tmp cfg file
	}
}

void Re_Submit_All_toCrab(TString path, TString date, TString run, TString version)
{
	for(int istep=0; istep<step_list.size(); istep++)
	{
		if(!step_isUsed[istep]) {continue;}

		cout<<FYEL("--- Re-submitting jobs "<<step_list[istep]<<"V to crab")<<endl;

		TString cmd = "crab resubmit ./crab_projects/crab_NoiseScan_"+ date + "_run" + run + "_" +  version + "_" + step_list[istep];
		system(cmd);
	}
}*/




//------------------------------------------
// ##     ##    ###    #### ##    ##
// ###   ###   ## ##    ##  ###   ##
// #### ####  ##   ##   ##  ####  ##
// ## ### ## ##     ##  ##  ## ## ##
// ##     ## #########  ##  ##  ####
// ##     ## ##     ##  ##  ##   ###
// ##     ## ##     ## #### ##    ##
//------------------------------------------


int main(int argc, char **argv)
{
	TString path_from_command = "";
	if(argc == 2) //If an arg was given at command line
    {
        path_from_command = argv[1];
    }

	//True --> will look for .txt file containing all the dataset files (needed if want to run on dataset interactively rather than using crab !)
	bool get_list_of_datafiles_from_textfile = true;

	TString date, run, version, outputdir;

	// date = "20120921", run = "203243", version = "v1";
	// date = "20170919", run = "303272", version = "v1";
	// date = "20160914", run = "280667", version = "v1";
	date = "20180618", run = "317974", version = "v1";
	outputdir="/store/group/dpg_tracker_strip/comm_tracker/Strip/RadMonitoring/NoiseBiasScan/2018/VRRandom0to7";

	vector<TString> v_datasets;
	v_datasets.push_back("dataset0");
	v_datasets.push_back("dataset1");
	v_datasets.push_back("dataset2");
	v_datasets.push_back("dataset3");
	v_datasets.push_back("dataset4");
	v_datasets.push_back("dataset5");
	v_datasets.push_back("dataset6");
	v_datasets.push_back("dataset7");

	Fill_Step_List_Vector(run);

	Create_all_cfg_files(date, run, v_datasets, get_list_of_datafiles_from_textfile);
	// Create_all_crab_files(date, run, version);

	// Submit_All_To_Batch(path_from_command, run, outputdir);

	// Submit_All_toCrab(path_from_command);
	// Re_Submit_All_toCrab(path_from_command, date, run, version); //-- obsolete

	return 0;
}
