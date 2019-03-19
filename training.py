import datetime
import csv
import matplotlib.pyplot as plt 
import pandas as pd  
import numpy as np
df = pd.read_csv("training.csv")
date = pd.to_datetime(df["date"])

# x = [] # on x-axis there will be dates
# i = date.values
# for i in date:
#     x.append(100*i.month+i.day) # converting Date into integer

y = df.close.values # on y-axis there will be adj_close values
print(y)
x = list(range(1, len(y) + 1))
print(x) 

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
