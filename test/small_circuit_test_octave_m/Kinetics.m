function rV = Kinetics(t,x,DF)

% Get the parameter vector - 
kV = DF.KINETIC_PARAMETER_VECTOR;

% Alias the species for debugging - 
INDUCER = x(1,1);
GENE = x(2,1);
INDUCER_GENE = x(3,1);
RNAP = x(4,1);
RNAP_INDUCER_GENE = x(5,1);
mRNA = x(6,1);
RIBOSOME = x(7,1);
RIBOSOME_mRNA = x(8,1);
RIBOSOME_mRNA_START = x(9,1);
PROTEIN = x(10,1);
REPRESSOR = x(11,1);
REPRESSOR_GENE = x(12,1);

% Calculate the rate vector - 
rV(1,1) = kV(1,1)*((GENE)^1.0)*((INDUCER)^1.0);
rV(2,1) = kV(2,1)*((INDUCER_GENE)^1.0);
rV(3,1) = kV(3,1)*((INDUCER_GENE)^1.0)*((RNAP)^1.0);
rV(4,1) = kV(4,1)*((RNAP_INDUCER_GENE)^1.0);
rV(5,1) = kV(5,1)*((RNAP_INDUCER_GENE)^1.0);
rV(6,1) = kV(6,1)*((RIBOSOME)^1.0)*((mRNA)^1.0);
rV(7,1) = kV(7,1)*((RIBOSOME_mRNA)^1.0);
rV(8,1) = kV(8,1)*((RIBOSOME_mRNA)^1.0);
rV(9,1) = kV(9,1)*((RIBOSOME_mRNA_START)^1.0);
rV(10,1) = kV(10,1)*((GENE)^1.0)*((REPRESSOR)^1.0);
rV(11,1) = kV(11,1)*((REPRESSOR_GENE)^1.0);
rV(12,1) = kV(12,1)*((RNAP)^1.0);
rV(13,1) = kV(13,1);
rV(14,1) = kV(14,1)*((RIBOSOME)^1.0);
rV(15,1) = kV(15,1);
rV(16,1) = kV(16,1)*((INDUCER)^1.0);
rV(17,1) = kV(17,1)*((mRNA)^1.0);
rV(18,1) = kV(18,1)*((PROTEIN)^1.0);

return;
