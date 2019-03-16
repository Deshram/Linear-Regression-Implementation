import datetime
import csv
import matplotlib.pyplot as plt 
import pandas as pd  
import numpy as np

#calculating sum of square errors (btw it should be repeated till r2 appr= 1 and should be tried on different dataset)
def Rss(x, y, m, c, n):
    rss = 0 
    for i in range(n):
        y_pred = m * x[i] + c
        rss += (y[i] - y_pred) ** 2
    return rss / n

def gradient_descent_runner(x, y, m, c, n, learning_rate, num_iterations):
    for i in range(num_iterations):
        m, c = step_gradient(m, c, x, y, n, learning_rate)
    return [m, c]

def step_gradient(m, c, x, y, n, learning_rate):
    c_gradient = 0
    m_gradient = 0
    for i in range(n):
        y_err = y[i] - ((m * x[i]) + c)
        c_gradient += -(2/n) * y_err
        m_gradient += -(2/n) * x[i] * y_err 
    new_c = c - (learning_rate * c_gradient)
    new_m = m - (learning_rate * m_gradient)
    return [new_m, new_c]
    
df = pd.read_csv("testing.csv")
date = pd.to_datetime(df["date"])
x = [] # on x-axis there will be dates
i = date.values
for i in date:
    x.append(100*i.month + i.day) # converting Date into integer
print(x)
y = df.close.values # on y-axis there will be adj_close values
print(y) 

m = 0.5189880105434824
c = 1019.834484638208
n = len(x)
learning_rate = 0.0001
num_iterations = 1000
print(m,c,Rss(x, y, m, c, n))
[m1, c1] = gradient_descent_runner(x, y, m, c, n, learning_rate, num_iterations)
print(m1,c1,Rss(x, y, m1, c1, n))

mean_x = np.mean(x)
mean_y = np.mean(y)
ss_r = 0
ss_t = 0
for i in range(n):
    y_pred = m1 * x[i] + c1
    ss_t += (y[i] - mean_y) ** 2
    ss_r += (y[i] - y_pred) ** 2
r2 = 1 - (ss_r/ss_t)
print(r2)