/**
Nicolas Tonon, IPHC
12/2017
*/

#ifndef _helper_h_
#define _helper_h_

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
#include "TProfile.h"
#include "TCut.h"
#include "TLegend.h"
#include "TIterator.h"
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
#include <iomanip>
#include <cstdlib>
#include <iostream>
#include <map>
#include <string>
#include <cmath>
#include <sstream>
#include <fstream>

#include <cassert> 	//Can be used to terminate program if argument is not true. Ex : assert(test > 0 && "Error message");
#include <sys/stat.h> // to be able to use mkdir

#include "mapFedkeyToDetid.h"
#include "tdrstyle.C"




// ------------------------------
//  ######   #######  ##     ## ##     ##  #######  ##    ##    ######## ##     ## ##    ##  ######
// ##    ## ##     ## ###   ### ###   ### ##     ## ###   ##    ##       ##     ## ###   ## ##    ##
// ##       ##     ## #### #### #### #### ##     ## ####  ##    ##       ##     ## ####  ## ##
// ##       ##     ## ## ### ## ## ### ## ##     ## ## ## ##    ######   ##     ## ## ## ## ##
// ##       ##     ## ##     ## ##     ## ##     ## ##  ####    ##       ##     ## ##  #### ##
// ##    ## ##     ## ##     ## ##     ## ##     ## ##   ###    ##       ##     ## ##   ### ##    ##
//  ######   #######  ##     ## ##     ##  #######  ##    ##    ##        #######  ##    ##  ######
// ------------------------------


//Convert a double into a TString
// precision --> can choose if TString how many digits the TString should display
TString Convert_Number_To_TString(double number, int precision=20)
{
	stringstream ss;
	ss << std::setprecision(precision) << number;
	TString ts = ss.str();
	return ts;
}

//Convert a TString into a double
double Convert_TString_To_Number(TString ts)
{
	double number = 0;
	string s = ts.Data();
	stringstream ss(s);
	ss >> number;
	return number;
}


//Convert a Hexadecimal TString into an unsigned long
unsigned long Convert_Hexa_To_UnsignedLong(TString hex_TString)
{
	return std::strtoul(hex_TString.Data(), 0, 16);
}

//Convert an unsigned long into hexa TString
TString Convert_UnsignedLong_To_Hexa(unsigned long number)
{
	TString ts = "";
	stringstream ss;
	ss << std::hex << number;
	ts = ss.str();
	return ts;
}


//Use stat function (from library sys/stat) to check if a file exists
bool Check_File_Existence(const TString& name)
{
  struct stat buffer;
  return (stat (name.Data(), &buffer) == 0); //true if file exists
}






//---------------





// ------------------------------
//  ######  ########  ########  ######  #### ######## ####  ######     ######## ##     ## ##    ##  ######
// ##    ## ##     ## ##       ##    ##  ##  ##        ##  ##    ##    ##       ##     ## ###   ## ##    ##
// ##       ##     ## ##       ##        ##  ##        ##  ##          ##       ##     ## ####  ## ##
//  ######  ########  ######   ##        ##  ######    ##  ##          ######   ##     ## ## ## ## ##
//       ## ##        ##       ##        ##  ##        ##  ##          ##       ##     ## ##  #### ##
// ##    ## ##        ##       ##    ##  ##  ##        ##  ##    ##    ##       ##     ## ##   ### ##    ## ###
//  ######  ##        ########  ######  #### ##       ####  ######     ##        #######  ##    ##  ######  ###
// ------------------------------



//  ####  ##### ###### #####     #      #  ####  #####
// #        #   #      #    #    #      # #        #
//  ####    #   #####  #    #    #      #  ####    #
//      #   #   #      #####     #      #      #   #
// #    #   #   #      #         #      # #    #   #
//  ####    #   ###### #         ###### #  ####    #

//Global object, needed by most functions (to know the Vsteps on which to run)
vector<TString> step_list(0); vector<bool> step_isUsed(0);

/**
 * Fill the global vector needed throughout the codes
 * Run -- load different steps depending on run number
 */
void Fill_Step_List_Vector(TString run)
{
	if(step_list.size() != 0) {cout<<FRED("Warning : filling global vector 'step_list' multiple times ! Potentially problematic !")<<endl; step_list.resize(0);} //Vector must be filled only once !

	if(run == "303272")
	{
		step_list.push_back("10"); step_isUsed.push_back(false);
		step_list.push_back("20"); step_isUsed.push_back(false);
		step_list.push_back("30"); step_isUsed.push_back(false);
		step_list.push_back("40"); step_isUsed.push_back(false);
		step_list.push_back("50"); step_isUsed.push_back(false);
		step_list.push_back("60"); step_isUsed.push_back(false);
		step_list.push_back("70"); step_isUsed.push_back(false);
		step_list.push_back("80"); step_isUsed.push_back(false);
		step_list.push_back("90"); step_isUsed.push_back(false);
		step_list.push_back("100"); step_isUsed.push_back(false);
		step_list.push_back("110"); step_isUsed.push_back(false);
		step_list.push_back("120"); step_isUsed.push_back(false);
		step_list.push_back("130"); step_isUsed.push_back(false);
		step_list.push_back("140"); step_isUsed.push_back(false);
		step_list.push_back("150"); step_isUsed.push_back(false);
		step_list.push_back("160"); step_isUsed.push_back(false);
		step_list.push_back("170"); step_isUsed.push_back(false);
		step_list.push_back("180"); step_isUsed.push_back(false);
		step_list.push_back("190"); step_isUsed.push_back(false);
		step_list.push_back("200"); step_isUsed.push_back(false);
		step_list.push_back("210"); step_isUsed.push_back(false);
		step_list.push_back("225"); step_isUsed.push_back(false);
		step_list.push_back("240"); step_isUsed.push_back(false);
		step_list.push_back("255"); step_isUsed.push_back(false);
		step_list.push_back("270"); step_isUsed.push_back(false);
		step_list.push_back("285"); step_isUsed.push_back(false);


		step_isUsed[0] = true; //10V
		step_isUsed[1] = true; //20V
		step_isUsed[2] = true; //30V
		step_isUsed[3] = true; //40V
		step_isUsed[4] = true; //50V
		step_isUsed[5] = true; //60V
		step_isUsed[6] = true; //70V
		step_isUsed[7] = true; //80V
		step_isUsed[8] = true; //90V
		step_isUsed[9] = true; //100V
		step_isUsed[10] = true; //110V
		step_isUsed[11] = true; //120V
		step_isUsed[12] = true; //130V
		step_isUsed[13] = true; //140V
		step_isUsed[14] = true; //150V
		step_isUsed[15] = true; //160V
		step_isUsed[16] = true; //170V
		step_isUsed[17] = true; //180V
		step_isUsed[18] = true; //190V
		// step_isUsed[19] = true; //200V
		step_isUsed[20] = true; //210V
		step_isUsed[21] = true; //225V
		step_isUsed[22] = true; //240V
		step_isUsed[23] = true; //255V
		step_isUsed[24] = true; //270V
		step_isUsed[25] = true; //285V
	}
	else if(run == "203243")
	{
		step_list.push_back("30"); step_isUsed.push_back(true);
		step_list.push_back("45"); step_isUsed.push_back(true);
		step_list.push_back("60"); step_isUsed.push_back(true);
		step_list.push_back("75"); step_isUsed.push_back(true);
		step_list.push_back("90"); step_isUsed.push_back(true);
		step_list.push_back("105"); step_isUsed.push_back(true);
		step_list.push_back("120"); step_isUsed.push_back(true);
		step_list.push_back("135"); step_isUsed.push_back(true);
		step_list.push_back("150"); step_isUsed.push_back(true);
		step_list.push_back("165"); step_isUsed.push_back(true);
		step_list.push_back("180"); step_isUsed.push_back(true);
		step_list.push_back("195"); step_isUsed.push_back(true);
		step_list.push_back("210"); step_isUsed.push_back(true);
		step_list.push_back("225"); step_isUsed.push_back(true);
		step_list.push_back("240"); step_isUsed.push_back(true);
		step_list.push_back("250"); step_isUsed.push_back(true);
		step_list.push_back("260"); step_isUsed.push_back(true);
		step_list.push_back("275"); step_isUsed.push_back(true);
		step_list.push_back("290"); step_isUsed.push_back(true);
		step_list.push_back("300"); step_isUsed.push_back(true);
		step_list.push_back("325"); step_isUsed.push_back(true);
		step_list.push_back("350"); step_isUsed.push_back(true);
	}
	else {cout<<FRED("Wrong run number ? Abort")<<endl;}

	return;
}



 // #####  ######   ##   #####      ####  #    # #####      ####  #    # ##### #####  #    # #####
 // #    # #       #  #  #    #    #    # ##  ## #    #    #    # #    #   #   #    # #    #   #
 // #    # #####  #    # #    #    #      # ## # #    #    #    # #    #   #   #    # #    #   #
 // #####  #      ###### #    #    #      #    # #    #    #    # #    #   #   #####  #    #   #
 // #   #  #      #    # #    #    #    # #    # #    #    #    # #    #   #   #      #    #   #
 // #    # ###### #    # #####      ####  #    # #####      ####   ####    #   #       ####    #

/**
 * Executes bash command and returns the output as a Tstring
 */
TString GetStdoutFromCommand(TString cmd_ts)
{
	string output = "";
	FILE * stream;
	const int max_buffer = 256;
	char buffer[max_buffer]; //Create buffer
	string cmd = cmd_ts.Data();
	cmd.append(" 2>&1");

	stream = popen(cmd.c_str(), "r"); //Open read-only stream, run command
	if (stream)
	{
		while (!feof(stream))
		if (fgets(buffer, max_buffer, stream) != NULL) output.append(buffer); //Get the output
		pclose(stream);
	}

	output.erase(std::remove(output.begin(), output.end(), '\n'), output.end()); //Remove the "end of line" character

	TString ts_output(output); //Convert string to TString

	return ts_output;
}







// ######  ####   ####     #####    ##   ##### #    #
// #      #    # #         #    #  #  #    #   #    #
// #####  #    #  ####     #    # #    #   #   ######
// #      #    #      #    #####  ######   #   #    #
// #      #    # #    #    #      #    #   #   #    #
// ######  ####   ####     #      #    #   #   #    #


/**
 * C++ code to get file path for given run and Vstep (looking at EOS ls output)
 * @param  path_run -- basic path corresponding to the run (in which to look for)
 * @param  run      -- run number
 * @param  step     -- voltage step
 * @return          -- return the path of .root file
 */
TString Find_Path_EOS_File(TString path_run, TString run, TString step)
{
	Fill_Step_List_Vector(run);

	bool debug = false;

	int counter = 0; //Make sure while loops are not infinite

	TString path_file = path_run, command = "", read_output = "";

	//Reads content of "path_run" dir. -- Will look up to the 60 first lines to look for desired Vstep
	for (int iline = 1; iline < 60; iline++)
	{
		command = "eos ls " + path_file + " | sed -n '" + Convert_Number_To_TString(iline) + "p'"; //Look to last line of printed output
		read_output = GetStdoutFromCommand(command); //Get command output

		//If Vstep found
		if(read_output.Contains("_" + step) )
		{
			//-- Complicated way of making sure that the "step" pattern is really placed at the end of the path name (not inside the date, ...)
			int step_string_size = ((string) step).size();
			TString ts_tmp = read_output;
			ts_tmp.Remove(0, ((string) read_output).size() - ((string) step).size() -1 ); //Just keep the last characters (e.g. "_150")
			if(ts_tmp != "_" + step) {continue;}

			path_file+= "/" + read_output; //If vstep found, add to path

			if(debug) cout<<"path_file "<<path_file<<endl;
			break;
		}
	}

	//Then, add directories recursively to final path, until .root file is found
	while(!path_file.Contains(".root"))
	{
		bool isFound = false; //true if root file has been found -> exit loops

		// command = "eos ls " + path_file + "| tail -1";
		command = "eos ls " + path_file + " | tail -1";

		// cout<<FYEL(""+command+"")<<endl; //Print command for check

		read_output = GetStdoutFromCommand(command);

		if(read_output.Contains(".root") )
		{
			command = "eos ls " + path_file + " | wc -l";
			read_output = GetStdoutFromCommand(command);

			if(read_output == "1")
			{
				command = "eos ls " + path_file;
				read_output = GetStdoutFromCommand(command);

				isFound = true;
			}
			else
			{
				bool isFound = false;

				// {cout<<FRED("Warning : found more than 1 .root file in EOS dir. ! Will select SiStripCommissioningSource_1.root (default)")<<endl;}
				//Reads content of "path_run" dir. -- Will look up to the 60 first lines to look for desired Vstep
				for (int iline = 1; iline < 60; iline++)
				{
					// cout<<iline<<endl;

					command = "eos ls " + path_file + " | sed -n '" + Convert_Number_To_TString(iline) + "p'"; //Look to last line of printed output
					read_output = GetStdoutFromCommand(command); //Get command output

					if(debug) cout<<read_output<<endl;

					//If Vstep found
					if(read_output.Contains("_" + step + ".root") )
					{
						//-- Complicated way of making sure that the "step" pattern is really placed at the end of the path name (not inside the date, ...)
						int step_string_size = ( (string) (step + ".root")).size();
						TString ts_tmp = read_output;
						ts_tmp.Remove(0, ((string) read_output).size() - step_string_size - 1 ); //Just keep the last characters (e.g. "_150")
						if(debug) cout<<ts_tmp<<endl;
						if(ts_tmp != "_" + step + ".root") {continue;}

						isFound = true; break; //Break for loop (path found)
					}
				}
			}

			if(debug) cout<<"path_file "<<path_file<<endl;
		} //ROOT file found

		if(read_output != "") path_file+= "/" + read_output;
		if(isFound) {break;} //Break while loop (file found)

		counter++; if(counter>80) {cout<<FRED("Infinite loop (not finding EOS path of .root file) -- Abort")<<endl; return "";}
	}


	if(debug) cout<<"path_file "<<path_file<<endl;

	return path_file;
}








/*
 ██████  ██████  ██████  ██████  ███████  ██████ ████████     ██ ██      ███████  █████  ██   ██
██      ██    ██ ██   ██ ██   ██ ██      ██         ██        ██ ██      ██      ██   ██ ██  ██
██      ██    ██ ██████  ██████  █████   ██         ██        ██ ██      █████   ███████ █████
██      ██    ██ ██   ██ ██   ██ ██      ██         ██        ██ ██      ██      ██   ██ ██  ██
 ██████  ██████  ██   ██ ██   ██ ███████  ██████    ██        ██ ███████ ███████ ██   ██ ██   ██
*/



//////////////////////////////////////////////////////////////////////////////////////////////////

// Leackage current corrections
//------------------------------

int CorrectGraphForLeakageCurrent(TGraph* g, double detid, TFile* f)
{
	// Get correction function

	if(!f) {return 0;}


	TF1* func = (TF1*) f->Get( ("fit_" +Convert_Number_To_TString(detid)).Data() );

	//WARNING on missing Leakage correction, only if module is in list of monitored detectors
	if(!func)
	{
		bool isInList = false;

		ifstream det_file;
		TString ts = Convert_Number_To_TString(detid);
		if(ts.Contains("36912")) {det_file.open("detid_lists/TIB_detit_list.txt");}
		else if(ts.Contains("43628")) {det_file.open("detid_lists/TOB_detit_list.txt");}
		else if(ts.Contains("47014")) {det_file.open("detid_lists/TEC_detit_list.txt");}
		//else {cout<<"Corresponding detector list not found ! Detid = "<<ts<<endl; return 0;}
		//cout<<"detID = "<<detid<<endl;

		string line; double id=0;
		while(getline(det_file,line))
		{
			std::istringstream iss(line);
		    iss >> id;
		    cout<<id<<endl;
		    if(detid == id || detid/10 == id || detid == id/10) {isInList = true;}
		}

		// if(isInList) 
		{cout<<FRED("No leakage current correction for detid : ")<<std::setprecision(11)<<detid<<endl;}
		return 0;
	}

	// Correct points
	double x,y;
	for(int i=0; i<g->GetN(); i++)
	{
	g->GetPoint(i, x, y);
	g->SetPoint(i, x-func->Eval(x), y);
	}

	return 1;
}

int CorrectGraphForLeakageCurrent(TGraph* g, double detid, TString output_name)
{
	// Get correction function
	TString filename="LeakCurCorr"+output_name+".root";
	//string filepath="/afs/cern.ch/work/j/jlagram/public/SiStripRadMonitoring/LeakageCurrentCorrections/Corrections/"+filename;

	TString filepath="/afs/cern.ch/user/n/ntonon/public/tracker_aging/CMSSW_9_2_10/src/SiStripRadMonitoring/LeakageCurrentBiasScan/Analysis/LeakCurCorr_files/"+filename;

	if (filename.Contains("170000") ) {return 0;} //No leakage correction for this old run, neglected
	if(!Check_File_Existence(filepath)) {cout<<BOLD(FRED("No leakage current correction file : "))<<filepath<<endl; return 0;}

	TFile* f = new TFile(filepath, "read");

	int out = CorrectGraphForLeakageCurrent(g, detid, f);

	f->Close();
	f->Delete();

	return out;
}





#endif

