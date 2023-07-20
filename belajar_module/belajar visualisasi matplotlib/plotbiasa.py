import matplotlib.pyplot as plt
import random
'''
tier style matplotlib
S : 
A : 
B : 
C :
'''
print(plt.style.available)
plt.style.use('ggplot')
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni',
         'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
ibnu = []
john = []
freya = []

def pertambahan_follower(follower_awal, follower_siapa):
    for i in range(len(bulan)):
        follower_awal += random.randint(2000, 20000)
        follower_siapa.append(follower_awal)

pertambahan_follower(200000, ibnu)
pertambahan_follower(210000, john)
pertambahan_follower(220000, freya)

plt.plot(bulan, ibnu, label = "ibnu",color= "#FF00FF", linestyle = '--')
plt.plot(bulan, freya, label = "freya", color = "#54e765", linewidth = 2)
plt.plot(bulan, john, label = "john", color = "#141235", linewidth = 2)
plt.xlabel("Bulan")
plt.xticks(rotation = 45)
plt.ylabel("Follower")
plt.title("Kenaikan Follower Perbulan")
plt.legend()
plt.tight_layout()
plt.savefig('assets/plotbiasa.png')
plt.show()