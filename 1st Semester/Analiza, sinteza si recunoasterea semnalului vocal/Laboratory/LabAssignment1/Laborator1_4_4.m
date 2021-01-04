% 4.4. Experimente pe rata de eșantionare: Scrieți un script MATLAB pentru
% a înregistra dvs. de rostire "numele meu este ***", cu o rată de 
% eșantionare de 16 kHz și 8-biți rezoluție sau folositi un fisier 
% existent. Încercați să reeșantionati semnalele audio prin scăderea 
% ratelor de eșantionare la 11 kHz, 8 kHz, 4 kHz, 2 kHz, 1 kHz, și așa 
% mai departe. La care rata de esantionare începem să avem dificultăți 
% în a înțelege conținutul enunțului?

fs=16000; % Frecventa de esantionare
t=5;
nBits = 8; % Rezolutia
nChannels = 1; % Nr canale
fprintf('Apasa tasta t pentru a incepe o inregistrare de %g secunde',t);
pause;

fprintf('A inceput inregistrarea');
recorded_audio = audiorecorder(fs,nBits,nChannels);
record(recorded_audio,t);
fprintf('Gata de inregistrat.\n');

fprintf('Apasa tasta t pentru a salva inregistrarea in %s... \n', t);
pause;
file = 'numele_meu.wav';
w = getaudiodata(recorded_audio, 'int16'); 
audiowrite(file,w,fs);
fprintf('Fisierul a fost salvat %s\n', file);

[y, fs]=audioread('numele_meu.wav');
sound = audioplayer(y, fs);
play(sound);

pause(10);

fs = 11000;
sound = audioplayer(y, fs);
play(sound);

pause(10);

fs = 8000;
sound = audioplayer(y, fs);
play(sound);

pause(10);

fs = 4000;
sound = audioplayer(y, fs);
play(sound);

pause(10);

fs = 2000;
sound = audioplayer(y, fs);
play(sound);

pause(10);

fs = 1000;
sound = audioplayer(y, fs);
play(sound);

pause(10);


