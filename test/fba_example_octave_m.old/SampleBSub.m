NSAMPLES = 1000

% Are we minimizing (1) -or- maximizing (-1)?
MIN_MAX_FLAG = -1;
FLUX_INDEX_PRODUCTION = 22; 
OBJ_VECTOR = [FLUX_INDEX_PRODUCTION];

q_vector = linspace(0,20.0,NSAMPLES);
q_glucose = 20;

DF = BSubDataFile(0,0,0,[]);
%DF = DataFile(0,0,0,[]);
FA = [];
for sample_index = 1:NSAMPLES
	
	DFIN = DF;
	SBA = DFIN.SPECIES_BOUND_ARRAY;
	INDEX_BOUNDS = DFIN.SPECIES_BOUNDS_INDEX;

	% Bounds on d(A_x)/dt -
	SBA(INDEX_BOUNDS(3,2),2) = -1*q_glucose;
	SBA(INDEX_BOUNDS(3,2),3) = 0;
	SBA(INDEX_BOUNDS(10,2),2) = q_vector(sample_index);

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
save -ascii FLUX_BSUB.dat FAK;