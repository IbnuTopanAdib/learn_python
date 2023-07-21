from matplotlib import pyplot as plt


plt.style.use('ggplot')

idol = ['Freya', 'IU', 'Tzuyu', 'Yeji', 'Lalisa']
vote = [20, 25, 30, 34, 66]

colors_for_data_viz = ['#1f77b4', '#2ca02c', '#d62728', '#ff7f0e', '#7f7f7f']
explode = [0, 0, 0, 0, 0.05]

plt.pie(vote, labels= idol,
        colors= colors_for_data_viz,
        wedgeprops={'edgecolor' :'black'}, explode= explode, autopct='%.0f%%')
plt.show()
plt.savefig('assets/piechart.png')


'''
Blue (#1f77b4)
Gray (#7f7f7f)
Orange (#ff7f0e)
Red (#d62728)
Green (#2ca02c)
'''