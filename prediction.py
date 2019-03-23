import datetime
import matplotlib.pyplot as plt  

print("1.Google\n2.Amazon\n3.Microsoft\n")
comp = int(input("enter company no:"))
if comp == 1:    
    m = 1.8864902867318045
    c = 1069.5506523327006
elif comp == 2 :
    m = 0.7666575320604043
    c = 1624.6219748136084
elif comp == 3 :
    m = 0.2879155986921302
    c = 99.55507197230504
else :
    print("Enter valid no")

a = datetime.date.today()
dates = []
for i in range(0,30):
    b = a + datetime.timedelta(days = i)
    dates.append(b.strftime('%Y-%m-%d'))
print(dates)

x = list(range(1,31))
print(x)

y_pred = []
for i in range(len(x)):
    y_pred.append( m * x[i] + c )
print(y_pred)
print("Next day prediction will be near to ")
print(y_pred[1])

plt.plot(dates ,y_pred)
plt.show()
