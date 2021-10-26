% Obțineți informații dintr-un fișier audio mono. Scrieti un script MATLAB
% care poate citi fisierul "church.wav" și va afișa următoarele informații 
% în acest script:
%
% Numărul de puncte de eșantionare.
% Rata esantionare
% Rezoluție Biti
% Numărul de canale
% Durata de timp a înregistrării (în secunde)

[y, fs]=audioread('church.wav');
info=audioinfo('church.wav')
