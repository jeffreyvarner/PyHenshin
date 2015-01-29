% =================== PHASE ONE: PROBLEM SETUP ======================================== %
% Setup uptake/production constraints -
qUptake_C1 = 1.0;
qG = 0.2

% Are we minimizing (1) -or- maximizing (-1)?
MIN_MAX_FLAG = -1;
FLUX_INDEX_PRODUCTION = 22; 
OBJ_VECTOR = [FLUX_INDEX_PRODUCTION];
% ====================================================================================== %
%
% =================== PHASE TWO: PROBLEM SOLUTION ====================================== %
% Set the pointer to the DataFile for the FBA problem
pDataFile = @DataFile;

% Create an instance of the data file -
DF = feval(pDataFile,0,0,0,[]);

% Set problem specific constraints -
SBA = DF.SPECIES_BOUND_ARRAY;
INDEX_BOUNDS = DF.SPECIES_BOUNDS_INDEX;

% Bounds on d(A_x)/dt -
SBA(INDEX_BOUNDS(3,2),2) = -1*qUptake_C1;
SBA(INDEX_BOUNDS(3,2),3) = -1*qUptake_C1;

SBA(INDEX_BOUNDS(10,2),2) = qG;

% set the bounds -
DF.SPECIES_BOUND_ARRAY = SBA;

% Call the FBA solver -
[FLOW,status,UPTAKE] = FluxDriver(pDataFile,OBJ_VECTOR,MIN_MAX_FLAG,DF);
% ====================================================================================== %