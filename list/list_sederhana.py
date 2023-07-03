n = int(input("Masukan jumlah data buku yang ingin ditambahkan:"))

data_buku = []
i = 0
while i < n:
    penulis = input("Masukan nama penulis: ")
    judul_buku = input("Masukan judul buku :")
    buku = [penulis, judul_buku]
    data_buku.append(buku)
    for index, data in enumerate(data_buku):
        print(f"{index+1} | penulis: {data[0]} | judul: {data[1]}")
    i +=1