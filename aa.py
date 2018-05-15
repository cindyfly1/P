# Required Packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model

# Function to get data
def get_data(file_name):
    data = pd.read_csv(file_name)
    X_parameter = []
    Y_parameter = []
    for single_square_feet, single_price_value in zip(data['day'], data['price']):
        X_parameter.append([float(single_square_feet)])
        Y_parameter.append(float(single_price_value))
    return X_parameter, Y_parameter


# Function for Fitting our data to Linear model
def linear_model_main(X_parameters, Y_parameters, predict_value):
    # Create linear regression object
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)
    predict_outcome = regr.predict(predict_value)
    predictions = {}
    predictions['intercept'] = regr.intercept_
    predictions['coefficient'] = regr.coef_
    predictions['predicted_value'] = predict_outcome
    return predictions

# Function to show the resutls of linear fit model
def show_linear_line(X_parameters, Y_parameters):
    # Create linear regression object
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)
    plt.scatter(X_parameters, Y_parameters, color='blue')
    plt.plot(X_parameters, regr.predict(X_parameters), color='red', linewidth=4)
    plt.xticks(())
    plt.yticks(())
    plt.legend()
    plt.show()

# def get_plot(file_name):
#     data = pd.read_csv(file_name)
#     X_parameter = []
#     Y_parameter = []
#     for single_square_feet, single_price_value in zip(data['f'], data['b']):
#         X_parameter.append([float(single_square_feet)])
#         Y_parameter.append(float(single_price_value))
#     for i in range(68,1,-1):
#         plt.plot([X_parameter[i],X_parameter[i-1]],[Y_parameter[i],Y_parameter[i-1]],'k')
#     plt.legend()
#     plt.show()
#     return X_parameter, Y_parameter


X, Y = get_data('data1.csv')
predictvalue = 30000
result = linear_model_main(X, Y, predictvalue)
print("Intercept value ", result['intercept'])
print("coefficient", result['coefficient'])
# print("Predicted value: ", result['predicted_value'])
show_linear_line(X,Y)
# get_plot('data.csv')



