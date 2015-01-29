function DF = DataFile(TSTART,TSTOP,Ts,INDEX)

% Load the stoichiometric matrix and flux bounds array - 
stoichiometric_matrix = load('Network.dat');

[number_of_species,number_of_reactions] = size(stoichiometric_matrix);

% Kinetic parameter vector - 
KPV = [
];


% Initial condition vector - 
ICV = [
	0.0;	% 1 A
	0.0;	% 2 ATP
	0.0;	% 3 B
	0.0;	% 4 NADH
	0.0;	% 5 C
	0.0;	% 6 F
	0.0;	% 7 G
	0.0;	% 8 D
	0.0;	% 9 E
	0.0;	% 10 H
	0.0;	% 11 O2
	0.0;	% 12 ISOPRENE
	0.0;	% 13 ENZYME
	0.0;	% 14 X_S1
	0.0;	% 15 X_S2
	0.0;	% 16 X_F
	0.0;	% 17 X_D
	0.0;	% 18 X_E
	0.0;	% 19 X_H
	0.0;	% 20 X_O2
	0.0;	% 21 X_ENZYME
	0.0;	% 22 X_ISOPRENE
	0.0;	% 23 X_BIOMASS
	1.0;	% 24 E_RXN_R1
	1.0;	% 25 E_RXN_R2A
	1.0;	% 26 E_RXN_R2B
	1.0;	% 27 E_RXN_R3
	1.0;	% 28 E_RXN_R4
	1.0;	% 29 E_RXN_R5A
	1.0;	% 30 E_RXN_R6
	1.0;	% 31 E_RXN_R7
	1.0;	% 32 E_RXN_R8A
	1.0;	% 33 E_RXN_R8B
	1.0;	% 34 E_RXN_RES
	1.0;	% 35 E_RXN_ISOPRENE
	1.0;	% 36 E_RXN_TC1
	1.0;	% 37 E_RXN_TC2
	1.0;	% 38 E_RXN_TF
	1.0;	% 39 E_RXN_TD
	1.0;	% 40 E_RXN_TE
	1.0;	% 41 E_RXN_TH
	1.0;	% 42 E_RXN_TO2
	1.0;	% 43 E_RXN_ISO_EXPORT
	1.0;	% 44 E_RXN_ENZ_EXPORT
	1.0;	% 45 E_RXN_GROWTH
	1.0;	% 46 E_RXN_ENZYME
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
