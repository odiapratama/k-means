import xlrd
import xlwt
import numpy
import matplotlib.pyplot as plt
import random

workbook = xlrd.open_workbook("data.xlsx")

worksheet1 = workbook.sheet_by_name("DataTrain")
worksheet2 = workbook.sheet_by_name("DataTest")

dataTrain= list()
data = list()

"""
NAMA     : ODIA PRATAMA
KELAS    : IF 39-13
NIM      : 1301154405
"""

x = list()
y = list()

c1x = list()
c1y = list()
c2x = list()
c2y = list()
c3x = list()
c3y = list()
c4x = list()
c4y = list()
c5x = list()
c5y = list()
c6x = list()
c6y = list()
c7x = list()
c7y = list()
c1Label = list()
c2Label = list()
c3Label = list()
c4Label = list()
c5Label = list()
c6Label = list()
c7Label = list()

newC1 = list()
newC2 = list()
newC3 = list()
newC4 = list()
newC5 = list()
newC6 = list()
newC7 = list()
listCentroid = list()
tempCentroid = list()

newList = list()


def distance(x, y):
    return (numpy.linalg.norm(x-y))
def euclid(x1,x2,y1,y2):
    euclid = ((((x1-x2)**2)+((y1-y2)**2))**0.5)
    return (euclid)
def moveCentroid(k,x,y):
    for i in range(len(x)):
        tempC1 = euclid(k[0][0], x[i], k[0][1], y[i])
        tempC2 = euclid(k[1][0], x[i], k[1][1], y[i])
        tempC3 = euclid(k[2][0], x[i], k[2][1], y[i])
        tempC4 = euclid(k[3][0], x[i], k[3][1], y[i])
        tempC5 = euclid(k[4][0], x[i], k[4][1], y[i])
        tempC6 = euclid(k[5][0], x[i], k[5][1], y[i])
        tempC7 = euclid(k[6][0], x[i], k[6][1], y[i])
        tempMin = min(tempC1, tempC2, tempC3, tempC4, tempC5, tempC6, tempC7)
        if (tempMin == tempC1):
            c1x.append(x[i])
            c1y.append(y[i])
            c1Label.append(1)
            newList.append([x[i], y[i], 1])
        elif (tempMin == tempC2):
            c2x.append(x[i])
            c2y.append(y[i])
            c2Label.append(2)
            newList.append([x[i], y[i], 2])
        elif (tempMin == tempC3):
            c3x.append(x[i])
            c3y.append(y[i])
            c3Label.append(3)
            newList.append([x[i], y[i], 3])
        elif (tempMin == tempC4):
            c4x.append(x[i])
            c4y.append(y[i])
            c4Label.append(4)
            newList.append([x[i], y[i], 4])
        elif (tempMin == tempC5):
            c5x.append(x[i])
            c5y.append(y[i])
            c5Label.append(5)
            newList.append([x[i], y[i], 5])
        elif (tempMin == tempC6):
            c6x.append(x[i])
            c6y.append(y[i])
            c6Label.append(6)
            newList.append([x[i], y[i], 6])
        elif (tempMin == tempC7):
            c7x.append(x[i])
            c7y.append(y[i])
            c7Label.append(7)
            newList.append([x[i], y[i], 7])

    newC1x = ((sum(c1x)) / len(c1x))
    newC1y = ((sum(c1y)) / len(c1y))
    newC1.append([newC1x, newC1y, 1])

    newC2x = ((sum(c2x)) / len(c2x))
    newC2y = ((sum(c2y)) / len(c2y))
    newC2.append([newC2x, newC2y, 2])

    newC3x = ((sum(c3x)) / len(c3x))
    newC3y = ((sum(c3y)) / len(c3y))
    newC3.append([newC3x, newC3y, 3])

    newC4x = ((sum(c4x)) / len(c4x))
    newC4y = ((sum(c4y)) / len(c4y))
    newC4.append([newC4x, newC4y, 4])

    newC5x = ((sum(c5x)) / len(c5x))
    newC5y = ((sum(c5y)) / len(c5y))
    newC5.append([newC5x, newC5y, 5])

    newC6x = ((sum(c6x)) / len(c6x))
    newC6y = ((sum(c6y)) / len(c6y))
    newC6.append([newC6x, newC6y, 6])

    newC7x = ((sum(c7x)) / len(c7x))
    newC7y = ((sum(c7y)) / len(c7y))
    newC7.append([newC7x, newC7y, 7])

    listCentroid.append([newC1x, newC1y, 1])
    listCentroid.append([newC2x, newC2y, 2])
    listCentroid.append([newC3x, newC3y, 3])
    listCentroid.append([newC4x, newC4y, 4])
    listCentroid.append([newC5x, newC5y, 5])
    listCentroid.append([newC6x, newC6y, 6])
    listCentroid.append([newC7x, newC7y, 7])

    tempCentroid.append([newC1x, newC1y, 1])
    tempCentroid.append([newC2x, newC2y, 2])
    tempCentroid.append([newC3x, newC3y, 3])
    tempCentroid.append([newC4x, newC4y, 4])
    tempCentroid.append([newC5x, newC5y, 5])
    tempCentroid.append([newC6x, newC6y, 6])
    tempCentroid.append([newC7x, newC7y, 7])

for i in range(1,689):
    for j in range(2):
        if j == 0 :
            x.append(float(worksheet1.cell_value(i,j)))
        elif j == 1:
            y.append(float(worksheet1.cell_value(i,j)))

k = list()
i = 0
while (i<7):
    rand = int(random.uniform(0, 688))
    k.append([x[rand],y[rand]])
    i += 1

"""Centroid Dengan Menunjuk Titik"""
# k.append([x[539],y[539]])
# k.append([x[671],y[671]])
# k.append([x[84],y[84]])
# k.append([x[403],y[403]])
# k.append([x[21],y[21]])
# k.append([x[206],y[206]])
# k.append([x[627],y[627]])
"""=============================="""

print("First Centroid   : ",k)

repeat = False
cek = 0
count = 0

while (count <= 10000 or repeat == False):
    tempCentroid = []
    c1x = []
    c1y = []
    c2x = []
    c2y = []
    c3x = []
    c3y = []
    c4x = []
    c4y = []
    c5x = []
    c5y = []
    c6x = []
    c6y = []
    c7x = []
    c7y = []
    newList = []
    moveCentroid(k, x, y)
    print("Looping   : ",count+1)
    # print(tempCentroid, " = ", k)
    for m in range(len(k)):
        if (tempCentroid == k):
            cek += 1
    # print(cek)
    k = []
    k = tempCentroid
    if (cek == 7):
        repeat = True
        break
    cek = 0
    count += 1
    # print(tempCentroid)

# for l in range(len(k)):
#     print("Nilai K ke-",l+1, " : ", k[l],"  Centroid = ", listCentroid[l])

print("Centoroid    : ",k)
print("Hasil        : ",newList)

# print(len(c1x))
# print(len(c2x))
# print(len(c3x))
# print(len(c4x))
# print(len(c5x))
# print(len(c6x))
# print(len(c7x))
#
# print(len(newList))

# for i in range(len(x)):
#     plt.scatter(x[i], y[i], marker='o', c='red')

handle = open("HasilTrain.txt", "w")
for m in range(len(newList)):
    handle.write(str(newList[m][0])+"       |       "+str(newList[m][1])+"      |       "+str(newList[m][2])+"\n")
handle.close()



"""Data Test"""

xx = list()
yy = list()
for i in range(1,101):
    for j in range(2):
        if j == 0 :
            xx.append(float(worksheet2.cell_value(i,j)))
        elif j == 1:
            yy.append(float(worksheet2.cell_value(i,j)))

listLabel = list()
for p in range(len(xx)):
    for q in range(len(k)):
        temp = euclid(xx[p], k[q][0], yy[p], k[q][1])
        if(k[q][2] == 1):
            e1 = temp
        elif(k[q][2] == 2):
            e2 = temp
        elif (k[q][2] == 3):
            e3 = temp
        elif (k[q][2] == 4):
            e4 = temp
        elif (k[q][2] == 5):
            e5 = temp
        elif (k[q][2] == 6):
            e6 = temp
        elif (k[q][2] == 7):
            e7 = temp
    temp = min(e1, e2, e3, e4, e5, e6, e7)
    if(temp == e1):
        label = 1
    elif(temp == e2):
        label = 2
    elif(temp == e3):
        label = 3
    elif(temp == e4):
        label = 4
    elif(temp == e5):
        label = 5
    elif(temp == e6):
        label = 6
    elif(temp == e7):
        label = 7
    listLabel.append(label)

handle = open("HasilTest.txt", "w")
for n in range(len(listLabel)):
    handle.write(str(xx[n])+"       |       "+str(yy[n])+"      |       "+str(listLabel[n])+"\n")
handle.close()

for i in range(len(x)):
    if(newList[i][2] == 1):
        c1 = plt.scatter(newList[i][0], newList[i][1], marker='o', c='red')
    elif(newList[i][2] == 2):
        c2 = plt.scatter(newList[i][0], newList[i][1], marker='o', c='green')
    elif (newList[i][2] == 3):
        c3 =plt.scatter(newList[i][0], newList[i][1], marker='o', c='yellow')
    elif (newList[i][2] == 4):
        c4 = plt.scatter(newList[i][0], newList[i][1], marker='o', c='cyan')
    elif (newList[i][2] == 5):
        c5 = plt.scatter(newList[i][0], newList[i][1], marker='o', c='violet')
    elif (newList[i][2] == 6):
        c6 = plt.scatter(newList[i][0], newList[i][1], marker='o', c='pink')
    elif (newList[i][2] == 7):
        c7 = plt.scatter(newList[i][0], newList[i][1], marker='o', c='orange')

tes = plt.scatter(xx, yy, c='purple')

plt.legend((c1, c2, c3, c4, c5, c6, c7, tes),
           ("Cluster 1", "Cluster 2", "Cluster 3", "Cluster 4", "Cluster 5", "Cluster 6", "Cluster 7", "Data Test"),
           loc="upper center",
           bbox_to_anchor=(0.5, -0.05),
           ncol=8,
           fontsize=5)

for j in range(len(k)):
    plt.scatter(k[j][0], k[j][1], c='blue')

plt.show()