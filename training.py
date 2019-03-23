import datetime
import csv
import matplotlib.pyplot as plt 
import pandas as pd  
import numpy as np

print("1.Google\n2.Amazon\n3.Microsoft\n")
comp = int(input("enter company no:"))
if comp == 1:    
    df = pd.read_csv("GOOGL.csv")
elif comp == 2 :
    df = pd.read_csv("AMZN.csv")
elif comp == 3 :
    df = pd.read_csv("MSFT.csv")
else :
    print("Enter valid no") 
# x = [] # on x-axis there will be dates
# i = date.values
# for i in date:
#     x.append(100*i.month+i.day) # converting Date into integer

y = df.Close.values # on y-axis there will be adj_close values
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
y_pred = []
for i in range(n):
    y_pred.append(m * x[i] + c)

# df['Date'] = pd.to_datetime(df.Date,format='%Y-%m-%d')
df['Date'] = pd.to_datetime(df.Date,format='%d-%m-%Y')
df.index = df['Date']

plt.figure("Training Graph")
plt.scatter(df.index ,df['Close'])
plt.plot(df.index , y_pred)

plt.show()