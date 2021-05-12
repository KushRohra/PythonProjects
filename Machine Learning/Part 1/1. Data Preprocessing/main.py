import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

# Reading Dataset
dataset = pd.read_csv('../datasets/Data.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Handling the Missing Data
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])

# Encoding Independent Variable
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
x = np.array(ct.fit_transform(x))

# Encoding Dependent Variable
le = LabelEncoder()
y = le.fit_transform(y)

# Splitting the Dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

# Feature Scaling
sc = StandardScaler()
x_train[:, 3:] = sc.fit_transform(x_train[:, 3:])
x_test[:, 3:] = sc.transform(x_test[:, 3:])

'''
Steps: 
1. Import libraries
2. Import dataset
3. Take care of missing data
4. Encoding Categorical Data (Encode the independent and dependent variable)
5. Splitting the dataset into Training set and Test set
6. Feature Scaling (done after splitting set because mean and deviation should not be calculated on the test set)
'''


'''
Feature Scaling:
1. Standardisation (all the time) : Xstand = (x- mean(x)) / standard deviation(x)
2. Normalisation (when you have normal distribution) : Xnorm = (x - min(x)) / (max(x) - min(x))
'''
