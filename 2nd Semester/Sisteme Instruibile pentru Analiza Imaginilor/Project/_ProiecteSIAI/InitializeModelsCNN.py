# -*- coding: utf-8 -*-
"""
Created on Sat May  9 23:07:53 2020

@author: Florea.Camelia
"""
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPool2D, Flatten
from sklearn.metrics import classification_report
from keras.applications.resnet50 import ResNet50
from keras.models import Model

# from keras.models import Sequential
from keras.layers.normalization import BatchNormalization
# from keras.layers.convolutional import Conv2D
# from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
# from keras.layers.core import Flatten
from keras.layers.core import Dropout
# from keras.layers.core import Dense

def modelSimple(Hm, Wm, ch, clsNr):
    # Conv2D->MaxPool2D->Flatten->Dense->Dense
    model = Sequential()

    # CONVOLUTIONAL LAYER
    model.add(Conv2D(filters=32, kernel_size=(4,4),input_shape=(Hm, Wm, ch), activation='relu',))
    
    # POOLING LAYER
    model.add(MaxPool2D(pool_size=(2, 2)))
    
    # FLATTEN IMAGES FROM 28 by 28 to 764 BEFORE FINAL LAYER
    model.add(Flatten())
    
    # 128 NEURONS IN DENSE HIDDEN LAYER (YOU CAN CHANGE THIS NUMBER OF NEURONS)
    model.add(Dense(128, activation='relu'))
    
    # LAST LAYER IS THE CLASSIFIER, THUS 10 POSSIBLE CLASSES
    model.add(Dense(clsNr, activation='softmax'))
    
    return model

def Model2Layers(Hm, Wm, ch, clsNr):
    #   Second model
    
    model_2layers = Sequential()
    
    ## FIRST SET OF LAYERS
    
    # CONVOLUTIONAL LAYER
    model_2layers.add(Conv2D(filters=32, kernel_size=(4,4),input_shape=(Hm, Wm, ch), activation='relu',))
    # POOLING LAYER
    model_2layers.add(MaxPool2D(pool_size=(2, 2)))
    
    ## SECOND SET OF LAYERS
    
    # CONVOLUTIONAL LAYER
    model_2layers.add(Conv2D(filters=32, kernel_size=(4,4), activation='relu',))
    # POOLING LAYER
    model_2layers.add(MaxPool2D(pool_size=(2, 2)))
    
    # FLATTEN IMAGES FROM 28 by 28 to 764 BEFORE FINAL LAYER
    model_2layers.add(Flatten())
    
    # 256 NEURONS IN DENSE HIDDEN LAYER (YOU CAN CHANGE THIS NUMBER OF NEURONS)
    model_2layers.add(Dense(256, activation='relu'))
    
    # LAST LAYER IS THE CLASSIFIER, THUS 10 POSSIBLE CLASSES
    model_2layers.add(Dense(clsNr, activation='softmax'))
    
    return model_2layers

def ModelLargeCNN(Hm, Wm, ch, clsNr):
    # ## Optional: Large Model
    
    model_large = Sequential()
    
    ## FIRST SET OF LAYERS
    
    # CONVOLUTIONAL LAYER
    model_large.add(Conv2D(filters=32, kernel_size=(4,4),input_shape=(Hm, Wm, ch), activation='relu',))
    # CONVOLUTIONAL LAYER
    model_large.add(Conv2D(filters=32, kernel_size=(4,4), activation='relu',))
    
    # POOLING LAYER
    model_large.add(MaxPool2D(pool_size=(2, 2)))
    
    ## SECOND SET OF LAYERS
    
    # CONVOLUTIONAL LAYER
    model_large.add(Conv2D(filters=64, kernel_size=(4,4), activation='relu',))
    # CONVOLUTIONAL LAYER
    model_large.add(Conv2D(filters=64, kernel_size=(4,4), activation='relu',))
    
    # POOLING LAYER
    model_large.add(MaxPool2D(pool_size=(2, 2)))
    
    # FLATTEN IMAGES FROM 28 by 28 to 764 BEFORE FINAL LAYER
    model_large.add(Flatten())
    
    # 512 NEURONS IN DENSE HIDDEN LAYER (YOU CAN CHANGE THIS NUMBER OF NEURONS)
    model_large.add(Dense(512, activation='relu'))
    
    # LAST LAYER IS THE CLASSIFIER, THUS 10 POSSIBLE CLASSES
    model_large.add(Dense(clsNr, activation='softmax'))
    
    return model_large
    
    
def ResNet50Model(Hm, Wm, ch, clsNr):
       
    IMAGE_SIZE = [Wm, Hm] # feel free to change depending on dataset
    # add preprocessing layer to the front of VGG
    res = ResNet50(input_shape=IMAGE_SIZE + [ch], include_top=False) #weights='imagenet', 
    
    # don't train existing weights
    for layer in res.layers:
      layer.trainable = False
    
    # our layers - you can add more if you want
    x = Flatten()(res.output)
    x = Dense(256, activation='relu')(x)
    prediction = Dense(clsNr, activation='softmax')(x)
    
    # create a model object
    model = Model(inputs=res.input, outputs=prediction)
    
    return model

def MiniVGGNet(Hm, Wm, ch, clsNr):
    
    # initialize the model along with the input shape to be
    # "channels last" and the channels dimension itself
    model = Sequential()
    inputShape = (Hm, Wm, ch)
    chanDim = -1
    # if we are using "channels first", update the input shape
    # and channels dimension
    # if K.image_data_format() == "channels_first":
    #     inputShape = (depth, height, width)
    #     chanDim = 1    
        
        
    # first CONV => RELU => CONV => RELU => POOL layer set
    model.add(Conv2D(32, (3, 3), padding="same", input_shape=inputShape))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis=chanDim))
    model.add(Conv2D(32, (3, 3), padding="same"))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis=chanDim))
    model.add(MaxPool2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    # second CONV => RELU => CONV => RELU => POOL layer set
    model.add(Conv2D(64, (3, 3), padding="same"))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis=chanDim))
    model.add(Conv2D(64, (3, 3), padding="same"))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis=chanDim))
    model.add(MaxPool2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
  	# first (and only) set of FC => RELU layers
    model.add(Flatten())
    model.add(Dense(512))
    model.add(Activation("relu"))
    model.add(BatchNormalization())
    model.add(Dropout(0.5))
  	# softmax classifier
    model.add(Dense(clsNr))
    model.add(Activation("softmax"))
  	# return the constructed network architecture
    return model
