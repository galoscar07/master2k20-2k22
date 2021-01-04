% 4.5. Experimente cu adăugarea de zgomot: Scrieți un script MATLAB pentru 
% a înregistra rostirea "numele meu este ***", cu o rată de eșantionare de
% 8 kHz și 8-biți rezoluție. Putem adăuga zgomot la semnalele audio prin 
% utilizarea secventei următoare:
% k = 0.1;
% y2 = y + k*randn(length(y), 1); % Aduna zgomot 
% sound(y2, 8000); Playback/redare 
% plot(y2);
% Creșteti valoarea lui k cu 0,1 de fiecare dată și răspundeți la 
% următoarele întrebări.
% a) La ce valoare a lui K începem să avem dificultăți în a 
% înțelege conținutul redat?
% b) Se trasează formele de undă la valori diferite ale lui k. 
% La ce valoare a lui k vom începe să avem dificultăți în a 
% identifica perioada fundamentală ?

fs=8000; % Frecventa de esantionare
t=5;
numarBits = 8; % Rezolutia
numarCanale = 1; % Nr canale
fprintf('Apasa tasta t pentru a incepe o inregistrare de %g secunde',t);
pause;

fprintf('\nA inceput inregistrarea');
recorded_audio = audiorecorder(fs,numarBits,numarCanale);
record(recorded_audio,t);
fprintf('\nGata de inregistrat.\n');

fprintf('Apasa tasta t pentru a salva inregistrarea in %s... \n', t);
pause;
file = 'numele_meu_2.wav';
w = getaudiodata(recorded_audio, 'int16'); 
audiowrite(file,w,fs);
fprintf('Fisierul a fost salvat %s\n', file);

[y, fs]=audioread('numele_meu_2.wav');
p = audioplayer(y, fs);
play(p);
pause(5)

k = 0;
y2 = y + k * randn(length(y), 1);
sound(y2, fs);
plot(y2);

