import csv
import matplotlib.pyplot as plt
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


#creating the xaxaia
setxaxis()


print(sum_each_day)
#print("################the rates##################")
print(finalgoldrate)
#print("############this is the xaaxis##############")
#print(len(xaxis))

plt.plot(xaxis, sum_each_day, label = "line 1")

plt.xlabel('x - axis')
# Set the y axis label of the current axis.
plt.ylabel('y - axis')
# Set a title of the current axes.
plt.title('Two or more lines on same plot with suitable legends ')
# show a legend on the plot
plt.legend()
# Display a figure.
plt.show()

plt.plot(xaxis, finalgoldrate, label = "line 1")
plt.xlabel('x - axis')
# Set the y axis label of the current axis.
plt.ylabel('y - axis')
# Set a title of the current axes.
plt.title('Two or more lines on same plot with suitable legends ')
# show a legend on the plot
plt.legend()
# Display a figure.
plt.show()