# class Makanan: 
#     def enak():
#         print("Makanan enak")
#     sate = ""
#     nasi_uduk = ""
#     nasi_goreng = ""

# makanan = Makanan()

# makanan.sate = "sate adalah makanan dari daging yang ditusuk kemudian dibumbui dan dibakar"

# print(makanan.nasi_uduk)

# class Makanan: 
#     sate = ""
#     def makanan_enak(self):
#         print("deskripsi {}".format(self.sate))

# makanan = Makanan()
# makanan.sate = "sate adalah makanan dari daging yang ditusuk kemudian dibumbui dan dibakar"
# makanan.makanan_enak()


class Segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def mencari_luas (self):
        """Mencari luas Segitiga akan mengembalikan nilai berupa perkalian antara alas dan tinggi"""
        return self.alas * self.tinggi
    
    def __str__(self):
        return f"luas segitiga adalah {self.mencari_luas()}"
    
segitiga = Segitiga(20, 20)

print(segitiga)

help(Segitiga)



