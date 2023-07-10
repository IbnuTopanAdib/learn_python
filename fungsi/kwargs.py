def biodata(**kwargs):
    nama = kwargs.get("nama")
    hewan = kwargs.get("hewan")
    pasangan = kwargs.get("pasangan")
    print(f"nama : {nama}, hewan : {hewan}, pasangan : {pasangan}")

biodata(nama = "ibnu topan", hewan = "anjing", pasangan = "Freya")


def loopingthrough(**kwargs):
    for k in kwargs.keys():
        print(k)
loopingthrough(nama = "ibnu topan", hewan = "anjing", pasangan = "Freya")


def operasiMtk(*args, **kwargs):
    hasil = 0
    if kwargs.get("operasi") == "tambah":
        for arg in args:
            hasil += arg
    if kwargs.get("operasi") == "kali":
        hasil = 1
        for arg in args:
            hasil*= arg
    return hasil
apaantuh = operasiMtk(1,2, operasi = "tambah")
print(apaantuh)

def faktorial(n):
    hasil = 1
    for i in range(1, n+1):
        hasil *= i

    return hasil

faktorial = faktorial(5)
print(faktorial)


def hubungan( *args, **kwargs ):
    print(f"{args[0]} dengan {args[1]} mempunyai hubungan berupa {kwargs.get('hubungan')}")

hubungan("freya", "ibnu", hubungan = "pasangan")


