import matplotlib.pyplot as plt
import pandas as pd

negara_pildun = ["Germany", "Brazil", "Uruguay", "Italy", "England", "France", "Spain"]
trophy = [4, 5, 2, 4, 1, 2, 1]

df = pd.DataFrame({
    'negara_pildun' : negara_pildun,
    'trophy' : trophy
})

df = df.sort_values(by= "trophy", ascending= False)
print(df)

plt.title("Perbandingan Trophy Pildun")
plt.xlabel("Jumlah Trophy")
plt.barh(y = df['negara_pildun'], width= df['trophy'])
plt.show()