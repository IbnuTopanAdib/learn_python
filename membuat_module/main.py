from perhitungan import operasi_pembagian, penjumlahan, perkalian
from biodata.biodata_anggota import anggota1
import time
t1= time.time()
hasil_penjumlahan = penjumlahan(1,2,3,4,5,6,7,8,9,10,11)
hasil_perkalian = perkalian(1,2,3,4,5)
hasil_pembagian = operasi_pembagian(10, 3, operasi = "bukan")
print(hasil_perkalian)
print(hasil_penjumlahan)
print(hasil_pembagian)

for key, value in anggota1.items():
    print(f"{key} : {value}")

t2 = time.time()

print(f"waktu eksekusi {t2-t1}")