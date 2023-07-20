import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

nama_top_scorer = [
    "Cristiano Ronaldo",
    "Lionel Messi",
    "Raúl",
    "Robert Lewandowski",
    "Karim Benzema",
    "Gerd Müller",
    "Ruud van Nistelrooy",
    "Thierry Henry",
    "Alfredo Di Stéfano",
    "Andriy Shevchenko"
]

# List Jumlah Gol
jumlah_gol = [135,120, 71,69, 67, 66,56,50,49,48]

df = pd.DataFrame({
    'nama' : nama_top_scorer,
    'jumlah gol' : jumlah_gol
})

df = df.sort_values(by = "jumlah gol", ascending= False)

sns.barplot(y= df['jumlah gol'], x= df['nama'], orient = 'v', color= 'red')
plt.xticks(rotation = 60)
plt.title("UCL Top Score of All Time")
plt.show()

