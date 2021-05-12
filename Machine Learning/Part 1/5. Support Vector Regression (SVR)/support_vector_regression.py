import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

dataset = pd.read_csv('../datasets/Position_Salaries.csv')
x = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

# Y is reshaped (converted from 1d to 2d array as feature scaling excepts a 2D array)
y = y.reshape(len(y), 1)

'''
Since the dependent variable has very high values compared to the features(independent variables) we need to apply feature scaling in
order to make the values in the same range such that the SVR models does not reject the features with small values
'''
# Feature Scaling
sc_x = StandardScaler()
sc_y = StandardScaler()
x = sc_x.fit_transform(x)
y = sc_y.fit_transform(y)
'''
2 standard scalar objects are required beacuse it scales tha value on the basis of standard deviation and mean of that same variable, 
and it will not be same for the level(very low value) and salary(very high value)
'''

# Training the model
regressor = SVR(kernel='rbf')
regressor.fit(x, y)

# redicting a new result
pred_value = sc_y.inverse_transform(regressor.predict(sc_x.transform([[6.5]])))
print("Predicted Salary for Level 6.5 is : ", pred_value[0])

# Visulaizing the SVR results
plt.scatter(sc_x.inverse_transform(x), sc_y.inverse_transform(y), color='red')
plt.plot(sc_x.inverse_transform(x), sc_y.inverse_transform(regressor.predict(x)), color='blue')
plt.title('Support Vector Regression')
plt.xlabel('Position Label')
plt.ylabel('Salary')
plt.show()

# Visulaizing the SVR results for higher reolution and smoother curve
x_grid = np.arange(min(sc_x.inverse_transform(x)), max(sc_x.inverse_transform(x)), 0.1)
x_grid = x_grid.reshape(len(x_grid), 1)
plt.scatter(sc_x.inverse_transform(x), sc_y.inverse_transform(y), color='red')
plt.plot(x_grid, sc_y.inverse_transform(regressor.predict(sc_x.transform(x_grid))), color='blue')
plt.title('Support Vector Regression')
plt.xlabel('Position Label')
plt.ylabel('Salary')
plt.show()
