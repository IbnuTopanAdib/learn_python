from matplotlib import pyplot as plt
plt.style.use('ggplot')
hewan_peliharaan = ['anjing', 'kucing', 'ikan', 'burung','lainnya']

jumlah = [12, 25, 15, 32, 7]

colors = ['#2ca02c','#7f7f7f' , '#d62728', '#ff7f0e','#1f77b4' ]

plt.pie(jumlah, labels= hewan_peliharaan, wedgeprops= {'edgecolor' : 'black'})
plt.show()
'''
Blue (#1f77b4)
Gray (#7f7f7f)
Orange (#ff7f0e)
Red (#d62728)
Green (#2ca02c)
'''