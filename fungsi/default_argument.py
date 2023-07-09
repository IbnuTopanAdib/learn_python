def sapa(nama, pesan = "hallo"):
    print(f"{pesan}, {nama}")

sapa("ibnu")


def kecepatan(h, *, vo = 0, g = 10 ):
    vt = vo + g * h
    return vt

gravitasi_bulan = kecepatan(12, g = 8)
print(gravitasi_bulan)

def laptop(*, merk = None, harga = None, madein = None):
    print( "laptop {} dengan harga {} dibuat di {}".format(merk, harga, madein))

laptop(harga = 20000, merk= "asus", madein= "Cina")

def positional_only(i, j , k ,/):
    print(f"{i}, {j}, {k}")

positional_only("windah", "basudara", "kucing")






