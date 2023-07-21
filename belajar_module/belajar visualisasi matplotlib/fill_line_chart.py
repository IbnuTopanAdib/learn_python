import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('assets/data/programming_language.csv')

age = df['Age']
all_devs = df['All_Devs']
py_devs = df['Python']
js_devs = df['JavaScript']
overall_median = 57287

plt.style.use('ggplot')
plt.plot(age, all_devs, label= 'all dev', linestyle ='--', color ='#7f7f7f')
plt.plot(age, py_devs, label= 'python dev')

plt.fill_between(age, py_devs,all_devs, where=(py_devs> all_devs),
                 interpolate=True, alpha = 0.25, color = '#1f77b4', label = 'Diatas All dev')
plt.fill_between(age, py_devs,all_devs, where=(py_devs<=all_devs),
                 interpolate=True, alpha = 0.25, color = '#d62728', label = 'Dibawah All dev')
plt.title("Comparison Developer Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.tight_layout()
plt.legend()
plt.savefig("assets/fill_line_chart.png")
plt.show()

