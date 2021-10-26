,# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 10:36:02 2020
Template proiect
@author: Florea.Camelia
"""
import itertools
import matplotlib.pyplot as plt  
from random import random
import numpy as np
# In[0] Incarcare baza de date 

from sklearn.datasets import load_breast_cancer
dsXy = load_breast_cancer()

# from sklearn.datasets import load_iris
# dsXy = load_iris()

# from sklearn.datasets import load_digits
# dsXy = load_digits()


# Vizualizare structura dataset -  dsXy.keys()
print(' Dataset loaded! ', dsXy.keys())
print('     - digits.data.shape', dsXy.data.shape)

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
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 101)

print(' Setul de date vor fi impartite: \n  - ', X_train.shape[0],' train \n  - ',  X_test.shape[0],' test' )

# In[2] Preprocesare date X
from sklearn.preprocessing import StandardScaler

# Scalare date in acelasi interval
print(' Scalare/normare date: ')
print('  - Interval original: [', X_train[0].min(), ' ; ', X_train[0].max(),']')
sc = StandardScaler()
X_train = sc.fit_transform(X_train) # scalare in functie de setul de train
X_test = sc.transform(X_test) # aplicare si pe setul de test
print('  - Interval normalizat: [',round(X_train[0].min(),2),' ; ', round(X_train[0].max(),2), ']')
# In[3] Creare model, antrenare pe setul de date, si testare

from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

# definire/modelare clasificator

opt_par_svm = False; # True or False
if (not(opt_par_svm)):
    nkernel =  'linear' #  'linear','poly', 'rbf'
    model_svm = SVC(kernel = nkernel, random_state = 0)
    model_svm.fit(X_train, y_train)
    print(' Model SVM - kernel:', model_svm.kernel,', gamma:', model_svm.gamma,
          ', C: ', model_svm.C,', degree: ', model_svm.degree)
else: 
    print(' S-a ales optimizare parametri SVM !!!!')
    param_grid = {'kernel':['linear', 'rbf','poly'], 
                  'degree':[2,3],
                  'C': [0.1,1, 10, 100], 
                  'gamma': [100, 10,1,0.1,0.01,0.001]} 
    model_svm = GridSearchCV(SVC(),param_grid,refit=True,verbose=1)
    model_svm.fit(X_train, y_train)
    print(' Parametrii optimi obtinuti: ', model_svm.best_params_)


#antrenare clasificator folosind setul de date de antrenament
model_svm.fit(X_train, y_train)

# predictie pe setul de antrenare
y_train_pred = model_svm.predict(X_train)

# predictie pe setul de test
y_test_pred = model_svm.predict(X_test)

# In[4] Evaluare rezultate
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

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

print( " \n ------ Evaluare performante clasificator ------ ")

print(' \n   Classification report - train dataset : \n\n', classification_report(y_train, y_train_pred))
fig = plt.figure(figsize=(16, 6))
cm_train = confusion_matrix(y_train, y_train_pred)
ImagePlotConfusionMatrix(cm_train, cls_labels, 'Confusion matrix train dataset')

print(' \n   Classification report - test dataset: \n\n', classification_report(y_test, y_test_pred))
fig = plt.figure(figsize=(16, 6))
cm_test = confusion_matrix(y_test, y_test_pred)
ImagePlotConfusionMatrix(cm_test, cls_labels, 'Confusion matrix test dataset')
