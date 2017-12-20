/**
Nicolas Tonon, IPHC
12/2017
*/

#include <map>

#include "Helper_Functions.h"


using namespace std;



//-------------------------------------------------------

//  ######  ######## ##    ## ##       ########    ##     ## ####  ######  ########  #######
// ##    ##    ##     ##  ##  ##       ##          ##     ##  ##  ##    ##    ##    ##     ##
// ##          ##      ####   ##       ##          ##     ##  ##  ##          ##    ##     ##
//  ######     ##       ##    ##       ######      #########  ##   ######     ##    ##     ##
//       ##    ##       ##    ##       ##          ##     ##  ##        ##    ##    ##     ##
// ##    ##    ##       ##    ##       ##          ##     ##  ##  ##    ##    ##    ##     ##
//  ######     ##       ##    ######## ########    ##     ## ####  ######     ##     #######
//-------------------------------------------------------

void Style_Control_Histo(TH1F* h)
{
	h->SetMarkerStyle(8);
	h->SetMarkerSize(1.5);
	h->SetMarkerColor(1);

	h->GetXaxis()->SetTitle("Bias voltage [V]");
	h->GetXaxis()->SetTitleSize(.05);

	h->GetYaxis()->SetTitle("Noise [a.u.]");
	h->GetYaxis()->SetTitleSize(.05);
	h->GetYaxis()->SetTitleOffset(0.95);

	return;
}


void Draw_ExtraText(TCanvas* c)
{
	c->cd();

	TString cmsText     = "CMS";
	TLatex latex;
	latex.SetNDC();
	latex.SetTextAngle(0);
	latex.SetTextColor(kBlack);
	latex.SetTextFont(61);
	latex.SetTextAlign(11);
	latex.SetTextSize(0.05);
	latex.DrawLatex(c->GetLeftMargin(),0.93,cmsText);


	bool writeExtraText = false;
	TString extraText   = "Preliminary 2017";
	latex.SetTextFont(52);
	latex.SetTextSize(0.04);
	latex.DrawLatex(c->GetLeftMargin() + 0.1, 0.932, extraText);

	return;
}




//-------------------------------------------------------
//  ######  ########  ########    ###    ######## ########    ##     ##    ###    ########
// ##    ## ##     ## ##         ## ##      ##    ##          ###   ###   ## ##   ##     ##
// ##       ##     ## ##        ##   ##     ##    ##          #### ####  ##   ##  ##     ##
// ##       ########  ######   ##     ##    ##    ######      ## ### ## ##     ## ########
// ##       ##   ##   ##       #########    ##    ##          ##     ## ######### ##
// ##    ## ##    ##  ##       ##     ##    ##    ##          ##     ## ##     ## ##
//  ######  ##     ## ######## ##     ##    ##    ########    ##     ## ##     ## ##
//-------------------------------------------------------


 //   #
 //  ##      #    #  ####  ##### ###### #####
 // # #      #    # #        #   #      #    #
 //   #      #    #  ####    #   #####  #    #
 //   #      #    #      #   #   #      #####
 //   #       #  #  #    #   #   #      #
 // #####      ##    ####    #   ###### #

/**
 * For given Vstep, reads associated file containing noise infos for all det ids (from code Extract_Noise_Per_DetID.cxx) and returns a map linking each detid to its noise infos (for this Vstep)
 * @param step -- Bias voltage step
 * @param run  -- Run number
 */
map< double, vector<double> > Read_Noise_For1Step_And_Fill_Map(TString step, TString run)
{
	//Input files, produced by code "Extract_Noise_Per_DetID.cxx"
	TString filename = "./Noise_All_DetIDs_files/run_"+run+"/Noise_All_DetIDs_run"+run+"_"+step+"V.root";
	if(!Check_File_Existence(filename) ) {cout<<FRED("File "<<filename<<" not found ! Continue")<<endl;}

	TFile* f_input = TFile::Open(filename);
	TTree* t_input = (TTree*) f_input->Get("Tree");

	double detid=0, noise=0, error=0, chi2=0, pedestal_mean_err=0;

	//To read input branches
	t_input->SetBranchAddress("detid", &detid);
	t_input->SetBranchAddress("noise_mean", &noise);
	t_input->SetBranchAddress("noise_err", &error);
	t_input->SetBranchAddress("pedestal_mean_err", &pedestal_mean_err); //alternative error
	t_input->SetBranchAddress("noise_chi2", &chi2);

	map< double, vector<double> > map_detid_noise; //Will map detid <-> noise infos (for given Vstep)

	vector<double> v_tmp(4);
	//For all detids, read input file, create map : detid <-> noise infos
	for(int ientry=0; ientry<t_input->GetEntries(); ientry++)
	{
		//FIXME -- don't process all entries for now
		if(ientry>10) {break;}

		v_tmp.clear(); v_tmp.resize(4);
		detid=0, noise=0, error=0, chi2=0;

		t_input->GetEntry(ientry);

		v_tmp[0] = noise; v_tmp[1] = error; v_tmp[2] = pedestal_mean_err; v_tmp[3] = chi2;

		map_detid_noise.insert(pair< double, vector<double> > (detid, v_tmp) );
	}

	f_input->Close();

	return map_detid_noise;
}







 //   ##   #      #         #    #  ####  ##### ###### #####   ####
 //  #  #  #      #         #    # #        #   #      #    # #
 // #    # #      #         #    #  ####    #   #####  #    #  ####
 // ###### #      #         #    #      #   #   #      #####       #
 // #    # #      #          #  #  #    #   #   #      #      #    #
 // #    # ###### ######      ##    ####    #   ###### #       ####

/**
 * Call above function for each Vstep --> Fill a vector of maps (1 map per Vstep)
 * @param run -- run number
 */
vector < map< double, vector<double> > > Get_Detid_Noise_Maps_For_All_Steps(TString run)
{
	vector < map< double, vector<double> > > v_maps_allSteps( step_list.size() );

	for(int istep=0; istep<step_list.size(); istep++)
	{
		if(!step_isUsed[istep]) {continue;}

		v_maps_allSteps[istep] = Read_Noise_For1Step_And_Fill_Map(step_list[istep], run);
	}

	return v_maps_allSteps;
}







//-------------------------------------------------------
// ###### # #####    #    #  ####  #####  ###### #
// #      #   #      ##  ## #    # #    # #      #
// #####  #   #      # ## # #    # #    # #####  #
// #      #   #      #    # #    # #    # #      #
// #      #   #      #    # #    # #    # #      #
// #      #   #      #    #  ####  #####  ###### ######
//-------------------------------------------------------


/**
 * Fitting model used to fit the noise VS bias plots and extract Vfd.
 * User-defined function used to create a TF1 object
 * @param  x   -- x[0] = Bias voltage (1D histo)
 * @param  par -- array of parameters : 0 = cst, 1 = beta, 2 = vfd
 */
double Fitting_Model(double* x, double *par) //Arguments by convention
{
	double xx = x[0]; //abcissa
	double result = 0;

	if(xx <= par[2])
	{
		result = par[0] + par[1] * (1./sqrt(xx) - 1./sqrt(par[2]) );
	}
	else
	{
		result = par[0];
	}

	return result;
}











//-------------------------------------------------------
// ########  ##        #######  ########       ###    ##    ## ########     ######## #### ########
// ##     ## ##       ##     ##    ##         ## ##   ###   ## ##     ##    ##        ##     ##
// ##     ## ##       ##     ##    ##        ##   ##  ####  ## ##     ##    ##        ##     ##
// ########  ##       ##     ##    ##       ##     ## ## ## ## ##     ##    ######    ##     ##
// ##        ##       ##     ##    ##       ######### ##  #### ##     ##    ##        ##     ##
// ##        ##       ##     ##    ##       ##     ## ##   ### ##     ##    ##        ##     ##
// ##        ########  #######     ##       ##     ## ##    ## ########     ##       ####    ##
//-------------------------------------------------------



 //   #      #     #
 //  ##      #     #  ####  ##### ###### #####
 // # #      #     # #        #   #      #    #
 //   #      #     #  ####    #   #####  #    #
 //   #       #   #       #   #   #      #####
 //   #        # #   #    #   #   #      #
 // #####       #     ####    #   ###### #


/**
 * Takes as input the Noise_vs_bias histo for given detid/run, and fits it with model ; returns the Vfd param and its error, and stores a few plots for control
 * @param histo_to_fit          -- histogram noise_vs_bias to fit
 * @param counter_control_plots -- counter (don't store all control plots)
 * @param detid                 -- detid corresponding to the histo
 */
pair<double, double> Fit_Noise_VS_Bias_Histogram_And_Make_Control_Plots(TH1F* histo_to_fit, int& counter_control_plots, double detid)
{
	gStyle->SetOptFit(111);
	gStyle->SetFuncWidth(3);

	//Fitting model --- (name, fcn, xmin, xmax, npar)
	TF1* noise_fit = new TF1("myfunc", Fitting_Model, histo_to_fit->GetXaxis()->GetXmin(), histo_to_fit->GetXaxis()->GetXmax(), 3);
	noise_fit->SetParNames("Constant","#beta", "V_{FD}");
	noise_fit->SetParameters(5., 1., 100.); //FIXME -- init parameters

	histo_to_fit->Fit(noise_fit, "q"); //quiet
	// cout<<"Histo to fit : nentries = "<<histo_to_fit->GetEntries()<<endl;

	pair<double, double> result;
	result.first = noise_fit->GetParameter(2);
	result.second = noise_fit->GetParError(2);
	// cout<<endl<<"noise_fit->GetParameter(0) = "<<noise_fit->GetParameter(0)<<" / error = "<<noise_fit->GetParError(0)<<endl;
	// cout<<"noise_fit->GetParameter(1) = "<<noise_fit->GetParameter(1)<<" / error = "<<noise_fit->GetParError(1)<<endl;
	// cout<<"noise_fit->GetParameter(2) = "<<noise_fit->GetParameter(2)<<" / error = "<<noise_fit->GetParError(2)<<endl;

	if(counter_control_plots < 5 && noise_fit->GetParameter(2) > 0) //Only plot few histos, not all
	{
		TCanvas* c = new TCanvas("c", "", 1000, 800); c->cd();
		c->SetTopMargin(0.1);
		c->SetBottomMargin(0.1);

		Style_Control_Histo(histo_to_fit);

		histo_to_fit->Draw("PE"); //Markers, error bars

		Draw_ExtraText(c);

		TLegend *leg = new TLegend(0.70, 0.70, 0.90, 0.80);
		//leg->SetBorderSize(0.1);
		leg->SetTextFont(42);
		// leg->SetHeader("Noise analysis");
		leg->AddEntry(histo_to_fit, "Data", "P");
		leg->AddEntry(noise_fit, "Fit model", "l");
		leg->Draw("same");

		c->SaveAs("noiseVSbias_detid_"+Convert_Number_To_TString(detid)+".png" );

		delete leg; leg = NULL;
		delete c; c = NULL;

		counter_control_plots++;
	}

	delete noise_fit; noise_fit = NULL;

	return result;
}





 //    #                     #     #
 //   # #   #      #         #     #  ####  ##### ###### #####   ####
 //  #   #  #      #         #     # #        #   #      #    # #
 // #     # #      #         #     #  ####    #   #####  #    #  ####
 // ####### #      #          #   #       #   #   #      #####       #
 // #     # #      #           # #   #    #   #   #      #      #    #
 // #     # ###### ######       #     ####    #   ###### #       ####

/**
 * Main function. For all detids, it will collect the fit results and store the Vfd values into an output TTree
 * @param run -- run number
 */
void Produce_Noise_VS_Bias_Histograms_For_All_Detids_And_Store_Results(TString run)
{
	cout<<endl<<FYEL("#######################")<<endl;
	cout<<FYEL("--- Produce Noise VS Bias plots, Fit them, Store results and control plots")<<endl;
	cout<<FYEL("#######################")<<endl<<endl;


	//Get maps detid <-> noise infos, for all Vsteps
	vector < map< double, vector<double> > > v_maps_allSteps = Get_Detid_Noise_Maps_For_All_Steps(run); //Fill the vector of maps (1 map per Vstep)

	pair<double, double> fit_results; double detid;

	//Output file, containing Vfd results for all detids
	TFile *f_fit_results = new TFile("Fit_Results_run"+run+".root","RECREATE");
	TTree* tree = new TTree("Tree", "Fit results");
	TBranch *b_detid = tree->Branch("detid", 0, "detid/D");
	TBranch *b_Vfd = tree->Branch("Vfd", 0, "Vfd/D");
	TBranch *b_Vfd_err = tree->Branch("Vfd_err", 0, "Vfd_err/D");
	tree->SetBranchAddress("detid", &detid);
	tree->SetBranchAddress("Vfd", &fit_results.first);
	tree->SetBranchAddress("Vfd_err", &fit_results.second);

	int counter_control_plots = 0; //Produce only few control plots

	//Iterate over all the detids, taken as the list of keys stored in 1 map (e.g. the map corresponding to first Vstep)
	for(map< double, vector<double> >::iterator it = v_maps_allSteps[0].begin(); it != v_maps_allSteps[0].end(); it++)
	{
		detid = 0; fit_results.first = 0; fit_results.second = 0;

		double current_detid = it->first; //if(current_detid == 0) {cout<<__LINE__<<FRED(" : Null detid -- correct map initialization ? ")<<endl;}
		// cout<<"current_detid = "<< current_detid << endl;

		//Store noise_vs_bias histo for current detid
		// TH1F* h_noise_vs_bias_current_detid = new TH1F("", "", step_list.size(), 0, Convert_TString_To_Number(step_list[step_list.size() - 1]) );
		double xmin = 2.5, xmax = 302.5, nbins = 60;
		TH1F* h_noise_vs_bias_current_detid = new TH1F("", "", nbins, xmin, xmax); //CHANGED -- 26 steps in total


		double ymin = 999; //There are empty bins messing with y-axis --> will show only bins with y > ymin instead

		//For each detid, we loop on all the maps (<-> all the Vsteps) and look for noise values for all Vsteps
		for(int istep=0; istep<step_list.size(); istep++)
		{
			if(!step_isUsed[istep]) {continue;}

			//Iterate over all detids (keys) of map, and look for the detid we're interested in
			map< double, vector<double> >::iterator it = v_maps_allSteps[istep].begin();

			while(it->first != current_detid && it != v_maps_allSteps[istep].end()) {it++;} //Loop on all detids (keys) of the map to find current detid

			if(it == v_maps_allSteps[istep].end() ) //If detid not found
			{
				cout<<FRED("Detid "<<current_detid<<" not found for Vstep "<<step_list[istep]<< " !")<<endl;
				continue;
			}

			// cout<<"detid "<<Convert_Number_To_TString(it->first)<<", "<<step_list[istep]<<"V, noise "<<it->second[0]<<", error : "<<it->second[1]<<endl;

			int ibin = Convert_TString_To_Number(step_list[istep]) / ((xmax - xmin) / nbins); //Compute bin corresponding to this voltage
			// cout<<"Vstep = "<<step_list[istep]<<" / ibin = "<<ibin<<" / "<<nbins<<endl;

			//Fill noise_vs_bias histo with noise info for current Vstep
			h_noise_vs_bias_current_detid->SetBinContent(ibin, it->second[0]);
			h_noise_vs_bias_current_detid->SetBinError(ibin, it->second[1]);

			if(it->second[0] < ymin && it->second[0] != 0) {ymin = it->second[0];} //Compute ymin (for plotting)
		}

		//Once noise_vs_bias histo is done, fit it and extract results
		if(h_noise_vs_bias_current_detid->GetEntries() != 0)
		{
			h_noise_vs_bias_current_detid->SetMinimum(ymin - 0.2); //Set custom ymin because there are empty bins

			fit_results = Fit_Noise_VS_Bias_Histogram_And_Make_Control_Plots(h_noise_vs_bias_current_detid, counter_control_plots, current_detid);
			detid = current_detid;

			//Fill the output TTree with fit result for current detid
			tree->Fill();
		}
		else {cout<<FRED("Noise VS Bias histo empty for detid "+Convert_Number_To_TString(current_detid)<<" !")<<endl;}

		delete h_noise_vs_bias_current_detid; h_noise_vs_bias_current_detid = NULL;
	}

	f_fit_results->cd();
	tree->Write();

	delete tree; tree = NULL;
	f_fit_results->Close(); delete f_fit_results; f_fit_results = NULL;

	return;
}







//-------------------------------
// ##     ##    ###    #### ##    ##
// ###   ###   ## ##    ##  ###   ##
// #### ####  ##   ##   ##  ####  ##
// ## ### ## ##     ##  ##  ## ## ##
// ##     ## #########  ##  ##  ####
// ##     ## ##     ##  ##  ##   ###
// ##     ## ##     ## #### ##    ##
//-------------------------------

int main()
{
	Fill_Step_List_Vector();
	Modified_tdr_style();

	TString run = "303272";

	Produce_Noise_VS_Bias_Histograms_For_All_Detids_And_Store_Results(run);

	return 0;
}
