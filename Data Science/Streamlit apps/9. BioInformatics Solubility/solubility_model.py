import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle

from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

dataset_url = "https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv"
dataset = pd.read_csv(dataset_url)

X = dataset.drop(['logS'], axis=1)
Y = dataset.iloc[:, -1]

model = linear_model.LinearRegression()
model.fit(X, Y)

Y_pred = model.predict(X)

print("Coeffcients : ", model.coef_)
print("Intercept : ", model.intercept_)
print("Mean Squared Error (MSE) : %.2f" % mean_squared_error(Y, Y_pred))
print("Coefficient of determination (R^2) : %.2f" % r2_score(Y, Y_pred))

print('LogS = %.2f %.2f LogP %.4f MW + %.4f RB %.2f AP' % (model.intercept_, model.coef_[0], model.coef_[1], model.coef_[2], model.coef_[3]))

plt.figure(figsize=(5, 5))
plt.scatter(x=Y, y=Y_pred, c="#7CAE00", alpha=0.3)

z = np.polyfit(Y, Y_pred, 1)
p = np.poly1d(z)

plt.plot(Y, p(Y), "#F8766D")
plt.ylabel("Predicted LogS")
plt.xlabel("Experimental LogS")
plt.show()

pickle.dump(model, open('solubility_model.pkl', 'wb'))