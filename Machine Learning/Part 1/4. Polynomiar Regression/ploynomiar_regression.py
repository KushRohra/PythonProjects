import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

dataset = pd.read_csv('Position_Salaries.csv')
x = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

# Training Linear Resgression Model on dataset first
linear_regressor = LinearRegression()
linear_regressor.fit(x, y)

# Visualizing the Linear Regression Models
plt.scatter(x, y, color='red')
plt.plot(x, linear_regressor.predict(x), color='blue')
plt.title('Linear Regression Model')
plt.xlabel('Position Levl')
plt.ylabel('Salary')
plt.show()

# Training the Polynomial Regression Model with degree 2
polynomial_regressor_2 = PolynomialFeatures(degree=2)
x_poly = polynomial_regressor_2.fit_transform(x)
linear_regressor_2 = LinearRegression()
linear_regressor_2.fit(x_poly, y)

# Visualizing the Ploynomial Regression Models
plt.scatter(x, y, color='red')
plt.plot(x, linear_regressor_2.predict(x_poly), color='blue')
plt.title('Polynomail Regression Model with degree 2')
plt.xlabel('Position Levl')
plt.ylabel('Salary')
plt.show()

# Training the Polynomial Regression Model with degree 4
polynomial_regressor_4 = PolynomialFeatures(degree=4)
x_poly = polynomial_regressor_4.fit_transform(x)
linear_regressor_4 = LinearRegression()
linear_regressor_4.fit(x_poly, y)

# Visualizing the Ploynomial Regression Models
plt.scatter(x, y, color='red')
plt.plot(x, linear_regressor_4.predict(x_poly), color='blue')
plt.title('Polynomail Regression Model with degree 4')
plt.xlabel('Position Levl')
plt.ylabel('Salary')
plt.show()


# Predicting a new result with Linear Regression
print("Linear Regression Prediction : ", linear_regressor.predict([[6.5]]))
print()

# Predicting a new result with Polynomial Regression
print("Polynomial Regression Prediction with degree 2 : ", linear_regressor_2.predict(polynomial_regressor_2.fit_transform([[6.5]])))
print("Polynomial Regression Prediction with degree 4 : ", linear_regressor_4.predict(polynomial_regressor_4.fit_transform([[6.5]])))
print()

# Coefficient and Intercept of Polynomial Regression with degree 2
print("Coefficient of degree 2 : ", linear_regressor_2.coef_)
print("Intercept of degree 2 : ", linear_regressor_2.intercept_)
print()

# Coefficient and Intercept of Polynomial Regression with degree 4
print("Coefficient of degree 4 : ", linear_regressor_4.coef_)
print("Intercept of degree 4 : ", linear_regressor_4.intercept_)
print()
