# kata = "Ibnu Topan Adib Amruloh"
#
# for k in kata:
#     print(f"huruf: {k}")
#
# buah = [ "apel", "jeruk", "anggur"]
#
# for bh in buah:
#     print(bh)
#
# for index in range(len(buah)):
#     print(f"Buah : {buah[index]}")
#
# # perulangan while
#
# a = 1
#
# while a < 8:
#     print(a)
#     a+=1
#
# #for loop bersarang
# for i in range(0, 6):
#     for j in range(0, 6-i):
#         print('%', end ='')
#     print()
#
# for i in range(1, 4):
#     for j in range(1, 3):
#         print(i, j)
#
#
# list2 = ["maju", 'mundur', "kanan", "kiri", "maju", "stop"]
#
# for index in range(len(list2)):
#     if list2[index] == "stop":
#         break
#     print(f"stop pada langkah ke {index}")

for i in range(0,20,2):
    if i/2 == 5:
        continue
    print(i)

'''
Pada Python juga dikenal fungsi else setelah for. Fungsinya diutamakan pada 
perulangan yang bersifat pencarian - untuk memberikan jalan keluar program saat pencarian tidak
ditemukan.

Struktur umumnya adalah sebagai berikut:

for item in items:
    if cari(item):
        #ditemukan!
        proses_item()
        break
else:
    #Item tidak ditemukan
    not_found_in_container()

if any(something_about(thing) for each thing in container):
    do_something(that_thing)
else:
    no_such_thing()
'''

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n/x)
            break


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print( n, 'equals', x, '*', n/x)
            break
    else:
        # loop fell through without finding a factor
        print(n, ' adalah bilangan prima')