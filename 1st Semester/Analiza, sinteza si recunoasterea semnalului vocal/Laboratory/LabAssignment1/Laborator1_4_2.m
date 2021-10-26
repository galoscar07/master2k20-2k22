%4.2. Inregistrare Wave. Scrieți un script MATLAB pentru a înregistra 10 de
% secunde de vorbire, cum ar fi "Numele meu este X....Y.... și sunt un student
% la master in anul I TM la departamentul de Comunicatii al Universitatii
% Tehnice din Cluj-Napoca". Salvați înregistrarea ca myVoice.wav.
% Alți parametri de înregistrare sunt: Frecventa de eșantionare = 16 kHz, 
% rezoluție biți = 16 biți. Script-ul va permite indicarea răspunsurilor 
% la următoarele întrebări, în cadrul ferestrei MATLAB.
% Cât spațiu este ocupat cu date audio în spațiul de lucru MATLAB?
% Ce tip de date au datele audio?
% Cum vă calculati cantitatea de memorie necesară din parametrii de înregistrare?
% Care este dimensiunea fisierului myVoice.wav?
% Câti octeți sunt utilizati în myVoice.wav pentru a înregistra date, 
% altele decât datele audio în sine?

fs=16000; % Frecventa de esantionare
t=10;
nBits = 16; % Rezolutia
nChannels = 1; % Nr canale
fprintf('Apasa tasta t pentru a incepe o inregistrare de %g secunde',t);
pause;

fprintf('A inceput inregistrarea');
recorded_audio = audiorecorder(fs,nBits,nChannels);
% se inregistraza un numar de t secunde
record(recorded_audio,t);
fprintf('Gata de inregistrat.\n');

fprintf('Apasa tasta t pentru a salva inregistrarea in %s... \n', t);
pause;
% Preia datele in format de int16 array si se salveaza intr-un fisier
% numit myVoice.was
file = 'myVoice.wav';
w = getaudiodata(recorded_audio, 'int16'); 
audiowrite(file,w,fs);
fprintf('Fisierul a fost salvat %s\n', file);
fprintf('Apasa tasta t pentru a reda continutul fisierului %s...\n', file);

play(recorded_audio);

% Cât spațiu este ocupat cu date audio în spațiul de lucru MATLAB?
dimensiune = length(w) * 2 / 100;
fprintf('\nSpatiul ocupat: %s bytes \n', dimensiune);

% Ce tip de date au datele audio?
[~,~,ext] = fileparts(which('myVoice.wav'));
fprintf('\nTipul de date audio este: %s \n', ext);

% Cum vă calculati cantitatea de memorie necesară din parametrii de înregistrare?
% -- se calculeaza ca fiind rata de esantionare * nr de secunde
memoria_necesara_este = fs * t;
fprintf('\nCantitatea de memorie este de %d bytes \n', memoria_necesara_este);

% Care este dimensiunea fisierului myVoice.wav?
[y, fs] = audioread('myVoice.wav');
memorie = length(y) * 32768;
fprintf('\nDimensiunea myVoice.wav este de %d bytes \n', memorie);

% Câti octeți sunt utilizati în myVoice.wav pentru a înregistra date, altele decât datele audio în sine?
octeti = memorie - dimensiune;
fprintf('\nOcteti utilizati pentru alte date decat cele audio: %d', octeti);
