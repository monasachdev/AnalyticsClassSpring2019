import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report


# loading the data
CryoData = pd.read_csv('Cryotherapy.csv')

# Creating the data set
X = np.array(CryoData.loc[:,['Age','Time']])
y = np.array(CryoData.Success)
targetNames = ['Failure', 'Success']

# Standardizing the data
stdData = StandardScaler().fit(X)  # standardization object
X_norm = stdData.transform(X)  # the actual transformation

# plotting the data
plt.figure(figsize=[6,6])
plt.scatter(X[:,0],X[:,1],c=y,cmap=plt.cm.coolwarm)
plt.xlabel('Age')
plt.ylabel('Time')
plt.show()


# Exercise code here!
