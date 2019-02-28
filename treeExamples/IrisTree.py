import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

# Loading data
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

# spliting the data into training and testing data sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4,
                                                    random_state=2018)


# decision tree classifier
dt = DecisionTreeClassifier(criterion='entropy', 
                            min_samples_leaf = 3,
                            max_depth = 4,
                            random_state=0)
dt.fit(X_train,y_train)


# classification on the testing data set
y_pred = dt.predict(X_test)
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test, y_pred,
                            target_names=target_names))


# decision tree classifier, unconstrained
dtUnc = DecisionTreeClassifier(criterion='entropy',
                               random_state=0)
dtUnc.fit(X_train,y_train)
y_pred_unc = dtUnc.predict(X_test)
print(confusion_matrix(y_test,y_pred_unc))
print(classification_report(y_test, y_pred_unc,
                            target_names=target_names))

