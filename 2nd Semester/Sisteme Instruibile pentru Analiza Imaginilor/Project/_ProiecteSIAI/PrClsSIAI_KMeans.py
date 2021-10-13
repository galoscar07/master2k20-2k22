# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 13:16:04 2020
Inspirat de la:
https://jakevdp.github.io/PythonDataScienceHandbook/05.11-k-means.html 
@author: Florea.Camelia
"""

import matplotlib.pyplot as plt
import seaborn as sns; 
import numpy as np
import itertools
from random import random
from sklearn.cluster import KMeans

# -----------------------------------------------------------------------------------
# definirea unei functii pentru afisare matrice de confuzie
def ImagePlotConfusionMatrix(cm, classes, title, normalize=False, cmap=plt.cm.Blues):
  """
  This function prints and plots the confusion matrix.
  Normalization can be applied by setting `normalize=True`.
  """
 
  plt.imshow(cm, interpolation='nearest', cmap=cmap)
  plt.title(title); plt.colorbar(); tick_marks = np.arange(len(classes))
  plt.xticks(tick_marks, classes, rotation=45); plt.yticks(tick_marks, classes)

  fmt = '.2f' if normalize else 'd'
  thresh = cm.max() / 2.
  for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
      plt.text(j, i, format(cm[i, j], fmt), horizontalalignment="center",
               color="white" if cm[i, j] > thresh else "black")

  plt.tight_layout(); plt.ylabel('True label'); plt.xlabel('Predicted label'); plt.show();
# -----------------------------------------------------------------------------------
# In[0] Incarcare baza de date 

# from sklearn.datasets import load_breast_cancer
# dsXy = load_breast_cancer()

# from sklearn.datasets import load_iris
# dsXy = load_iris()

from sklearn.datasets import load_digits
dsXy = load_digits()

# Vizualizare structura dataset -  dsXy.keys()
print(' Dataset loaded! ', dsXy.keys())
print('     - dsXy.data.shape', dsXy.data.shape)

# Vectorul de trasaturi X si label-urile y
X = dsXy.data; 
y = dsXy.target;

# Verificam daca datele au etichete nume/string 
# sau valori numerice (se obtin automat ca valori unice in y) 
if ('target_names' in dsXy.keys()): cls_labels = dsXy.target_names
else: cls_labels = np.unique(y).astype(str);

# Stabilire numar clase pentru setul de date incarcat
nrCls = len(cls_labels);
print(' Numar clase: ', nrCls)
print(' Etichete: ', cls_labels)

# Afisare imagini, doar daca baza de date contine imaginile!!!
if ('images' in dsXy.keys()): 
    # setul de date are incarcate si imaginile 
    # (nu doar descrire prin trasaturi)

    Ximg = dsXy.images; 
    print(' Imaginile au rezolutia: ', Ximg.shape[1],'x', Ximg.shape[2] )
    print(' Afisare imagini (random) din setul de date:',
          ' \n - pe fiecare linie o clasa diferita',
          ' \n - pe coloane - 10 exemple din acceasi clasa ')
    cols = 10; line = nrCls; pl = 1;
    fig = plt.figure(figsize=(cols*1.2,line*1.8))
    for i in range(0, line):
        X_ci = Ximg[ y == i]
        for j in range (0, cols):
            fig.add_subplot(line,cols, (i*cols+j+1)); #pl=pl+1;
            rdmImg = int(random()* X_ci.shape[0])
            plt.imshow(X_ci[rdmImg], cmap=plt.cm.bone); plt.title(str([rdmImg, cls_labels[i]]))
    plt.show();

# In[1] Divizare dataset in - Training set / Test set

# KMeans este un clasificator nesupervizat 
# NU exista faza de antrenare si faza de testare    

# In[2] Preprocesare date X
# from sklearn.preprocessing import StandardScaler

# # Scalare date in acelasi interval
# print(' Scalare/normare date: ')
# print('  - Interval original: [', X[0].min(), ' ; ', X[0].max(),']')
# sc = StandardScaler()
# X = sc.fit_transform(X) # scalare in functie de setul de train

# print('  - Interval normalizat: [',round(X[0].min(),2),' ; ', round(X[0].max(),2), ']')

# In[3] Creare model, antrenare pe setul de date, si testare
# Aplicare KMeans
model_kmeans = KMeans(n_clusters = nrCls, random_state=0)
clusters = model_kmeans.fit_predict(X)
print(' KMeans - cluster centers')
print('     - kmeans.cluster_centers_.shape', model_kmeans.cluster_centers_.shape)

 # Afisare centrelor claselor KMeans
if ('images' in dsXy.keys()): 
    print('     - digits.images.shape', dsXy.images.shape)
    centers_image = model_kmeans.cluster_centers_.reshape(model_kmeans.n_clusters, dsXy.images.shape[1], dsXy.images.shape[2])
    
    fig, ax = plt.subplots(1, model_kmeans.n_clusters, figsize=(model_kmeans.n_clusters*1.6, 3))
    
    for axi, center in zip(ax.flat, centers_image):
        axi.set(xticks=[], yticks=[])
        axi.imshow(center, cmap=plt.cm.bone)
    plt.show()
# In[4] Evaluare rezultate

from scipy.stats import mode

# se coreleaza labelurile returnate de KMeans cu cele reale
labels = np.zeros_like(clusters)
for i in range(model_kmeans.n_clusters):
    mask = (clusters == i)
    labels[mask] = mode(y[mask])[0] # returneaza cele mai frecvente valori dintr-un vector

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

print( " \n ------ Evaluare performante clasificator ------ ")
# print( "accuracy: ", accuracy_score(dsXy.target, labels))
cm = confusion_matrix(y, labels)
fig = plt.figure(figsize=(16, 6))
ImagePlotConfusionMatrix(cm, cls_labels, "CM")
print('    Classification report: \n\n', classification_report(y, labels))

# In[] Optizare descriere date prin aplicare TSNE 

from sklearn.manifold import TSNE

# Project the data: this step will take several seconds
tsne = TSNE(n_components=2, init='random', random_state=0)
X_tsne = tsne.fit_transform(X)

print("\n*********************************************************\n")
print( " DUPA aplicare TSNE !!!")
print(" Vectorul de trasaturi, X_tsne.shape: ", X_tsne.shape)

# Compute the clusters
model_kmeans_tnse = KMeans(n_clusters= nrCls, random_state=0)
clusters = model_kmeans_tnse.fit_predict(X_tsne)

# Permute the labels
labels = np.zeros_like(clusters)
for i in range(10):
    mask = (clusters == i)
    labels[mask] = mode(y[mask])[0]

print( " \n ------ Evaluare performante clasificator ------ ")
# Compute the accuracy
# print( "accuracy: ", accuracy_score(dsXy.target, labels))
cm = confusion_matrix(y, labels)
fig = plt.figure(figsize=(16, 6))
ImagePlotConfusionMatrix(cm, cls_labels, "CM, optimizat")
print('    Classification report: \n\n', classification_report(y, labels))
