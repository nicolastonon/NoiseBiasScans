/**
Nicolas Tonon, IPHC
12/2017
*/

#include <map>
#include "TRandom3.h"
#include "TGraphErrors.h"

#include "Helper_Functions.h"

#define model_choice 1 //Choose here fitting model to use

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

void Style_Control_TGraph(TGraphErrors* g)
{
	g->SetMarkerStyle(8);
	g->SetMarkerSize(1.5);
	g->SetMarkerColor(1);

	g->GetXaxis()->SetTitle("Bias voltage [V]");
	g->GetXaxis()->SetTitleSize(.05);

	g->GetYaxis()->SetTitle("Noise [a.u.]");
	g->GetYaxis()->SetTitleSize(.05);
	g->GetYaxis()->SetTitleOffset(0.95);

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

	double detid=0, noise=0, error=0, chi2=0, noise_rms = 0;

	//To read input branches
	t_input->SetBranchAddress("detid", &detid);
	t_input->SetBranchAddress("noise_mean", &noise);
	t_input->SetBranchAddress("noise_err", &error);
	t_input->SetBranchAddress("noise_chi2", &chi2);
	t_input->SetBranchAddress("noise_rms", &noise_rms);

	map< double, vector<double> > map_detid_noise; //Will map detid <-> noise infos (for given Vstep)

	vector<double> v_tmp(4);
	//For all detids, read input file, create map : detid <-> noise infos
	for(int ientry=0; ientry<t_input->GetEntries(); ientry++)
	{
		//FIXME -- don't process all entries for now
		// if(ientry>10) {break;}

		v_tmp.clear(); v_tmp.resize(4);
		detid=0, noise=0, error=0, chi2=0, noise_rms=0;

		t_input->GetEntry(ientry);

		v_tmp[0] = noise; v_tmp[1] = error; v_tmp[2] = noise_rms; v_tmp[3] = chi2;

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
		if(model_choice == 0) result = par[0];
		else if(model_choice == 1) result = par[0] + par[3] * (xx - par[2]); //c0 + c1 * (x-Vfd)
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
 * @param graph_to_fit          -- TGraphErrors* noise_vs_bias to fit
 * @param counter_control_plots -- counter (don't store all control plots)
 * @param detid                 -- detid corresponding to the histo
 */
pair<double, double> Fit_Noise_VS_Bias_Histogram_And_Make_Control_Plots(TGraphErrors* graph_to_fit, int& counter_control_plots, double detid)
{
	gStyle->SetOptFit(1);
	gStyle->SetFuncWidth(3);

	//Fitting model --- (name, fcn, xmin, xmax, npar)
	TF1* noise_fit;
	if(model_choice==0)
	{
		noise_fit = new TF1("myfunc", Fitting_Model, graph_to_fit->GetXaxis()->GetXmin(), graph_to_fit->GetXaxis()->GetXmax(), 3);
		noise_fit->SetParNames("Constant","#beta", "V_{FD}");
		noise_fit->SetParameters(5., 1., 100.); //-- init. parameters needed for convergence
		// noise_fit->SetParameters(par_cst, par_beta, par_vfd); //-- init. parameters needed for convergence
	}
	else if(model_choice==1)
	{
		noise_fit = new TF1("myfunc", Fitting_Model, graph_to_fit->GetXaxis()->GetXmin(), graph_to_fit->GetXaxis()->GetXmax(), 4);
		noise_fit->SetParNames("Constant","#beta", "V_{FD}", "Slope");
		noise_fit->SetParameters(6., 5., 100., 1.); //-- init. parameters needed for convergence

	}


	graph_to_fit->Fit(noise_fit, "q"); //quiet

	pair<double, double> result;
	result.first = noise_fit->GetParameter(2);
	result.second = noise_fit->GetParError(2);
	// cout<<endl<<"noise_fit->GetParameter(0) = "<<noise_fit->GetParameter(0)<<" / error = "<<noise_fit->GetParError(0)<<endl;
	// cout<<"noise_fit->GetParameter(1) = "<<noise_fit->GetParameter(1)<<" / error = "<<noise_fit->GetParError(1)<<endl;
	// cout<<"noise_fit->GetParameter(2) = "<<noise_fit->GetParameter(2)<<" / error = "<<noise_fit->GetParError(2)<<endl;

	// if(counter_control_plots < 5 && noise_fit->GetParameter(2) > 0) //Only plot few histos, not all
	if(noise_fit->GetParameter(2) > 0) //Only plot few histos, not all //FIXME
	{
		TCanvas* c = new TCanvas("c", "", 1000, 800); c->cd();
		c->SetTopMargin(0.1);
		c->SetBottomMargin(0.1);

		Style_Control_TGraph(graph_to_fit);

		graph_to_fit->Draw("AP"); //A=draw axis, P=draw markers,

		Draw_ExtraText(c);

		//--- display fit proba on plot
		// cout<<"Fit proba : "<<noise_fit->GetProb()<<endl;
		TLatex latex;
		latex.SetNDC();
		latex.SetTextSize(0.03);
		TString tmp = "Fit->GetProb() = " + Convert_Number_To_TString(noise_fit->GetProb(), 3);
		latex.DrawLatex(0.70, 0.60, tmp);

		TLegend *leg = new TLegend(0.70, 0.70, 0.90, 0.80);
		//leg->SetBorderSize(0.1);
		leg->SetTextFont(42);
		// leg->SetHeader("Noise analysis");
		leg->AddEntry(graph_to_fit, "Data", "P");
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

		//FIXME -- only few TIB modules for now
		// cout<<Convert_Number_To_TString(current_detid)<<endl;
		if( !Convert_Number_To_TString(current_detid).Contains("36912138") && !Convert_Number_To_TString(current_detid).Contains("369121390") && !Convert_Number_To_TString(current_detid).Contains("36912586") && !Convert_Number_To_TString(current_detid).Contains("369125870") ) {continue;}
		TGraphErrors* g_noise_vs_bias_currentDetid = new TGraphErrors(step_list.size());

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
				cout<<FMAG("Detid "<<Convert_Number_To_TString(current_detid)<<" not found for Vstep "<<step_list[istep]<< " !")<<endl;
				continue;
			}

			// cout<<"detid "<<Convert_Number_To_TString(it->first)<<", "<<step_list[istep]<<"V, noise "<<it->second[0]<<", error : "<<it->second[1]<<endl;

			// int ibin = Convert_TString_To_Number(step_list[istep]) / ((xmax - xmin) / nbins); //Compute bin corresponding to this voltage
			// cout<<"Vstep = "<<step_list[istep]<<" / ibin = "<<ibin<<" / "<<nbins<<endl;

			//Fill noise_vs_bias histo with noise info for current Vstep
			g_noise_vs_bias_currentDetid->SetPoint(istep, Convert_TString_To_Number(step_list[istep]), it->second[0]);
			g_noise_vs_bias_currentDetid->SetPointError(istep, 0., it->second[1]); //ipt, e_x, e_y

			if(it->second[0] < ymin && it->second[0] != 0) {ymin = it->second[0];} //Compute ymin (for plotting)
		}

		//Once noise_vs_bias histo is done, fit it and extract results
		if(g_noise_vs_bias_currentDetid->GetN() != 0)
		{
			g_noise_vs_bias_currentDetid->SetMinimum(ymin - 0.2); //Set custom ymin because there are empty bins
			g_noise_vs_bias_currentDetid->GetXaxis()->SetRangeUser(0., 300.);

			fit_results = Fit_Noise_VS_Bias_Histogram_And_Make_Control_Plots(g_noise_vs_bias_currentDetid, counter_control_plots, current_detid);
			detid = current_detid;

			//Fill the output TTree with fit result for current detid
			tree->Fill();
		}
		else {cout<<FRED("Noise VS Bias histo empty for detid "+Convert_Number_To_TString(current_detid)<<" !")<<endl;}

		delete g_noise_vs_bias_currentDetid; g_noise_vs_bias_currentDetid = NULL;
	}

	f_fit_results->cd();
	tree->Write();

	delete tree; tree = NULL;
	f_fit_results->Close(); delete f_fit_results; f_fit_results = NULL;

	return;
}







//--------------------------------------
//  ######  ######## ##     ## ########  #### ########  ######
// ##    ##    ##    ##     ## ##     ##  ##  ##       ##    ##
// ##          ##    ##     ## ##     ##  ##  ##       ##
//  ######     ##    ##     ## ##     ##  ##  ######    ######
//       ##    ##    ##     ## ##     ##  ##  ##             ##
// ##    ##    ##    ##     ## ##     ##  ##  ##       ##    ##
//  ######     ##     #######  ########  #### ########  ######
//--------------------------------------

double Get_Vfd_Pull_From_MCToys_And_Return_Mean(int ntoys, double error)
{
	// create a random number generator
	// gRandom = new TRandom3();
	gRandom->SetSeed(0);

	int nbins = 60; double xmin = 2.5, xmax = 302.5;
	TH1F* h_vfd_toys = new TH1F("", "", 100, -0, 500);

	TF1* noise_fit = new TF1("myfunc", Fitting_Model, xmin, xmax, 3);
	noise_fit->SetParNames("Constant","#beta", "V_{FD}");


	double* par = new double[3];
	double* x = new double[1];

	for(int itoy=0; itoy<ntoys; itoy++)
	{
		//--- Init fit parameters
		// noise_fit->SetParameters(5., 1., 100.); //-- re-init fit parameters ; need to be tuned, for fit convergence
		noise_fit->SetParameters(5.1, 1., 200.); //-- re-init fit parameters ; need to be tuned, for fit convergence

		TH1F* h_1step = new TH1F("", "", nbins, xmin, xmax);
		// par[0] = 5.; par[1] = 3.3; par[2] = 100.; //Choose true parameters to construct the toys histo
		//--- Set true parameters
		par[0] = 5.; par[1] = 3.3; par[2] = 100.; //Choose true parameters to construct the toys histo
		double vfd = 0;

		for(int istep=0; istep<step_list.size(); istep++)
		{
			x[0] = Convert_TString_To_Number(step_list[istep]);

			int ibin = Convert_TString_To_Number(step_list[istep]) / ((xmax - xmin) / nbins); //Compute bin corresponding to this voltage
			h_1step->SetBinContent(ibin, gRandom->Gaus(Fitting_Model(x, par), error) );
			h_1step->SetBinError(ibin, error);
		}

		h_1step->Fit(noise_fit, "q");

		vfd = noise_fit->GetParameter(2);

		h_vfd_toys->Fill(vfd);
		if(itoy % 1000 == 0)
		{
			cout<<"vfd "<<vfd<<endl;
			cout<<"Fit proba : "<<noise_fit->GetProb()<<endl;
		}

		if(itoy==0)
		{
			TCanvas* c_control = new TCanvas("c_control", "", 1000, 800); c_control->cd();
			c_control->SetTopMargin(0.1);
			c_control->SetBottomMargin(0.1);
			h_1step->SetMinimum(par[0] - 0.5); h_1step->SetMaximum(par[0] + 1);
			h_1step->Draw();
			Draw_ExtraText(c_control);
			c_control->SaveAs("toy_control.png");
			delete c_control; c_control = NULL;
		}

		delete h_1step; h_1step = NULL;
	}

	TF1* gaus_fit = new TF1("myfunc", "gaus", h_vfd_toys->GetXaxis()->GetXmin(), h_vfd_toys->GetXaxis()->GetXmax() );
	// TF1* gaus_fit = new TF1("myfunc", "landau", h_vfd_toys->GetXaxis()->GetXmin(), h_vfd_toys->GetXaxis()->GetXmax() );
	h_vfd_toys->Fit(gaus_fit, "q");
	double mean_pull = gaus_fit->GetParameter(0);


	TCanvas* c = new TCanvas("c", "", 1000, 800); c->cd();
	c->SetTopMargin(0.1);
	c->SetBottomMargin(0.1);
	h_vfd_toys->Draw();
	Draw_ExtraText(c);

	// c->SaveAs("vfd_"+Convert_Number_To_TString(ntoys)+"toys.png" );
	c->SaveAs("vfd_toys.png" );

	delete noise_fit; noise_fit = NULL;
	delete gaus_fit; gaus_fit = NULL;
	delete h_vfd_toys; h_vfd_toys = NULL;
	delete c; c = NULL;
	delete[] par; par = NULL;
	delete[] x; x = NULL;

	return mean_pull;
}


void ToyStudy_Change_Scan_Procedure(int ntoys, double error, int scan_choice)
{
	if(scan_choice == 0)
	{
		step_list.push_back("275");
		step_list.push_back("280");
		step_list.push_back("290");
		step_list.push_back("295");
	}
	else if(scan_choice == 1)
	{
		step_list.push_back("5");
		step_list.push_back("15");
		step_list.push_back("25");
		step_list.push_back("35");
	}
	else if(scan_choice == 2)
	{
		step_list.push_back("85");
		step_list.push_back("95");
		step_list.push_back("105");
		step_list.push_back("115");
	}
	else {return;}

	Get_Vfd_Pull_From_MCToys_And_Return_Mean(ntoys, error);

	system( ("cp vfd_toys.png vfd_toys_scan"+Convert_Number_To_TString(scan_choice)+".png").Data() );

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
	Modified_tdr_style();

	// TString run = "203243";
	TString run = "303272";

	Fill_Step_List_Vector(run);

	Produce_Noise_VS_Bias_Histograms_For_All_Detids_And_Store_Results(run);

	//--- TOYS STUDIES
	// Get_Vfd_Pull_From_MCToys_And_Return_Mean(10000, 0.01);
	// ToyStudy_Change_Scan_Procedure(10000, 0.01, 2);

	return 0;
}
