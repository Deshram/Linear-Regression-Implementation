import datetime
import csv
import matplotlib.pyplot as plt 
import pandas as pd  
import numpy as np
df = pd.read_csv("google.csv")
date = pd.to_datetime(df["Date"])
x = [] # on x-axis there will be dates
i = date.values
for i in date:
    x.append(100*i.month + i.day) # converting Date into integer
print(x)
y = df.Adj_Close.values # on y-axis there will be adj_close values
print(y) 

#mean of x and y
mean_x = np.mean(x)
mean_y = np.mean(y)

n = len(x)

#Calculating m and c (y = mx + c)
numer = 0
denom = 0
for i in range(n):
    numer += (x[i] - mean_x) * (y[i] - mean_y)
    denom += (x[i] - mean_x) ** 2
m = numer / denom
c = mean_y - ( m * mean_x)

print(m,c)

#plot the trained model

"""testing"""
#calculating root-mean square (btw it should be repeated till r2 appr= 1 and should be tried on different dataset)
ss_t = 0
ss_r = 0
for i in range(n):
    y_pred = m * x[i] + c
    ss_t += (y[i] - mean_x) ** 2
    ss_r += (y[i] - y_pred) ** 2
r2 = 1 - ss_r/ss_t
print(r2) 