function uV = Input(t,x,DF)

% Get the number of states - 
number_of_states = DF.NUMBER_OF_STATES;

% Default is to return a vector of zeros - 
uV = zeros(number_of_states,1);
if (t> 20)
	uV(1,1) = 100.0*exp(-0.01*t);
end

return;
