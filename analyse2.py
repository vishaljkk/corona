import csv
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates
data=[]
golddata=[]
total_dates=[]
sum_each_day=[]
finalgoldrate=[]
xaxis=[]

#get_corona_data
def getcoronadata():
    with open('time-series-19-covid-combined.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)

#get_gold_data
def getgolddata():
    with open('finalgol.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            golddata.append(row)

def setdates():
    for i in range(0,len(data)):
        if(data[i][1]=="Thailand"):
            total_dates.append(data[i][4])

#find_patient_eachday_list
def findpatienteachdaylist():
    for j in range(0,len(total_dates)):
        sum=0
        for i in range(0,len(data)):
            if(data[i][4]==total_dates[j]):
                sum=sum+int(data[i][5])
        sum_each_day.append(sum)
def extractgoldonly():
    for i in range(0,len(golddata)):
        finalgoldrate.append(golddata[i][3][4:9])

def setxaxis():
    for i in range(0,len(sum_each_day)):
        xaxis.append(i)

#calling all the functions
getcoronadata()
setdates()
findpatienteachdaylist()
getgolddata()
extractgoldonly()

#transformation of the data
finalgoldrate.pop()
#total_dates.pop()

#creating the xaxaia
setxaxis()


print('sum', sum_each_day)
#print("################the rates##################")
for i in range(len(finalgoldrate)):
    x = ""
    for y in finalgoldrate[i]:
        if y == ',':
            continue
        else:
            x += y
    finalgoldrate[i] = int(x) 


xaxis.pop()

corona_deltas = []

x_values = [datetime.datetime.strptime(d,"%Y-%m-%d").date() for d in total_dates]


growth_rate = []
k=0
for pop in range(10,len(sum_each_day)):
    if(k==0):
        gnumbers = ((sum_each_day[pop] - sum_each_day[pop-1]) * 100.0 / sum_each_day[pop-1])
        growth_rate.append(gnumbers)
        k=1
    else:
        k=0
        continue
gold_deltas = []
print(growth_rate)

for i in range(0,len(finalgoldrate)):
    today, yesterday = finalgoldrate[i], finalgoldrate[i-1]
    gold_deltas.append(((today - yesterday) / today) * 100)

print(len(xaxis), len(growth_rate), len(gold_deltas))


ax = plt.gca()
#get axes


formatter = mdates.DateFormatter("%d")
#format as dates

ax.xaxis.set_major_formatter(formatter)

locator = mdates.DayLocator()
#set locator

ax.xaxis.set_major_locator(locator)
#plt.scatter(x_values, growth_rate)
#plt.plot(x_values, growth_rate, label = "line 1")
plt.scatter(x_values, gold_deltas)
plt.plot(x_values, gold_deltas,label = "line 2")
plt.xlabel('x - axis')
# Set the y axis label of the current axis.
plt.ylabel('y - axis')
# Set a title of the current axes.
plt.title('Two or more lines on same plot with suitable legends ')
# show a legend on the plot
plt.legend()
# Display a figure.
plt.show()


