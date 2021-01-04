% 4.3. Manipularea semnalului audio: Scrieți un script MATLAB pentru a 
% înregistra rostirea ta de "azi e ziua mea de naștere". Încercați să 
% explicați efectul de redare observați după ce încercați următoarele 
% operații asupra semnalelor audio:
% Inmultiti semnalele audio cu -1.
% Inversati semnalele audio pe axa timpului.
% Inmultiti semnalele audio cu 10.
% Înlocuiți fiecare esantion cu rădăcină sa pătrată.
% Înlocuiți fiecare esantion cu pătratul său.
% Taierea/limitarea semnalului, astfel încât eșantioanele din gama 
%      [-0.5, 0.5] sunt setate la zero.
% Modificati forma de undă astfel încât eșantioanele din intervalul 
%      [-0.5, 0.5] sunt setate la zero, iar eșantioanele din afara 
%      gamei de [-0.5, 0.5] sunt mutate spre zero, cu cantitatea de 0,5.

fs=16000; % Frecventa de esantionare
t=5;
nBits = 16; % Rezolutia
nChannels = 1; % Nr canale
fprintf('Apasa tasta t pentru a incepe o inregistrare de %g secunde',t);
pause;

fprintf('A inceput inregistrarea');
recorded_audio = audiorecorder(fs,nBits,nChannels);
record(recorded_audio,t);
fprintf('Gata de inregistrat.\n');

fprintf('Apasa tasta t pentru a salva inregistrarea in %s... \n', t);
pause;
file = 'aniversare.wav';
w = getaudiodata(recorded_audio, 'int16'); 
audiowrite(file,w,fs);
fprintf('Fisierul a fost salvat %s\n', file);

[y, fs]=audioread('aniversare.wav');
sound = audioplayer(y, fs);
play(sound);
pause(5);

% inversare pe axa timpului
s = flipud(y);
p = audioplayer(s, fs);
play(p);

pause(3)

% inversare pe axa timpului a semnalului inversat pentru verificare
s2 = flipud(s); 
p = audioplayer(s2, fs);
play(p);
pause(5)

file = audioplayer(10*y, fs);
play(file);
pause(5)

for i = 1:length(y)
    s(i) = sqrt(y(i));
end
file = audioplayer(s, fs);
    play(file);
pause(5)    
    
for i = 1:length(y)
    s(i) = y(i)^2;
end
file = audioplayer(s, fs);
    play(file);
pause(5)


for i = 1:length(y)
    if y(i) >= -0.5 && y(i) <= 0.5
        s(i) = 0;
    else s(i) = y(i);
    end
end

file = audioplayer(s, fs);
play(file);
pause(5)


for i = 1:length(y)
    if y(i) >= -0.5 && y(i) <= 0.5
        s(i) = 0;
    elseif y(i) < 0
        s(i) = y(i) + 0.5;
    elseif y(i) > 0
        s(i) = y(i) -0.5;
        
    end
end
file = audioplayer(s, fs);
play(file);