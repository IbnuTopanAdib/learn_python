angkaku = [ 1, 3,4,6,5,6,8,3,3,4,5,2,1,7,8,9, 0, 0, 1]
mylist = ["Ibnu", "Freya", "Khufra"]
print(angkaku)

# menghitung jumlah elemen yang ada pada list dengan method count()

jumlah_angka_3 = angkaku.count(3)
jumlah_angka_2 = angkaku.count(2)
print(jumlah_angka_2)
print(jumlah_angka_3)

# menentukan index dari list dengan method index()
index_freya = mylist.index("Freya")
print(index_freya)

# mengurutkan list dengan method sort
angkaku.sort()
print(angkaku)

# mengurutkan list secara descending dengan sort() dan reverse()
angkaku.sort()
angkaku.reverse()
print(angkaku)


