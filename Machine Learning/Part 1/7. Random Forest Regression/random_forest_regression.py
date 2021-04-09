import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

dataset = pd.read_csv('Position_Salaries.csv')
x = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

# Training the Decision Tree model on the whole dataset
num_of_trees = 10
regressor = RandomForestRegressor(n_estimators=num_of_trees, random_state=0)
regressor.fit(x, y)

# Predicting a new result
pred_value = regressor.predict([[6.5]])[0]
print("Predicted value for Level 6.5 is : ", pred_value)

# Visualizing the Decision Tree Regression Results (higher resolution)
x_grid = np.arange(min(x), max(x), 0.1)
x_grid = x_grid.reshape(len(x_grid), 1)
plt.scatter(x, y, color='red')
plt.plot(x_grid, regressor.predict(x_grid))
plt.title('Decision Tree Regression Model')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
