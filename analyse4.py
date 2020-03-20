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
''''
temp=[]
k=0
for i in range(10,len(total_dates)):
    if(k==0):
        temp.append(total_dates[i])
        k=1
    else:
        k=0
        continue
x_values = [datetime.datetime.strptime(d,"%Y-%m-%d").date() for d in temp]
'''

temp=[]
for i in range(10,len(total_dates)):
    temp.append(total_dates[i])
x_values = [datetime.datetime.strptime(d,"%Y-%m-%d").date() for d in temp]
growth_rate = []
'''
k=0
for pop in range(10,len(sum_each_day)):
    if(k==0):
        gnumbers = ((sum_each_day[pop] - sum_each_day[pop-1]) * 100.0 / sum_each_day[pop-1])
        growth_rate.append(gnumbers)
        k=1
    else:
        k=0
        continue
'''

for pop in range(10,len(sum_each_day)):
    gnumbers = ((sum_each_day[pop] - sum_each_day[pop-1]) * 100.0 / sum_each_day[pop-1])
    growth_rate.append(gnumbers)

gold_deltas = []
print(growth_rate)

for i in range(0,len(finalgoldrate)):
    today, yesterday = finalgoldrate[i], finalgoldrate[i-1]
    gold_deltas.append(((today - yesterday) / today) * 100)

new_xvalues=[]
for i in range(int(int(len(x_values))/2),len(x_values)):
    new_xvalues.append(x_values[i])

new_growth_rate=[]
for i in range(int(int(len(growth_rate))/2),len(growth_rate)):
    new_growth_rate.append(growth_rate[i])
new_xvalues=[]
for i in range(int(int(len(x_values))/2),len(x_values)):
    new_xvalues.append(x_values[i])
print("###############3finally the datas rare")
print(new_xvalues,new_growth_rate)
print(len(new_xvalues), len(new_growth_rate), len(gold_deltas))


ax = plt.gca()
#get axes


formatter = mdates.DateFormatter("%d")
#format as dates

ax.xaxis.set_major_formatter(formatter)

locator = mdates.DayLocator()
#set locator

ax.xaxis.set_major_locator(locator)
plt.scatter(new_xvalues, new_growth_rate)
plt.plot(new_xvalues, new_growth_rate, label = "line 1")
#plt.scatter(x_values, gold_deltas)
#plt.plot(x_values, gold_deltas,label = "line 2")
plt.xlabel('x - axis')
# Set the y axis label of the current axis.
plt.ylabel('y - axis')
# Set a title of the current axes.
plt.title('Two or more lines on same plot with suitable legends ')
# show a legend on the plot
plt.legend()
# Display a figure.
plt.show()





'''
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
#print("############this is the xaaxis##############")
#print(len(xaxis))

# plt.plot(xaxis, sum_each_day, label = "line 1")

# plt.xlabel('x - axis')
# # Set the y axis label of the current axis.
# plt.ylabel('y - axis')
# # Set a title of the current axes.
# plt.title('Two or more lines on same plot with suitable legends ')
# # show a legend on the plot
# plt.legend()
# # Display a figure.
# plt.show()

# plt.plot(xaxis, finalgoldrate, label = "line 1")
# plt.xlabel('x - axis')
# # Set the y axis label of the current axis.
# plt.ylabel('y - axis')
# # Set a title of the current axes.
# plt.title('Two or more lines on same plot with suitable legends ')
# # show a legend on the plot
# plt.legend()
# # Display a figure.
# plt.show()

xaxis.pop()

corona_deltas = []
temp=[]
k=0
for i in range(10,len(total_dates)):
    if(k==0):
        temp.append(total_dates[i])
        k=1
    else:
        k=0
        continue
x_values = [datetime.datetime.strptime(d,"%Y-%m-%d").date() for d in temp]
'''
'''for i in range(1,len(sum_each_day)):
    today, yesterday = sum_each_day[i], sum_each_day[i-1]
    corona_deltas.append(((today - yesterday) / today) * 100)
'''
'''
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

#plt.plot(xaxis, corona_deltas, label = "line 1")

ax = plt.gca()
#get axes


formatter = mdates.DateFormatter("%d")
#format as dates

ax.xaxis.set_major_formatter(formatter)

locator = mdates.DayLocator()
#set locator

ax.xaxis.set_major_locator(locator)
plt.scatter(x_values, growth_rate)
plt.plot(x_values, growth_rate, label = "line 1")
#plt.scatter(x_values, gold_deltas)
#plt.plot(x_values, gold_deltas,label = "line 2")
plt.xlabel('x - axis')
# Set the y axis label of the current axis.
plt.ylabel('y - axis')
# Set a title of the current axes.
plt.title('Two or more lines on same plot with suitable legends ')
# show a legend on the plot
plt.legend()
# Display a figure.
plt.show()

'''
'''
plt.plot(xaxis, gold_deltas, label = "line 2")
plt.xlabel('x - axis')
# Set the y axis label of the current axis.
plt.ylabel('y - axis')
# Set a title of the current axes.
plt.title('Two or more lines on same plot with suitable legends ')
# show a legend on the plot
plt.legend()
# Display a figure.
plt.show()
'''