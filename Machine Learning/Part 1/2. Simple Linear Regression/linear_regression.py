import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Importing Dataset
dataset = pd.read_csv('Salary_Data.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Splitting the dataset into training set and test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

# Training the Simple Linear Regression model on Training Set
regressor = LinearRegression()
regressor.fit(x_train, y_train)

# Predicting the results
y_pred = regressor.predict(x_test)

# Visulaizing the Training Set Results
plt.scatter(x_train, y_train, color='red')
plt.plot(x_train, regressor.predict(x_train), color='blue')
plt.title('Salary vs Experience (Training Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualizing the Test Set Results
plt.scatter(x_test, y_test, color='red')
plt.plot(x_train, regressor.predict(x_train), color='blue')
plt.title('Salary vs Experience (Test Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# To get salary of an employee with 12 yrs of experience
print(regressor.predict([[12]]))  # Expects a 2D array

# To get coefficient(b1) and intercept(b0) in y = b0 + b1*x
print(regressor.coef_)
print(regressor.intercept_)
