# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 10:03:36 2020

@author: Florea.Camelia
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# In[] Formare setul de date: X, y

df = pd.read_csv("datasets/ClassifiedDataCompanyPD",index_col=0)
print(df.head())

X = df.drop('TARGET CLASS',axis=1)
y = df['TARGET CLASS']

print('  X.shape ', X.shape)
print('  y.shape ', y.shape)

# In[] 
df = pd.read_csv("datasets/College_Data",index_col=0)
print(df.head())

X = df.drop('Private',axis=1)
y = df['Private']

print('  X.shape ', X.shape)
print('  y.shape ', y.shape)

target_names = np.unique(y); # numele florilor de iris diferite
print(target_names)
# Etichetare cu valori numerice a claselor 

print(y[df['Private']=='Yes'].shape)
print(y[df['Private']=='No'].shape)
