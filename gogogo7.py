from itertools import combinations

kata, angka=input().split(' ')
angka = int(angka)
huruf = []

hasil = list(combinations(kata, angka))

print(hasil)