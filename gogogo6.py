from itertools import permutations

kata, angka=input().split(' ')
angka = int(angka)
huruf = []

for h in kata:
    huruf.append(h)

hasil = list(permutations(huruf, angka))

final_hasil = []
for p in hasil:
    her = "".join(p)
    final_hasil.append(her)

final_hasil.sort()
for f in final_hasil:
    print(f)


