def penjumlahan(*args)->int:
    hasil = 0
    for data in args:
        hasil+=data
    return hasil

def perkalian(*args)->int:
    hasil = 1
    for data in args:
        hasil*=data
    return hasil

def operasi_pembagian(pembilang, penyebut, operasi = "pembagian_standard")->int:
    if operasi == "pembagian_standard":
        hasil = pembilang/ penyebut
    else:
        hasil = pembilang// penyebut

    return hasil