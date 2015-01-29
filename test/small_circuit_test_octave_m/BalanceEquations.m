function dxdt = BalanceEquations(x,t,DF)

% Get the stoichiometric matrix -
STM = DF.STOICHIOMETRIC_MATRIX;

% Calculate the kinetics -
rV = Kinetics(t,x,DF);

% Calculate the inputs -
uV = Input(t,x,DF);

% Calculate the dxdt terms -
dxdt = STM*rV + uV;

return;
