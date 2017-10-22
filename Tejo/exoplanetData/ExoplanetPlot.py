# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 14:32:13 2017

@author: tnuta
"""

# Evaluate using a train and a test set
from pandas import read_csv
import matplotlib.pyplot as plt
import numpy as np
filename = 'exoTrain.csv'
dataframefull = read_csv(filename)
array= dataframefull.values
#dataframeZero= read_csv(filename, nrows=1) #gets just the data for star at index 0 
#array = dataframeZero.values
X=array[4,1:]  #change first number to change star 
Z=array[1000,1:] #change first number to change star 
Y=np.arange(0,X.size,1)
Y=[]
for i in range(1,X.size+1):
    Y.append(i)
y=np.asarray(Y)
X=np.reshape(X,(1,3197))
Y=np.reshape(y,(1,3197))
Z=np.reshape(Z,(1,3197))
plt.plot(Y,X, 'ro')
plt.plot(Y,Z, 'bo')
plt.xlabel("time (arbitrary units)")
plt.ylabel("flux reading")
plt.title("Flux readings over time for Star X and Star Z")
plt.show()
