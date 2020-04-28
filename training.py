import datetime
import csv
import matplotlib.pyplot as plt 
import matplotlib.lines as mlines
import pandas as pd  
import numpy as np

print("1.Google\n2.Amazon\n3.Microsoft\n")
comp = int(input("enter company no:"))
if comp == 1:    
    df = pd.read_csv("GOOGL.csv")
    comp_name = "Google"
elif comp == 2 :
    df = pd.read_csv("AMZN.csv")
    comp_name = "Amazon"
elif comp == 3 :
    df = pd.read_csv("MSFT.csv")
    comp_name = "Microsoft" 
else :
    print("Enter valid no")

y = df.Close.values # on y-axis there will be adj_close values
x = list(range(1, len(y) + 1)) 

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

print("The values of m and c are : ",m,c)

#plot the trained model
y_pred = []
for i in range(n):
    y_pred.append(m * x[i] + c)

# df['Date'] = pd.to_datetime(df.Date,format='%Y-%m-%d')
df['Date'] = pd.to_datetime(df.Date,format='%d-%m-%Y')
df.index = df['Date']

plt.figure("Training Graph")
close = plt.scatter(df.index ,df['Close'])
plt.plot(df.index , y_pred, color = "red")
reg_line = mlines.Line2D(df.index , y_pred, color = "red")
plt.xlabel('Dates')
plt.ylabel('close price')
plt.title(comp_name)
plt.legend([close,reg_line],['Close Prices','Regression line'])

plt.show()