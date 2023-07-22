import pandas as pd
from matplotlib import pyplot as plt


df = pd.read_csv('assets/data/youtube.csv')
print(df.head())
view = df["view_count"]
likes = df["likes"]
ratio = df["ratio"]

plt.scatter(view, likes,c = ratio, cmap= 'Blues', edgecolors= 'black', linewidths= 1, alpha= 0.75 )
cbar = plt.colorbar()
cbar.set_label('ratio like dislike')
plt.xscale('log')
plt.yscale('log')
plt.xlabel("View Count")
plt.ylabel("Likes")
plt.savefig('assets/scatter1.png')
plt.show()