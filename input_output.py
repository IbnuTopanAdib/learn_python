# print gaya c/ c++
# nama = "Ibnu Topan "
# print("Hello my name is %s" % nama)
# # %s digunakan untuk tipe data string

# umur = 22
# print("umurku %d" % umur)
# # %d digunakan untuk tipe data integer

# phi = 3.14

# print("phi %.2f" % phi)

# # %f digunakan untuk tipe data float dimana %<angka dibelkang koma>f

jmlh_makanan = int(input("masukan jumlah makanan : "))

print(jmlh_makanan)
'''
    Jika input merupakan string berisi ekspresi matematika, maka konversi dengan int() atau float() akan 
    menghasilkan error. Anda dapat menggunakan fungsi eval() yang sekaligus juga berfungsi menyelesaikan 
    ekspresi matematika. Anda akan mempelajari lebih jauh mengenai fungsi pada modul Fungsi.
'''

#print(int("90 + 10")) # akan mengembalikan error

print(eval("90 + 10"))


# tugas nama saya adalah Ibnu Topan dan umur saya adalah 22 tahun ipk saya adalah 3.5

nama = "ibnu topan"
usia = 22
ipk = 3.845

print("nama saya asdalah %s, usia %d, ipk saya adalah %.2f" % (nama, usia, ipk))