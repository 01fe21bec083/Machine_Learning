# -*- coding: utf-8 -*-
"""Week_Assessment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s5qPJkxWsLFFMpFp48t_nxiM6889GHj1


"""## Weekley Assessment 3"""

#1  read an image and plot histogram of an image

#2 read excel file and  calculate mean and variance
import pandas as pd
import numpy as np

# Read the Excel file and specify the sheet name if needed
x1 = pd.read_excel('/content/drive/MyDrive/multivariate_example2.xlsx', usecols='C')
x2 = pd.read_excel('/content/drive/MyDrive/multivariate_example2.xlsx', usecols='D')
x3 = pd.read_excel('/content/drive/MyDrive/multivariate_example2.xlsx', usecols='E')

# Calculate means
x1_mean = np.mean(x1)
x2_mean = np.mean(x2)
x3_mean = np.mean(x3)

# Calculate variances along axis 0 (for each column)
x1_variance = np.var(x1, axis=0)
x2_variance = np.var(x2, axis=0)
x3_variance = np.var(x3, axis=0)

# Print means and variances
print("Means:")
print("x1_mean:", x1_mean)
print("x2_mean:", x2_mean)
print("x3_mean:", x3_mean)

print("\nVariances:")
print("x1_variance:", x1_variance)
print("x2_variance:", x2_variance)
print("x3_variance:", x3_variance)

#3 impliment gradient descent
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

x = np.array([0.1, 0.2, 0.3, 0.4]).reshape((-1, 1))
y = np.array([2, 3, 4, 5])
m = 4

Wo = int(input("Enter the bias value: "))
W1 = int(input("Enter the W1 value: "))
alph = float(input("Enter the learning rate value: "))
n = int(input("enter the numbe rof iterations"))

for i in range(n):
    mse1 = 0
    mse2 = 0
    cost = 0
    for j in range(m):
        pred = Wo + W1 * x[j]
        mse1 += pred - y[j]
        mse2 += (pred - y[j]) * x[j]
        cost += (pred - y[j]) ** 2

    Wo = Wo - (alph / m) * mse1
    W1 = W1 - (alph / m) * mse2

    cost /= (2 * m)  # Divide by 2m to get the mean squared error
    print(f"Iteration {i+1}: Wo = {Wo}, W1 = {W1}, Cost = {cost}")

#4 confusion matrix
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix

# Define the TP, TN, FP, FN values
TP = 30
TN = 40
FP = 30
FN = 20

# Create a confusion matrix
y_actual = np.array([TN + FP, FN + TP])
y_pred = np.array([FP + TP, TN + FN])

matrix = confusion_matrix(y_actual, y_pred)
print(matrix)

from sklearn.metrics import classification_report

# Define the TP, TN, FP, FN values
TP = 30
TN = 40
FP = 30
FN = 20

# Create a confusion matrix
y_actual = np.array([TN + FP, FN + TP])
y_pred = np.array([FP + TP, TN + FN])

# Generate the classification report
repo = classification_report(y_actual, y_pred)
print(repo)

