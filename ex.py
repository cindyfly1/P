# Required Packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model

#2012——2018
plt.figure(figsize=(6, 4))
data = pd.read_csv('data.csv')
X_parameter = []
Y_parameter = []
for single_square_feet, single_price_value in zip(data['f'], data['b']):
    X_parameter.append([float(single_square_feet)])
    Y_parameter.append(float(single_price_value))
for i in range(68,1,-1):
    plt.plot([X_parameter[i],X_parameter[i-1]],[Y_parameter[i],Y_parameter[i-1]],'b')
Y_parameter = []
for single_square_feet, single_price_value in zip(data['f'], data['c']):
    X_parameter.append([float(single_square_feet)])
    Y_parameter.append(float(single_price_value))
for i in range(68, 1, -1):
    plt.plot([X_parameter[i], X_parameter[i - 1]], [Y_parameter[i], Y_parameter[i - 1]], 'y')
Y_parameter = []
for single_square_feet, single_price_value in zip(data['f'], data['d']):
    X_parameter.append([float(single_square_feet)])
    Y_parameter.append(float(single_price_value))
for i in range(68, 1, -1):
    plt.plot([X_parameter[i], X_parameter[i - 1]], [Y_parameter[i], Y_parameter[i - 1]], 'k')
Y_parameter = []
for single_square_feet, single_price_value in zip(data['f'], data['e']):
    X_parameter.append([float(single_square_feet)])
    Y_parameter.append(float(single_price_value))
for i in range(68, 1, -1):
    plt.plot([X_parameter[i], X_parameter[i - 1]], [Y_parameter[i], Y_parameter[i - 1]], 'r')
plt.legend()
plt.show()







