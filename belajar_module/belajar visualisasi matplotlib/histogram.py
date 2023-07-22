from matplotlib import pyplot as plt
import csv

'''
okeh disini kita akan membuat histogram ygy
'''

data_umur = []
with open('assets/data/umur.csv') as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        data_umur.append(float(row['Age']))
print(data_umur)
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.hist(data_umur, bins= bins, edgecolor = 'black', log = True )
median = 29
color = 'red'
plt.axvline(median, color = color, label = "Median data")
plt.title("persebaran umur customer")
plt.ylabel("frekuensi")
plt.xlabel("umur")
plt.legend()
plt.show()

