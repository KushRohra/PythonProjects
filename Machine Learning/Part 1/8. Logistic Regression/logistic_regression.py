import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

dataset = pd.read_csv('Social_Network_Ads.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=0)

# Feature Scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)

# Predicting a new result
predicted_value = classifier.predict(sc.transform([[30, 87000]]))
print("Predicting a new result : ", predicted_value[0])
print()

# Predicting the test set results
y_pred = classifier.predict(X_test)
print("Predicting the test set results : ")
print(np.concatenate((y_test.reshape(len(y_test), 1), y_pred.reshape(len(y_pred), 1)), 1))
print()

# Making the confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix is : ", cm)
print()

# Accuracy Score
score = accuracy_score(y_test, y_pred)
print("Accuracy score of the model is : ", score)
print()
