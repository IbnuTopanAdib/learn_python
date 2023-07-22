from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('../belajar visualisasi matplotlib/assets/data/umur.csv')

umur = df['Age']
sns.histplot(umur, bins = 10, kde=True)
plt.show()
