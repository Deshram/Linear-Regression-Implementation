import datetime
import csv
import matplotlib.pyplot as plt 
import matplotlib.lines as mlines 
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

    
print("1.Google\n2.Amazon\n3.Microsoft\n")
comp = int(input("enter company no:"))
if comp == 1:    
    df = pd.read_csv("GOOGL_test.csv")
    m = 0.07305207559463993
    c = 1115.6280064807372
    learning_rate = 0.001
    num_iterations = 3000
    comp_name = "Google"
elif comp == 2 :
    df = pd.read_csv("AMZN_test.csv")
    m = 0.7903409986514652
    c = 1620.8507320555275
    learning_rate = 0.001
    num_iterations = 3000
    comp_name = "Amazon"
elif comp == 3 :
    df = pd.read_csv("MSFT_test.csv")
    m = 0.08662078595553525
    c = 94.85782102253692
    learning_rate = 0.001
    num_iterations = 3000
    comp_name = "Microsoft"
else :
    print("Enter valid no")

y = df.Close.values # on y-axis there will be adj_close values
x = list(range(1, len(y) + 1))

n = len(x)
print("Pre Optimization", end='\t')
print(m,c,Rss(x, y, m, c, n))
[m1, c1] = gradient_descent_runner(x, y, m, c, n, learning_rate, num_iterations)
print("Post Optimization", end='\t')
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

#Testing graphs
y_trained = []
y_optimised = []
for i in range(n):
    y_trained.append(m * x[i] + c1)
    y_optimised.append(m1 * x[i] + c1)

df['Date'] = pd.to_datetime(df.Date,format='%d-%m-%Y')
df.index = df['Date']

plt.figure("Testing Graph")
close = plt.scatter(df.index ,df['Close'])
plt.plot(df.index , y_trained, color = "red")
plt.plot(df.index , y_optimised, color = "green")
pre_opt = mlines.Line2D(df.index , y_trained, color = "red")
post_opt = mlines.Line2D(df.index , y_optimised, color = "green")
plt.xlabel('Dates')
plt.ylabel('close price')
plt.title(comp_name)
plt.legend([close , pre_opt, post_opt],['Close prices', 'pre-optimised regression line', 'post-optimised regression line'])
plt.show()

