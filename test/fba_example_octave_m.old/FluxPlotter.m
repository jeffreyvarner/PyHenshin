% Load the data -
FA_ECOLI = load('FLUX_ECOLI.dat');
FA_BSUB = load('FLUX_BSUB.dat');
FA_SUPER = load('FLUX_SUPER.dat');

% Make the plots -
hold on;
plot(FA_ECOLI(22,:),FA_ECOLI(20,:),'r');
plot(FA_BSUB(22,:),FA_BSUB(20,:),'b');
plot(FA_SUPER(22,:),FA_SUPER(20,:),'g');
set(gca,'XMinorTick','on','YMinorTick','on')