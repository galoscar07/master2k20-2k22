#! Exemplificare eigenfaces: PCA, Recunostere faciala, SVM, NN 
# =============================================
# 
# Scopul acestei lucrari este de a ilustra cum o metoda nesupervizata si o metoda 
# supervizata pot fi combinate pentru o predictie mai buna.
# 
# Sunt prezentate doua abordari de implementare:
#   - aplicare explicita, cu scop didactic a pasilor PCA
#   - abordare idiomatica (idiomatic approach), prin pipeline
# 
# Vom urmari un exemplu simplu pentru recunoastere faciala. 
# Baza de date utilizata contine fete etichetate (cunoastem cine apare in imagine).
# 
# Baze de date recomandate:
#   - vom rula programul pe o baza de date simpla, cu un numar redus de date, 
#     cu scop didactic - pentru rapiditate la incarcare/ procesare: 
#     disponibila in pachetul `sklearn.datasets.fetch_olivetti_faces`
#     
#   - o baza de date mai complexa (13233, 2914): 
#     disponibila in pachetul `sklearn.datasets.fetch_lfw_people` (~200MB)
# 
# Pentru a intelege mai usor modul de interpretare clasificarea datelor de citit:
#       Compute precision, recall, F-measure and support for each class  
# https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html   

# @authors: Camelia Florea & Mihaela Gordan
#    Research group IMIPA/ ETTI/ UTCN
# (Intelligent and Multimodal Image Processing and Analysis)    
# In[1]: Incarcarea setului de date
import sys
sys.path.append('../_PyUtilFcts/')
import UtilsPredictionResults as upr
import matplotlib.pyplot as plt

from sklearn import datasets

# Load data
# faces = datasets.fetch_olivetti_faces()
faces = datasets.fetch_lfw_people(min_faces_per_person=100)


# In[2]: Urmarire mod reprezentare date
import numpy as np
print('\n Mod stucturare informatie in variabila face: \n\t', faces.keys() ) 

print(' Numarul de imagini si rezolutia imaginilor [N, H, W]: \n\t', faces.images.shape)
print(' Rerprezentare 1D a imaginilor, prin scanare linie cu linie [N, W*H]: \n\t', faces.data.shape)

# Vectorul de date X
# Vectorul cu etichetele numerice y 
X = faces.data 
y = faces.target 

# Verificam daca baza de date contine numele persoanelor
# Daca da, ne vom referi la date dupa numele persoanei
# Daca nu, ne referim la date sub forma unei etichete numerice 
if ('target_names' in faces.keys()): target_names = faces.target_names
else: target_names = np.unique(y).astype(str);

# Pentru partea de procesare fiecare persoana are alocata cate o eticheta numerica  (y)

# Notam in RaportO365: 
#      - Nume Set de Date 
#      - Toate informatie despre baza de date afisate in consola 
print('\n -------------------------------------------------------------------')
# In[3]: Vizualizare imagini din setul de date
# O sa vizualizam o parte din imaginile din set pentru a vedea cum arata imaginile cu care lucram.
upr.ImageIllustrationOriginalDataSet(faces.images, y, target_names)

# Observatie - toate aceste imagini sunt preprocesate prin:
#   - decupare zona faciala si 
#   - redimensionare la o rezolutie comuna.

# Notam in RaportO365: 
#      - printscreen cu fetele afisate in 'IPython console'
#      - specificare ordine in care apar imaginile in baza de date 
#       (ordonate dupa persoana sau aleator) - verifica variabila y in 'Variable Explorer'
print('\n -------------------------------------------------------------------')
# In[4]: # Pregatire set date 
# 
# Tinand cont ca o sa aplicam o clasificare pe acest set de date, 
# in faza de antrenare nu trebuie sa tinem cont deloc de datele de la test. 
# 
# Astfel, setul de date o sa fie impartit in doua (train-test split): 
#   - o parte din imagini o sa fie folosite pentru antrenare
#   - cealalta parte din imagini va fi folosita la test
print(' Pregatire set date - impartire date in set date antrenare si set date test') 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(faces.data, faces.target, random_state=0)

print('\tDimensiune X_train: ', X_train.shape)
print('\tDimensiune X_test : ', X_test.shape)

# Notam in RaportO365: 
#   - numar date extrase pentru antrenare
#   - numar date extrase pentru test
print('\n -------------------------------------------------------------------')

# In[5]: PCA (Principal Component Analysis) - pas de preprocesare
 
# Un vector de trasaturi prea mare nu este eficient in pasul de clasificare. 
# O sa folosim PCA pentru a reduce numarul de trasaturi, prin mentinerea doar 
# a informatiei relevante.
print(' Aplicare PCA (Principal Component Analysis) pe setul de antrenare')
from sklearn import decomposition
pca = decomposition.PCA(n_components=150, whiten=True)
pca.fit(X_train)

print('\tDimensiune vector Componente Principale ("eigenfaces"): ',pca.components_.shape)

# Notam in RaportO365: 
#   - numar componente principale pastrate
print('\n -------------------------------------------------------------------')
# In[6]: Fata medie ("mean" face)

# Un aspect interesant in PCA este faptul ca se calculeaza o fata medie, 
# care poate fi interesant de examinat/vizualizat.
print(' Fata medie : ')
plt.imshow(pca.mean_.reshape(faces.images[0].shape), cmap=plt.cm.bone); plt.show()
# Notam in RaportO365: 
#   - printscreen cu fata medie afisata in 'IPython console'
print('\n -------------------------------------------------------------------')
# In[7]: Vizualizat componentele principale (principal components/ "eigenfaces")
# Componentele principale masoara deviatia de la fata medie pe axele ortogonale.
# De asemenea, este interesant de vizualizat componentele principale ("eigenfaces"):
print(' Vizualizat componentele principale (principal components/ "eigenfaces")')
fig = plt.figure(figsize=(16, 6))
for i in range(30):
    ax = fig.add_subplot(3, 10, i + 1, xticks=[], yticks=[])
    ax.imshow(pca.components_[i].reshape(faces.images[0].shape),
              cmap=plt.cm.bone)
plt.show()

# Componentele ("eigenfaces") sunt ordonate dupa importanta lor din coltul stanga-sus 
# spre coltul dreapta-jos. 
# Primele componente compacteaza mai mult informatia de iluminare (lighting conditions), 
# pe cand restul componentelor compacteaza anumite trasaturi relevante din fete: nas,
# ochi, sprancene, etc.  
# 
# Notam in RaportO365: 
#   - printscreen cu componentele principale (eigenfaces) afisate in 'IPython console'
print('\n -------------------------------------------------------------------')
# In[8]: Transformare set de date - PCA
# Cu aceste proiectii calculate (considerand componentele principale obtinute), 
# putem transforma datele noastre din setul de antrenare si setul de test.
print( ' Aplicare PCA pe setul de date, considerand componentele principale obtinute')
# Aceste proiectii corespund unor factori/ponderi a imaginilor eigen
# astfel incat prin combinarea liniara a imaginilor eigen cu ponderile date de proiectii
# se obtine imaginea originala.    
X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)

print('\tDimensiune X_train_pca: ', X_train_pca.shape)
print('\tDimensiune X_test_pca : ', X_test_pca.shape)

print(" Lungime vector trasaturi original:", X_train.shape[1])
print(" Lungime vector trasaturi dupa PCA:", X_train_pca.shape[1])

# Notam in RaportO365: 
#   - comparare dimeniuni originale X_train/X_test cu cele de dupa aplicare PCA 
print('\n -------------------------------------------------------------------')
# In[9]: Aplicare SVM linear pentru recunoastere faciala

# Vom aplica o clasificare SVM (Support Vector Machines). 
print( 'Clasificare date pentru recunoastere faciala \n')
print( '\t - SVM linear \n')
from sklearn import svm
from sklearn import metrics
clf = svm.SVC(kernel = 'linear')
clf.fit(X_train_pca, y_train)
y_train_pred = clf.predict(X_train_pca)
y_test_pred = clf.predict(X_test_pca)

X_test_face = np.reshape(X_test, (X_test.shape[0],faces.images[0].shape[0],faces.images[0].shape[1]))
upr.ImageIllustrationPredictionResults(X_test_face, y_test, y_test_pred, target_names)
cm = metrics.confusion_matrix(y_test, y_test_pred)
fig = plt.figure(figsize=(16, 6))
upr.ImagePlotConfusionMatrix(cm, target_names)
# Acum se poate evalu cat de bine au fost clasificate datele.
# evRez = upr.EvalModelCls(y_test, y_test_pred,  "Test Set")

# Aceasta eficienta/rata de clasificare corecta poate fi cuantificata prin utilizarea 
# metricilor: *classification report*, *confusion matrix*.
print('    Classification report: \n\n', metrics.classification_report(y_test, y_test_pred))


# *Confusion matrix*, indica cat de des doua clase sunt confundate intre ele.
# Matricea de confuzie a unui clasificator perfect ar avea valori diferite de zero 
# doar pe diagonala principala (in rest va fi zero).

# Notam in RaportO365: 
#   - classification report
#   - confusion matrix (daca matricea este prea mare verificare valori in 'Variable explorer')
print('\n -------------------------------------------------------------------')
# In[10]: Aplicare SVM linear pentru recunoastere faciala

# Vom aplica o clasificare SVM (Support Vector Machines). 
print( 'Clasificare date pentru recunoastere faciala \n')
print( '\t - SVM nelinear \n')
from sklearn import svm
clf = svm.SVC(C=10., gamma=0.001)
clf.fit(X_train_pca, y_train)
y_pred = clf.predict(X_test_pca)

# Acum se poate evalu cat de bine au fost clasificate datele.
from sklearn import metrics

# Aceasta eficienta/rata de clasificare corecta poate fi cuantificata prin utilizarea 
# metricilor: *classification report*, *confusion matrix*.
print('    Classification report: \n\n', metrics.classification_report(y_test, y_pred))
print('    Confusion matrix:      \n\n', metrics.confusion_matrix(y_test, y_pred))
cmSVM = metrics.confusion_matrix(y_test, y_pred)

# Notam in RaportO365: 
#   - classification report
#   - confusion matrix (daca matricea este prea mare verificare valori in 'Variable explorer')
print('\n -------------------------------------------------------------------')
# In[11]: Afisare imagini (partial) si etichetele lor dupa clasificare
#Vom afisa cateva fete si etichetele lor obtinute prin clasificare. 




import numpy as np


# Clasificarea este corecta pe un numar impresionant de mare de imagini, luan in 
# considerarea simplitate modelului utilizat.
# 
# Utilizand un clasificator SVM pe un numar de 150 de trasaturi extrase, algoritmul 
# identifica corect un numar foarte mare de persoane in imagini. 

# Notam in RaportO365: 
#   - printscreen rezultat
# In[12]: Aplicare Retea Neuronala (neural network)
# antrenare NN
print( 'Clasificare date pentru recunoastere faciala \n')
print( '\t - NN (Neural Network) \n')
from sklearn.neural_network import MLPClassifier
print("Fitting the classifier to the training set")
clf = MLPClassifier(hidden_layer_sizes=(1024,), batch_size=256, verbose=False, early_stopping=True).fit(X_train_pca, y_train)
# clasificare 
y_pred = clf.predict(X_test_pca)
# evaluare
print(metrics.classification_report(y_test, y_pred))
print(metrics.confusion_matrix(y_pred, y_test))
plt.show()


# In[13]: # Pipelining
#  
# Mai sus am folosit PCA ca un pas de preprocesare/extragere de trasaturi pentru 
# a putea aplica clasificatorul. 
# 
# Trecerea iesirii a unui bloc/estimator direct la intrarea unui alt bloc/estimator 
# este un patern uzual, astfel scikit-learn ofera ``Pipeline`` care automatizeaza acest proces. 
# 
# Proiectul realizat mai sus se poate scrie, folosind *pipeline* dupa cum urmeaza: 



# SVM 
print('\n Pipeline PCA - SVM,  Confusion matrix: ')
from sklearn.pipeline import Pipeline
clf = Pipeline([('pca', decomposition.PCA(n_components=150, whiten=True)),
                ('svm', svm.SVC(C=5., gamma=0.001, kernel='rbf'))])

clf.fit(X_train, y_train)

# y_pred = clf.predict(X_test)
print(metrics.classification_report(y_pred, y_test))
plt.show()

# In[]
# NN 
print('\n Pipeline PCA - NN,  Confusion matrix: ')
from sklearn.pipeline import Pipeline
clf = Pipeline([('pca', decomposition.PCA(n_components=150, whiten=True)),
                ('NN', MLPClassifier(hidden_layer_sizes=(1024,), batch_size=256, verbose=False, early_stopping=True))])

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print(metrics.classification_report(y_pred, y_test))
plt.show()