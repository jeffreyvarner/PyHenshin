NSAMPLES = 1;

% Load the DataFile -
DF = DataFile(0,0,0,[]);
STM = DF.STOICHIOMETRIC_MATRIX;
IDX_CX_PROD = find(STM(30,:)>0); 
%IDX_CX_PROD = 132;

% What are the diffusion fluxes?
IDX_DIFF_FLUX = [];

% Are we minimizing (1) -or- maximizing (-1)?
MIN_MAX_FLAG = -1;
FLUX_INDEX_PRODUCTION = IDX_CX_PROD; 
OBJ_VECTOR = [FLUX_INDEX_PRODUCTION];

%q_vector = linspace(0,1.0,NSAMPLES) + 0.1;
q_vector = 1.0;


FA = [];
for sample_index = 1:NSAMPLES
	
	DFIN = DF;
	SBA = DFIN.SPECIES_BOUND_ARRAY;
	INDEX_BOUNDS = DFIN.SPECIES_BOUNDS_INDEX;

	% Bounds on d(A_x)/dt -
	SBA(INDEX_BOUNDS(1,2),2) = -1*q_vector(sample_index);
	SBA(INDEX_BOUNDS(1,2),3) = 0;

	% Force diffusion -
	%FBA = DFIN.FLUX_BOUNDS;
	%FBA(13,1) = 0.1*q_vector(sample_index);
	%DFIN.FLUX_BOUNDS = FBA;

	% set the bounds -
	DFIN.SPECIES_BOUND_ARRAY = SBA;

	% Call the FBA solver -
	[FLOW,status,UPTAKE] = FluxDriver(@DataFile,OBJ_VECTOR,MIN_MAX_FLAG,DFIN);
	
	BLOCK = [status ; FLOW];
	FA = [FA BLOCK];
end

% Filter out the non-feasible solutions -
IDX = find(FA(1,:)==0);
FAK = FA(2:end,IDX);
save -ascii FLUX_TEST.dat FAK;