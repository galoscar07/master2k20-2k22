# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 13:59:09 2019

@author: Camelia
"""

#import os
import numpy as np
import matplotlib.pyplot as plt
#import cv2

def SingleCompHistoThd(CompPr,FiltWindowLen,MinMaxDif):

    fig = plt.figure(figsize=(20,2)); 
    counts, bins = np.histogram(CompPr, range(256))
    fig.add_subplot(1,2,1)
    plt.bar(bins[:-1], counts, width=1, edgecolor='none'); plt.xlim([-0.5, 255.5]); 
    plt.title('Histograma 1-D a componentei alese pt segmentare')
    
    # Filtrare histograma
    from scipy.signal import medfilt
    CountHistFilt = medfilt(counts, FiltWindowLen)
    CountHistFilt[CountHistFilt<20] = 0
    #  Calcul minime si maxime locale 
    [LocMax,LocMin] = peakdet(CountHistFilt, MinMaxDif);
    print('LocMax shape: ', LocMax.shape, ';  LocMin shape: ', LocMin.shape)
    
    fig.add_subplot(1,2,2)
    plt.bar(bins[:-1], CountHistFilt, width=1, edgecolor='none'); plt.xlim([-0.5, 255.5]); 
    plt.plot(LocMin[:,0],LocMin[:,1], 'y*');
    plt.plot(LocMax[:,0],LocMax[:,1], 'r*');
    plt.title('Histograma filtrata si cu localizarea minimelor si maximelor locale')
    return [LocMin,LocMax]

def peakdet(CountHistFilt, MinMaxDif):
    delta = 50
    maxtab = [];
    mintab = [];
    
    v = CountHistFilt[:];# % Just in case this wasn't a proper vector
    mn = 2552222; mx = 0;
    mnpos = 0; mxpos = 0;
    
    lookformax = 1;
    
    for i in range(0,len(v)):
        this = v[i];
        if this > mx: mx = this; mxpos = i; 
        if this < mn: mn = this; mnpos = i; 
      
        if lookformax:
            if this < mx-delta:
                maxtab.append([mxpos, mx]);
                mn = this; mnpos = i;
                lookformax = 0;  
        elif this > mn+delta:
            mintab.append([mnpos, mn]);
            mx = this; mxpos = i;
            lookformax = 1;

    mintab = np.array(mintab)
    maxtab = np.array(maxtab)
    
    '''
    loc = np.where(CountHistFilt>0)
    T1 = loc[0][0]; T2 = loc[0][-1]
    if (mintab.shape[0] == 0 ):
        mintab = np.concatenate((np.array([[T1, CountHistFilt[T1]]]), 
                                 np.array([[T2, CountHistFilt[T2]]])), axis=0)
    else:  
        mintab = np.concatenate((np.array([[T1, CountHistFilt[T1]]]), 
                                 mintab, 
                                 np.array([[T2, CountHistFilt[T2]]])), axis=0)
    '''
    if (mintab.shape[0] == 0 ):
        mintab = np.array([[0, 0],[255,0]])
    else:  
        mintab = np.concatenate((np.array([[0, 0]]), 
                                 mintab, 
                                 np.array([[255, 0]])), axis=0)
    return [maxtab, mintab]
  
def segmMinMaxRegions(CompPr,LocMax,LocMin):
    
    # Segmentarea imaginii cu praguri determinate de minimele locale obtinute.
    COutMax = np.zeros(CompPr.shape,'uint8'); COutUni = np.zeros(CompPr.shape,'uint8');
    
    for k in range(LocMin.shape[0]-1):
        pozD = np.where((CompPr>=LocMin[k,0])&(CompPr<=LocMin[k+1,0]));
        COutMax[pozD[0],pozD[1]] =  LocMax[k,0]; 
        COutUni[pozD[0],pozD[1]] = ((k)/(LocMin.shape[0]-1) * 220);         
    
    fig = plt.figure(figsize=(10,10)); 
    
    
    fig = plt.figure(figsize=(20,10)); 
    fig.add_subplot(121); plt.imshow(COutMax, cmap = 'gray', vmin=0, vmax=255);plt.title('Imaginea Segmentatã, etichetare prin maximul local');
    fig.add_subplot(122); plt.imshow(COutUni, cmap = 'gray', vmin=0, vmax=255);plt.title('Imaginea Segmentatã, etichetare prin intensitati/culori egal distantate');
    plt.show()
    
    fig = plt.figure(figsize=(20,2)); 
    fig.add_subplot(121); plt.hist(COutMax.ravel(),256,[0,256]); plt.title('Histograma dupã segmentare, etichetare prin maximul local');
    fig.add_subplot(122); plt.hist(COutUni.ravel(),256,[0,256]); plt.title('Histograma dupã segmentare, distributie uniforma a etichetelor');
    plt.show()
    
    return [COutMax,COutUni]
    
    
'''





[CountHistSegMax, ValsHistSegMax] = imhist(COutMax);
[CountHistSegUni, ValsHistSegUni] = imhist(COutUni);

%afisare histograma componenta procesata, inainte si dupa segmentare:
figure(1); 
subplot(2,2,1); plot(ValsHist,CountHist); ylim([0 max(CountHist)]); title('Histograma originala');
subplot(2,2,2); plot(ValsHist,CountHistFilt); ylim([0 max(CountHist)]); title('Histograma netezita');
hold on; plot( ValsHist(LocMin(:,1)), LocMin(:,2), 'g*');
hold on; plot( ValsHist(LocMax(:,1)), LocMax(:,2), 'r*');
subplot(2,2,4); stem(ValsHistSegMax, CountHistSegMax, '-b.'); title('Histograma dupã segmentare, etichetare prin maximul local');
subplot(2,2,3); stem(ValsHistSegUni, CountHistSegUni, '-b.'); title('Histograma dupã segmentare, distributie uniforma a etichetelor');

%determinarea conturului regiunilor segmentate
ImOutEdge=255-uint8(edge(COutUni,'canny')*255); 
% Revenirea la spatiul de culoare RGB 
ImOutMax = zeros(size(A), 'uint8') + 128; ImOutUni = zeros(size(A), 'uint8') + 128;
ImOutMax(:,:,ClrComp) = COutMax; ImOutUni(:,:,1) = COutUni; ImOutUni = hsv2rgb(double(ImOutUni)./255); 
switch ClrSpace
    case 'YCbCr',      ImOutMax = ycbcr2rgb(ImOutMax);
    case 'HSV',        ImOutMax=uint8(255*hsv2rgb(double(ImOutMax)/255));
end;

%afisare imagine inainte si dupã segmentare
figure(2); 
subplot(3,3,1); imshow(CompPr); title(['Componenta procesata ' ClrSpace ' ' num2str(ClrComp)]);
subplot(3,3,2); imshow(COutMax); title('Imaginea Segmentatã, etichetare prin maximul local');
subplot(3,3,3); imshow(COutUni); title('Imaginea Segmentatã, etichetare prin intensitati/culori egal distantate');
subplot(3,3,4); plot(ValsHist,CountHist); ylim([0 max(CountHist)]); 
% subplot(3,3,4); plot(ValsHist,CountHistFilt); ylim([0 max(CountHist)]); title('histograma netezita');
subplot(3,3,5); stem(ValsHistSegMax, CountHistSegMax, '-b.'); 
subplot(3,3,6); stem(ValsHistSegUni, CountHistSegUni, '-b.'); 
subplot(3,3,7); imshow(A); title('Imaginea de intrare');
%Afisarea imaginii segmentate
subplot(3,3,8);  imshow(ImOutMax); title('Imaginea Segmentatã, etichetare color prin maximul local');
subplot(3,3,9);  imshow(ImOutUni); title('Imaginea Segmentatã, etichetare prin culori egal distantate');

%afisarea conturului regiunilor imaginii segmentate:
figure(3);
% subplot(2,1,1); imshow(A); 
% subplot(2,2,3); imshow(ImOutUni); 
% subplot(2,2,4); 
imshow(ImOutEdge); title('conturul regiunilor imaginii segmentate');

figure(4); 
subplot(2,3,1); imshow(CompPr); title(['Componenta procesata ' ClrSpace ' ' num2str(ClrComp)]);
subplot(2,3,2); imshow(COutMax); title('Imaginea Segmentatã, etichetare prin maximul local');
subplot(2,3,3); imshow(COutUni); title('Imaginea Segmentatã, etichetare prin intensitati/culori egal distantate');
subplot(2,3,4); imshow(A); title('Imaginea de intrare');
%Afisarea imaginii segmentate
subplot(2,3,5);  imshow(ImOutMax); title('Imaginea Segmentatã, etichetare color prin maximul local');
subplot(2,3,6);  imshow(ImOutUni); title('Imaginea Segmentatã, etichetare prin culori egal distantate');


'''