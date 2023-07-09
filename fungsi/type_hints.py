import string


def luas_segitiga(alas:float, tinggi:float) -> float:
    luas = (alas * tinggi) / 2
    return luas
def luas_persegi (panjang:float, lebar:float) -> float:
    luas = panjang * lebar
    return luas

luas_tanah = luas_segitiga(2, 4) + luas_persegi(4, 10)
print(luas_tanah)

def sapa(nama:string, pesan:string):
    print(f"{pesan}, {nama}")

sapa("kucing", "makan")




