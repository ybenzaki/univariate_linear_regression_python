# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


def predict(x):
    return slope * x + intercept

df = pd.read_csv("D:\DEV\PYTHON_PROGRAMMING\coursera_ml_exercices_in_python\univariate_linear_regression_dataset.csv")
#print len(df)
X =  df.iloc[0:len(df),0] #selection de la première colonne de notre dataset
Y =  df.iloc[0:len(df),1]

axes = plt.axes()
#axes.set_xlim([2, 25])
#axes.set_ylim([0, 30])
axes.grid()
plt.scatter(X,Y)
plt.show()
#plt.savefig("D:/figure.png")

slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)

#print r_value * r_value
fitLine = predict(X)
plt.plot(X, fitLine, c='r')


print predict(20.27)