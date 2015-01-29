import numpy as np

def calculateKinetics(x,t,PROBLEM_DICTIONARY):

	# Get the kinetics vector from the problem_dictionary 
	kV = PROBLEM_DICTIONARY['rate_constant_vector']
	number_of_rates = PROBLEM_DICTIONARY['number_of_rates']

	# Alias the species - 
	INDUCER = x[0];
	GENE = x[1];
	INDUCER_GENE = x[2];
	RNAP = x[3];
	RNAP_INDUCER_GENE = x[4];
	mRNA = x[5];
	RIBOSOME = x[6];
	RIBOSOME_mRNA = x[7];
	RIBOSOME_mRNA_START = x[8];
	PROTEIN = x[9];
	REPRESSOR = x[10];
	REPRESSOR_GENE = x[11];

	# Calculate the kinetics - 
	rV = np.zeros((number_of_rates,1))
	rV[0,0] = kV[0,0]*pow(GENE,4.0)*pow(INDUCER,2.0);
	rV[1,0] = kV[1,0]*(INDUCER_GENE);
	rV[2,0] = kV[2,0]*(INDUCER_GENE)*(RNAP);
	rV[3,0] = kV[3,0]*(RNAP_INDUCER_GENE);
	rV[4,0] = kV[4,0]*(RNAP_INDUCER_GENE);
	rV[5,0] = kV[5,0]*(RIBOSOME)*(mRNA);
	rV[6,0] = kV[6,0]*(RIBOSOME_mRNA);
	rV[7,0] = kV[7,0]*(RIBOSOME_mRNA);
	rV[8,0] = kV[8,0]*(RIBOSOME_mRNA_START);
	rV[9,0] = kV[9,0]*(GENE)*(REPRESSOR);
	rV[10,0] = kV[10,0]*(REPRESSOR_GENE);
	rV[11,0] = kV[11,0]*(RNAP);
	rV[12,0] = kV[12,0];
	rV[13,0] = kV[13,0]*(RIBOSOME);
	rV[14,0] = kV[14,0];
	rV[15,0] = kV[15,0]*(INDUCER);
	rV[16,0] = kV[16,0]*(mRNA);
	rV[17,0] = kV[17,0]*(PROTEIN);

	return rV

def calculateInputs(x,t,PROBLEM_DICTIONARY):

	# Default input is zero vector. Change for your problem.
	number_of_states = len(x)
	uV = np.zeros((number_of_states,1))
	return uV

def BalanceEquations(x,t,PROBLEM_DICTIONARY):

	# Call the kinetics function - 
	rV = calculateKinetics(x,t,PROBLEM_DICTIONARY)

	# Call the inputs function - 
	uV = calculateInputs(x,t,PROBLEM_DICTIONARY)

	# Calculate the balance equations - 
	STMATRIX = PROBLEM_DICTIONARY['stoichiometric_matrix']
	dxdt = STMATRIX*rV+uV

	# return dxdt to the caller - 
	return dxdt
