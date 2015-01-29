function DF = DataFile(TSTART,TSTOP,Ts,INDEX)

% Load the stoichiometric matrix and flux bounds array - 
stoichiometric_matrix = load('Network.dat');
flux_bounds_array = load('FB.dat');
[number_of_species,number_of_reactions] = size(stoichiometric_matrix);

% Setup the free metabolite array - 
IDX_FREE_METABOLITES = [
	15	1	;	% 1 Ax
	16	2	;	% 2 Bx
	17	3	;	% 3 Cx
	1	4	;	% 4 Lx
	4	5	;	% 5 SYSTEM
];

% Split the stoichiometric matrix - 
IDX_BALANCED_METABOLITES = setdiff(1:number_of_species,IDX_FREE_METABOLITES(:,1));
N_IDX_BALANCED_METABOLITES = length(IDX_BALANCED_METABOLITES);

% Setup the bounds on species - 
BASE_BOUND = 1;
SPECIES_BOUND = [
	15	0	BASE_BOUND	;	% 1 Ax
	16	0	BASE_BOUND	;	% 2 Bx
	17	0	BASE_BOUND	;	% 3 Cx
	1	0	BASE_BOUND	;	% 4 Lx
	4	0	BASE_BOUND	;	% 5 SYSTEM
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
