''' 
method len() yang akan menghitung panjang atau banyakn
ya elemen dari List (untuk String menjadi menghitung jumlah karakternya)
'''

contoh_list = [1,1,2,3,4,4,5,6,5,6,7,7]

print(len(contoh_list))

contoh_set = set(contoh_list)
print(len(contoh_set))

'''
untuk mengetahui nilai maksimum dan minimum list
'''

angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]
print(min(angka))
print(max(angka))

'''
Untuk mengetahui berapa kali suatu objek muncul dalam list, Anda dapat menggunakan fungsi count().
'''
genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]
print(genap.count(6))
string = "Belajar Python di Dicoding sangat menyenangkan"
substring = "a"
print(string.count(substring))


'''
kita juga bisa penggabungan list di python yang caranya ssama dengan penggabungan string
'''

list1 = ['makanan', 'minuman',]

list2 = ['komputer', 'python']

list_gabungan = list1 + list2

kalimat = " ".join(list_gabungan)

print(kalimat)


'''
kita juga bisa meriplakasi list

'''

#contoh
list_1 = ["ibnu"]*7
print(list_1)


# fungsi range
kocak = [_ for _ in range(2,12,2)]
print(kocak)

# fungsi in not in

kata = "indonesia is the best country in the world"
if ("indonesia" in kata):
    print("ada Indonesia cuy")

kalimat = "Belajar Python di Dicoding sangat menyenangkan"
print('Dicoding' in kalimat)
print('tidak' in kalimat)
print('Dicoding' not in kalimat)
print('tidak' not in kalimat)

list3 = [1, 2, 40, 20, 3, 3]
def bilangan_genap(angka):
    for i in angka:
        if(i%2 == 0):
            return i

if (bilangan_genap(list3) in list3 ):
    print("benar")

# memberikan nilai untuk multiple variabel
def history_meals(arr):
    return arr


history = history_meals(["nasi", "gorengan", "nanas"])

sarapan, makan_siang, makan_malam = history

print(sarapan)
print(makan_siang)
print(makan_malam)

'''
Penggunaan assignment pada multi variabel ini dapat Anda gunakan untuk menukar nilai dua atau lebih variabel:
'''

apparel, color = 'shirt', 'white'
apparel, color = color, apparel
print(apparel)
print(color)


# method sort 

angka = [2,34,6,5,56,76,54]

print(angka.sort())

kendaraan = ['motor', 'mobil', 'helikopter', 'Pesawat']
kendaraan.sort()
print(kendaraan)


kendaraan = ['Motor', 'Mobil', 'helikopter', 'pesawat']
kendaraan.sort(key=str.lower)
print(kendaraan)