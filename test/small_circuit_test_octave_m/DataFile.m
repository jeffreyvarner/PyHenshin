function DF = DataFile(TSTART,TSTOP,Ts,INDEX)

% Load the stoichiometric matrix - 
stoichiometric_matrix = load('STMatrix.dat');
[number_of_species,number_of_reactions] = size(stoichiometric_matrix);

% Kinetic parameter vector - 
KPV = [
	9.34087611425;	% 1 inducer_binding::INDUCER+GENE-->INDUCER_GENE
	0.831303801102;	% 2 inducer_binding_reverse::INDUCER_GENE-->INDUCER+GENE
	8.67336506588;	% 3 rnap_binding::RNAP+INDUCER_GENE-->RNAP_INDUCER_GENE
	1.09595226242;	% 4 rnap_binding_reverse::RNAP_INDUCER_GENE-->RNAP+INDUCER_GENE
	10.3606024458;	% 5 transcription::RNAP_INDUCER_GENE-->RNAP+mRNA+INDUCER
	11.252473105;	% 6 translation_binding::mRNA+RIBOSOME-->RIBOSOME_mRNA
	0.955883154033;	% 7 translation_binding_reverse::RIBOSOME_mRNA-->mRNA+RIBOSOME
	10.5976815126;	% 8 translation_start::RIBOSOME_mRNA-->RIBOSOME_mRNA_START
	11.3175915728;	% 9 translation_finish::RIBOSOME_mRNA_START-->RIBOSOME+mRNA+PROTEIN
	10.0076384836;	% 10 repressor_binding::REPRESSOR+GENE-->REPRESSOR_GENE
	0.955753789165;	% 11 repressor_binding_reverse::REPRESSOR_GENE-->REPRESSOR+GENE
	10.2815791152;	% 12 rnap_production_degradation::RNAP-->[]
	1.03906460807;	% 13 rnap_production_degradation_reverse::[]-->RNAP
	9.82053412745;	% 14 ribosome_production_degradation::RIBOSOME-->[]
	1.13785641477;	% 15 ribosome_production_degradation_reverse::[]-->RIBOSOME
	9.67105959871;	% 16 inducer_degradation::INDUCER-->[]
	1.0092922313;	% 17 mRNA_degradation::mRNA-->[]
	1.7646666402;	% 18 protein_degradation::PROTEIN-->[]
];

% Initial condition vector - 
ICV = [
	0.0;	% 1 INDUCER
	1.0;	% 2 GENE
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
