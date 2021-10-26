# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 11:28:50 2019

@author: Camelia Florea
"""
#import os
import numpy as np
import cv2 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# functiile necesare in aplicatie
def ConvertColorSpace(ImgOrg, OrgColorSpace, NewColorSpace):
    # Conversie din Spatiu de culoare original RGB intr-un alt spatiu de culoare
    # Sau revenite la spatiu RGB de la un alt spetiu
    if (OrgColorSpace == 'R/G/B'):  # conversie din RGB intr-un alt spatiu de culoare
        if (NewColorSpace == 'Y/Cr/Cb'): ImgCvt = cv2.cvtColor(ImgOrg, cv2.COLOR_RGB2YCrCb)
        elif (NewColorSpace == 'H/S/V'): ImgCvt = cv2.cvtColor(ImgOrg, cv2.COLOR_RGB2HSV)
        elif (NewColorSpace == 'L/a/b'): ImgCvt = cv2.cvtColor(ImgOrg, cv2.COLOR_RGB2Lab)
    elif (NewColorSpace == 'R/G/B'): # revenire la RGB - necesar pentru afisare corecta a imaginii
        if (OrgColorSpace == 'Y/Cr/Cb'): ImgCvt = cv2.cvtColor(ImgOrg, cv2.COLOR_YCrCb2RGB)
        elif (OrgColorSpace == 'H/S/V'): ImgCvt = cv2.cvtColor(ImgOrg, cv2.COLOR_HSV2RGB)
        elif (OrgColorSpace == 'L/a/b'): ImgCvt = cv2.cvtColor(ImgOrg, cv2.COLOR_Lab2RGB)
    return ImgCvt

def plotColorComponents(imgInColorSpace, clrSpName):
    # Afisarea celor 3 componente de culoare sub forma unei imagini 
    compName = clrSpName.split('/') # Extragere nume componente
    fig = plt.figure(figsize=(20,10))
    for i in range(0,3):
        fig.add_subplot(1,3,i+1)
        plt.imshow(imgInColorSpace[:,:,i], cmap='gray', vmin=0, vmax=255)
        plt.title('Componenta ' + compName[i])
    plt.show()
    
def plotColorHistograms(imgInColorSpace, clrSpName):
     # Afisarea histograme celor 3 componente de culoare 
    compName = clrSpName.split('/') # Extragere nume componente
    fig = plt.figure(figsize=(20,2))
    color = ('r','g','b')
    for i,col in enumerate(color):
        histr = cv2.calcHist([imgInColorSpace],[i],None,[256],[0,256])
        fig.add_subplot(1,3,i+1)
        plt.plot(histr,color = col)
        plt.title('Componenta ' + compName[i])
        plt.xlim([0,256])
    plt.show()
    
def plot3DcolorSpace(imgClrSp, imgOrg, clrSpName):
    print('\n Afisare Cub Culori in spatiu de culoare: ', clrSpName ) 
    imgClrSpRed = np.reshape(imgClrSp,(imgClrSp.shape[0]*imgClrSp.shape[1] ,imgClrSp.shape[2]))
    imgOrgRed = np.reshape(imgOrg,(imgOrg.shape[0]*imgOrg.shape[1] ,imgOrg.shape[2]))
    uniqvals, indices = np.unique(imgClrSpRed, axis = 0, return_index=True)
    print('\n Numar culori unice care apar in imagine: ',uniqvals.shape[0], 'din 2^24(',2**24,')', 
          '; procent: ', round(100*(uniqvals.shape[0]/2**24),4), '% acoperire cub')
    nrVals = uniqvals.shape[0]
    pas = int(nrVals/3000)+1
    #pas = 1
    uniqvals = uniqvals[range(0, nrVals, pas), :].copy()
    cli = imgOrgRed[indices[range(0, nrVals, pas)],:].astype(float)/255
    fig = plt.figure(figsize=(20,10)) 
    ax = fig.add_subplot(1,2,1, projection='3d')
    ax.scatter(uniqvals[:,2], uniqvals[:,1], uniqvals[:,0], c=cli, marker='.')
    ax.set_xlim([0,256]); ax.set_ylim([0,256]); ax.set_zlim([0,256])
    compName = clrSpName.split('/') 
    ax.set_xlabel('Componenta '+ compName[2]); ax.set_ylabel('Componenta '+ compName[1]); ax.set_zlabel('Componenta '+ compName[0])
    ax1 = fig.add_subplot(1,2,2)
    ax1.imshow(imgOrg)
    ax1.set_title('Imaginea originala RGB')
    plt.show()

def plot2DcolorSpace(imgClrSp, imgOrg, clrSpName, selCrom):
    
    print('\n Afisare Componente Crominata in spatiu de culoare: ', clrSpName) 
    compName = clrSpName.split('/') 
    imgClrSpRed = np.reshape(imgClrSp,(imgClrSp.shape[0]*imgClrSp.shape[1] ,imgClrSp.shape[2]))
    imgOrgRed = np.reshape(imgOrg,(imgOrg.shape[0]*imgOrg.shape[1] ,imgOrg.shape[2]))
    c=0;RetComp = np.zeros((imgOrg.shape[0]*imgOrg.shape[1], 2))
    compNameRet = [0, 0]
    for i in range (0,3):
        if (selCrom[i] == 1):
            RetComp[:,c] = imgClrSpRed[:,i];
            compNameRet[c] = compName[i]
            c = c+1
            
    uniqvals, indices = np.unique(RetComp, axis = 0, return_index=True)
    print('\n Numar culori unice care apar in imagine: ',uniqvals.shape[0])
    nrVals = uniqvals.shape[0]
    pas = int(nrVals/3000)+1
    #pas = 1
    uniqvals = uniqvals[range(0, nrVals, pas), :].copy()
    cli = imgOrgRed[indices[range(0, nrVals, pas)],:].astype(float)/255
    fig = plt.figure(figsize=(20,7)) 
    ax = fig.add_subplot(1,2,1)
    ax.scatter(uniqvals[:,1], uniqvals[:,0], c=cli, marker='.')
    ax.set_xlim([0,256]); ax.set_ylim([0,256]);
    ax.set_xlabel('Componenta '+ compNameRet[1]); ax.set_ylabel('Componenta '+ compNameRet[0]); #ax.set_zlabel('Componenta '+ compName[0])
    ax1 = fig.add_subplot(1,2,2)
    ax1.imshow(imgOrg)
    ax1.set_title('Imaginea originala RGB')
    plt.show()