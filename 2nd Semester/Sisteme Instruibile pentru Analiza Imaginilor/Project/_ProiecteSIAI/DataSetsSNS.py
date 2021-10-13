# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 21:02:33 2020

@author: Florea.Camelia
"""

import numpy as np
import seaborn as sns
print(sns.get_dataset_names())



# In[] Formare setul de date: X, y
dsXy = sns.load_dataset('iris') 
X = dsXy.drop('species',axis=1); 
target_names = np.unique(dsXy['species']); # numele florilor de iris diferite

# Etichetare cu valori numerice a claselor 
y = np.zeros(X.shape[0],).astype(int);
y[dsXy['species']=='setosa'] = 0
y[dsXy['species']=='versicolor'] = 1
y[dsXy['species']=='virginica'] = 2


# In[] Formare setul de date: X, y
dsXy = sns.load_dataset('tips') 

# In[] Formare setul de date: X, y
dsXy = sns.load_dataset('brain_networks') 
X = dsXy.drop('species',axis=1); 
target_names = np.unique(dsXy['species']); # numele florilor de iris diferite

# Etichetare cu valori numerice a claselor 
y = np.zeros(X.shape[0],).astype(int);
y[dsXy['species']=='setosa'] = 0
y[dsXy['species']=='versicolor'] = 1
y[dsXy['species']=='virginica'] = 2

print('\n Clasele: ', target_names)
print(' Set date, X.shape ', X.shape)
