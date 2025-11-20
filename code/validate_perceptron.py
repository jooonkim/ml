import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

s = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
df = pd.read_csv(s, header=None, encoding='utf-8') # dataframe

# print(df.tail()) # just to ensure that the data was loaded correctly

y = df.iloc[0:100, 4].values # creates a np array (.values) from the species labels (4 == 5th column == species) of the first 100 rows
y = np.where(y == 'Iris-setosa', 0, 1) # 0 if setosa, 1 if versicolor (first 100 rows only have those two species)

X = df.iloc[0:100, [0, 2]].values # 100 x 2 matrix that extracts two features: sepal length (0) and petal length (2)

# Plot the two iris classes in the 100 x 2 matrix to visualize how separable they are before fitting a perceptron
# It's important that it's roughly linearly separable, which is when a perceptron would be a good choice

plt.scatter(X[:50, 0], X[:50, 1], color='red', marker='o', label = 'Setosa')
plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='s', label = 'Versicolor')

# Note that the x-axis here would be sepal length (because it's in column 0) and y-axis would be petal length (column 1)
plt.xlabel('Sepal length (cm)')
plt.ylabel('Petal length (cm)')
plt.legend(loc='upper left')
plt.show()

