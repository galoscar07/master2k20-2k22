# -*- coding: utf-8 -*-
"""
Created on Sat May  9 20:01:46 2020

@author: Florea.Camelia
"""
import itertools
from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
from random import random

def ImageIllustrationOriginalDataSet(X, y, cls_labels):
    nrCls = len(cls_labels)
    print(' Labels, ', nrCls, ' classes: ', cls_labels)
   
    cols = 10; line = nrCls; pl = 1;
    fig = plt.figure(figsize=(cols*1.6,line*2.2))
    for i in range(0, line):
        X_ci = X[ y == i]
        for j in range (0, cols):
            fig.add_subplot(line,cols, (i*cols+j+1)); #pl=pl+1;
            rdmImg = int(random()* X_ci.shape[0])
            plt.imshow(X_ci[rdmImg], cmap=plt.cm.bone); plt.title(str([rdmImg, cls_labels[i]]))
    plt.show();

def ImageIllustrationPredictionResults(X, y, y_pred, cls_labels): 
    nrCls = len(cls_labels)
    pozErr = (y != y_pred) # errors in label prediction
    X_err = X [pozErr]
    y_err_or = y[pozErr]
    y_err_pr = y_pred[pozErr]
    print("Set date/imagini eronate: ", X_err.shape)
    
    lines = 4
    cols = max(nrCls, 10)
    fig = plt.figure(figsize=(cols*1.6,lines*2.2))
    for i in range(0, min(lines*cols, X_err.shape[0])):
      fig.add_subplot(lines, cols, i+1); plt.imshow(X_err[i], cmap=plt.cm.bone); 
      plt.title([str(y_err_or[i]) + '/ p:' + str(y_err_pr[i])]);
    plt.show()


def ImagePlotConfusionMatrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
  """
  This function prints and plots the confusion matrix.
  Normalization can be applied by setting `normalize=True`.
  """
  if normalize:
      cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
      print("Normalized confusion matrix")
  else:
      print('Confusion matrix, without normalization')

  # print(cm)

  plt.imshow(cm, interpolation='nearest', cmap=cmap)
  plt.title(title)
  plt.colorbar()
  tick_marks = np.arange(len(classes))
  plt.xticks(tick_marks, classes, rotation=45)
  plt.yticks(tick_marks, classes)

  fmt = '.2f' if normalize else 'd'
  thresh = cm.max() / 2.
  for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
      plt.text(j, i, format(cm[i, j], fmt),
               horizontalalignment="center",
               color="white" if cm[i, j] > thresh else "black")

  plt.tight_layout()
  plt.ylabel('True label')
  plt.xlabel('Predicted label')
  plt.show()

def EvalModelCls(y_a, y_a_pred, y_b, y_b_pred, ta, tb):
    acc_a = np.round(metrics.accuracy_score(y_a, y_a_pred),5)
    acc_b =np.round(metrics.accuracy_score(y_b, y_b_pred),5)
    cf_a = metrics.confusion_matrix(y_a, y_a_pred)
    cf_b = metrics.confusion_matrix(y_b, y_b_pred)
    
    tabel = []
    for i in range (0,cf_a.shape[0]):
        tabel.append([str(cf_a[i,:]), str(cf_b[i,:])])
    headers=[ta+", Accuracy: "+str(acc_a)+",\n Confusion Matrix: ", 
             tb+", Accuracy: "+str(acc_b)+",\n Confusion Matrix: "]
    print(tabulate(tabel, headers, colalign=("center","center")))
    return [acc_a, acc_b, cf_a, cf_b]  

def EvalModelCls(y_a, y_a_pred, ta):
    acc_a = np.round(metrics.accuracy_score(y_a, y_a_pred),5)
    cf_a = metrics.confusion_matrix(y_a, y_a_pred)
    
    tabel = []
    for i in range (0,cf_a.shape[0]):
        tabel.append([str(cf_a[i,:])])
    headers=[ta+", Accuracy: "+str(acc_a)+",\n Confusion Matrix: "]
    print(tabulate(tabel, headers));
    return [acc_a, cf_a]  

def PlotModelHistoryEpoch(histModel):
    print(histModel.history.keys())
    
    # plot some data
    
    # loss
    plt.plot(histModel.history['loss'], label='train loss')
    plt.plot(histModel.history['val_loss'], label='val loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend()
    plt.show()
    
    # accuracies
    plt.plot(histModel.history['accuracy'], label='train acc')
    plt.plot(histModel.history['val_accuracy'], label='val acc')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend()
    plt.show()

# from sklearn import metrics
# cm = metrics.confusion_matrix(y_test,predictions)
# #import plot_confusion_matrix
# # plot_confusion_matrix(y_test,predictions, title='Train confusion matrix')
# plot_confusion_matrix(cm,y_label_names,  title='Validation confusion matrix')