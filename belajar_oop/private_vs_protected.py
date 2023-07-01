class Buku:
    def __init__(self, nama, pengarang):
        self.pengarang = pengarang
        self.nama = nama
        # private variabel tidak bisa diakses
        self.__private = "private"
        # protected variabel bisa diakses tapi hanya pada kelas ini saja
        self._protected = "protected"


buku1 = Buku("sapaajadeh","Mencari")
print(buku1.__dict__)

print(buku1.nama)
print(buku1._protected)
print(buku1.__private)




