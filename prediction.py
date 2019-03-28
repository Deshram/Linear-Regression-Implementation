import datetime
import matplotlib.pyplot as plt  
import matplotlib.lines as mlines 
import pandas as pd 

print("1.Google\n2.Amazon\n3.Microsoft\n")
comp = int(input("enter company no:"))
if comp == 1:    
    m = 1.8864902867318045
    c = 1069.5506523327006
    comp_name = "Google"
elif comp == 2 :
    m = 0.7666575320604043
    c = 1624.6219748136084
    comp_name = "Amazon"
elif comp == 3 :
    m = 0.2879155986921302
    comp_name = "Microsoft"
    c = 99.55507197230504
else :
    print("Enter valid no")

a = datetime.date.today()
dates = []
for i in range(0,30):
    b = a + datetime.timedelta(days = i)
    dates.append(b.strftime('%Y-%m-%d'))

x = list(range(1,31))

y_pred = []
for i in range(len(x)):
    y_pred.append( m * x[i] + c )
print(y_pred)
print("Next day prediction will be near to ")
print(y_pred[1])
dates = pd.to_datetime(dates,format='%Y-%m-%d')
dates.index = dates

plt.xlabel('Dates')
plt.ylabel('close price')
plt.title(comp_name)
plt.plot(dates ,y_pred)
pred = mlines.Line2D(dates ,y_pred)
plt.legend([pred],['prediction line'])
plt.show()
