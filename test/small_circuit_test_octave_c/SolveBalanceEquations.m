function [TSIM,X,OUTPUT] = SolveBalanceEquations(pDataFile,TSTART,TSTOP,Ts,DFIN)

% Check to see if I need to load the datafile 
if (~isempty(DFIN))
	DF = DFIN;
else
	DF = feval(pDataFile,TSTART,TSTOP,Ts,[]);
end;

% Get reqd stuff from data struct - 
IC = DF.INITIAL_CONDITION_VECTOR;
TSIM = TSTART:Ts:TSTOP;
MEASUREMENT_INDEX_VECTOR = DF.MEASUREMENT_SELECTION_VECTOR;

% Call the ODE solver - the default is ODE15s
pMassBalances = @(x,t)BalanceEquations(x,t,DF);
X = lsode(pMassBalances,IC,TSIM);

% Calculate the output - 
OUTPUT = X(:,MEASUREMENT_INDEX_VECTOR);

% return to caller -
return;
