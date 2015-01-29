function DF = DataFile(TSTART,TSTOP,Ts,INDEX)

% Load the stoichiometric matrix - 
stoichiometric_matrix = load('STMatrix.dat');
[number_of_species,number_of_reactions] = size(stoichiometric_matrix);

% Kinetic parameter vector - 
KPV = [
	9.46321715145;	% 1 inducer_binding::2*INDUCER+4*GENE-->INDUCER_GENE
	0.85350154308;	% 2 inducer_binding_reverse::INDUCER_GENE-->2*INDUCER+4*GENE
	9.39893070529;	% 3 rnap_binding::RNAP+INDUCER_GENE-->RNAP_INDUCER_GENE
	0.902641444387;	% 4 rnap_binding_reverse::RNAP_INDUCER_GENE-->RNAP+INDUCER_GENE
	11.6488170204;	% 5 transcription::RNAP_INDUCER_GENE-->RNAP+mRNA+INDUCER
	10.7996270378;	% 6 translation_binding::mRNA+RIBOSOME-->RIBOSOME_mRNA
	1.01444830115;	% 7 translation_binding_reverse::RIBOSOME_mRNA-->mRNA+RIBOSOME
	9.78775302044;	% 8 translation_start::RIBOSOME_mRNA-->RIBOSOME_mRNA_START
	11.6228428389;	% 9 translation_finish::RIBOSOME_mRNA_START-->RIBOSOME+mRNA+PROTEIN
	10.6069179775;	% 10 repressor_binding::REPRESSOR+GENE-->REPRESSOR_GENE
	1.02235680882;	% 11 repressor_binding_reverse::REPRESSOR_GENE-->REPRESSOR+GENE
	8.18198721083;	% 12 rnap_production_degradation::RNAP-->[]
	0.898380914591;	% 13 rnap_production_degradation_reverse::[]-->RNAP
	13.0048958395;	% 14 ribosome_production_degradation::RIBOSOME-->[]
	0.979712548266;	% 15 ribosome_production_degradation_reverse::[]-->RIBOSOME
	10.6485150614;	% 16 inducer_degradation::INDUCER-->[]
	8.95873862393;	% 17 mRNA_degradation::mRNA-->[]
	10.3896422144;	% 18 protein_degradation::PROTEIN-->[]
];

% Initial condition vector - 
ICV = [
	0.0;	% 1 INDUCER
	0.0;	% 2 GENE
	0.0;	% 3 INDUCER_GENE
	0.0;	% 4 RNAP
	0.0;	% 5 RNAP_INDUCER_GENE
	0.0;	% 6 mRNA
	0.0;	% 7 RIBOSOME
	0.0;	% 8 RIBOSOME_mRNA
	0.0;	% 9 RIBOSOME_mRNA_START
	0.0;	% 10 PROTEIN
	0.0;	% 11 REPRESSOR
	0.0;	% 12 REPRESSOR_GENE
];

% == DO NOT EDIT BELOW THIS LINE ================================== 
DF.STOICHIOMETRIC_MATRIX = stoichiometric_matrix;
DF.NUMBER_OF_REACTIONS = number_of_reactions;
DF.NUMBER_OF_STATES = number_of_species;
DF.KINETIC_PARAMETER_VECTOR = KPV;
DF.INITIAL_CONDITION_VECTOR = ICV;
DF.MEASUREMENT_SELECTION_VECTOR = 1:number_of_species;
% ================================================================= 
return;
