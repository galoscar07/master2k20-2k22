function getrec

% Copyright (c) 1995 Philipos C. Loizou
%

fp= fopen('sndcard.cfg','r');

if fp<0
  errordlg('Could not find souncard config file: sndcard.cfg.  If this file does not exist, then create it and put the name of the record utility program','GETREC');
else
 
 snd = fscanf(fp,'%s');
 fclose(fp);

 if ~isempty(snd) 
    exe=['!' snd];
    eval(exe); 
 else
  str=sprintf('Could not find record utility: %s',snd);
  errordlg(str,'GETREC');
 end

end

