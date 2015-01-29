NUMBER_OF_FILES = 8

FLUX_ARRAY = []
for file_index = 1:NUMBER_OF_FILES

	cmd = ['DATA = load(''Flux-Induction-C',num2str(file_index),'.dat'');'];
	eval(cmd);
	disp(cmd);

	FLUX_ARRAY = [FLUX_ARRAY DATA];
end

LARR = [0.001 0.1 0.5 1.0 5.0 10.0 100.0 1000.0];