function DF = DataFile(TSTART,TSTOP,Ts,INDEX)

% Load the stoichiometric matrix and flux bounds array - 
stoichiometric_matrix = load('Network.dat');
flux_bounds_array = load('FB.dat');
[number_of_species,number_of_reactions] = size(stoichiometric_matrix);

% Setup the free metabolite array - 
IDX_FREE_METABOLITES = [
	23	1	;	% 1 X_BIOMASS
	22	2	;	% 2 X_ENZYME
	13	3	;	% 3 X_S1
	14	4	;	% 4 X_S2
	16	5	;	% 5 X_D
	17	6	;	% 6 X_E
	15	7	;	% 7 X_F
	18	8	;	% 8 X_H
	19	9	;	% 9 X_O2
	20	10	;	% 10 X_ISOPRENE
];

% Split the stoichiometric matrix - 
IDX_BALANCED_METABOLITES = setdiff(1:number_of_species,IDX_FREE_METABOLITES(:,1));
N_IDX_BALANCED_METABOLITES = length(IDX_BALANCED_METABOLITES);

% Setup the bounds on species - 
BASE_BOUND = 20;
SPECIES_BOUND = [
	23	0	BASE_BOUND	;	% 1 X_BIOMASS
	22	0	BASE_BOUND	;	% 2 X_ENZYME
	13	-20	BASE_BOUND	;	% 3 X_S1
	14	0	BASE_BOUND	;	% 4 X_S2
	16	0	BASE_BOUND	;	% 5 X_D
	17	0	BASE_BOUND	;	% 6 X_E
	15	0	BASE_BOUND	;	% 7 X_F
	18	0	BASE_BOUND	;	% 8 X_H
	19	-0.5 BASE_BOUND	;	% 9 X_O2
	20	0	BASE_BOUND	;	% 10 X_ISOPRENE
];

% Split the stochiometrix matrix - 
S	=	stoichiometric_matrix(IDX_BALANCED_METABOLITES,:);
SDB	=	stoichiometric_matrix(SPECIES_BOUND(:,1),:);

% == DO NOT EDIT BELOW THIS LINE ================================== 
DF.STOICHIOMETRIC_MATRIX = stoichiometric_matrix;
DF.FLUX_BOUNDS = flux_bounds_array;
DF.SPECIES_BOUND_ARRAY = SPECIES_BOUND;
DF.SPECIES_BOUNDS_INDEX = IDX_FREE_METABOLITES;
DF.BALANCED_MATRIX = S;
DF.SPECIES_CONSTRAINTS = SDB;
DF.NUMBER_OF_REACTIONS = number_of_reactions;
DF.NUMBER_OF_STATES = number_of_species;
% ================================================================= 
return;
