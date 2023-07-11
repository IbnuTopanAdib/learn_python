def pangkat_biasa(angka, n):
    return angka**n

hasil = pangkat_biasa(3,3)
print(hasil)


## teknik currying dengan menggunakaan lambda

def pangkat(n):
    return lambda angka: angka**n


pangkat2 = pangkat(2)

print(f"pangkat 2 dari 5 adalah {pangkat2(5)}")

pangkat3 = pangkat(3)

print(f"pangkat 3 dari 3 adalah {pangkat3(3)}")

# pangkat bebas 

print(f"pangkat bebas {pangkat(4)(3)}")


