#include <octave/oct.h>
#include <ov-struct.h>
#include <iostream>
#include <Math.h>

// Function prototypes - 
void calculateKinetics(ColumnVector&,ColumnVector&,ColumnVector&);
void calculateInputs();
void calculateMassBalances(int,Matrix&,ColumnVector&,ColumnVector&,ColumnVector&);

// Main function. Calls kinetics, inputs and balances. Returns the derivative - 
DEFUN_DLD(ExtBalanceFunction,args,nargout,"Calculate the mass balances.")
{
}

// Inputs function - 
void calculateInputs()
{
	 // Add inputs code here...
}

// Kinetics function - 
void calculateKinetics(ColumnVector& kV,ColumnVector& x,ColumnVector& rV)
{
	// Alias the species for debugging - 
	float INDUCER = x(0,0);
	float GENE = x(1,0);
	float INDUCER_GENE = x(2,0);
	float RNAP = x(3,0);
	float RNAP_INDUCER_GENE = x(4,0);
	float mRNA = x(5,0);
	float RIBOSOME = x(6,0);
	float RIBOSOME_mRNA = x(7,0);
	float RIBOSOME_mRNA_START = x(8,0);
	float PROTEIN = x(9,0);
	float REPRESSOR = x(10,0);
	float REPRESSOR_GENE = x(11,0);

	rV(0,0) = kV(0,0)*pow(GENE,4.0)*pow(INDUCER,2.0);
	rV(1,0) = kV(1,0)*(INDUCER_GENE);
	rV(2,0) = kV(2,0)*(INDUCER_GENE)*(RNAP);
	rV(3,0) = kV(3,0)*(RNAP_INDUCER_GENE);
	rV(4,0) = kV(4,0)*(RNAP_INDUCER_GENE);
	rV(5,0) = kV(5,0)*(RIBOSOME)*(mRNA);
	rV(6,0) = kV(6,0)*(RIBOSOME_mRNA);
	rV(7,0) = kV(7,0)*(RIBOSOME_mRNA);
	rV(8,0) = kV(8,0)*(RIBOSOME_mRNA_START);
	rV(9,0) = kV(9,0)*(GENE)*(REPRESSOR);
	rV(10,0) = kV(10,0)*(REPRESSOR_GENE);
	rV(11,0) = kV(11,0)*(RNAP);
	rV(12,0) = kV(12,0);
	rV(13,0) = kV(13,0)*(RIBOSOME);
	rV(14,0) = kV(14,0);
	rV(15,0) = kV(15,0)*(INDUCER);
	rV(16,0) = kV(16,0)*(mRNA);
	rV(17,0) = kV(17,0)*(PROTEIN);

}

// Balance equations function - 
void calculateMassBalances(int NSTATES,Matrix& STMATRIX,ColumnVector& rV,ColumnVector& uV,ColumnVector& dx)
{
	dx = STMATRIX*rV + uV;
}
