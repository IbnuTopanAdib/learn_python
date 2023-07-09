# belajar args sampe bisa

def biodata(nama, umur, gajih):
    print(f"{nama} {umur} {gajih}")

biodata("ibnu", 22, 20000000)


data_ibnu = ["ibnu", 22, 30000000]

def bio_baru(argument):
    argument = argument.copy()
    argument[-3] = "Ibnu Topan"
    argument[-2] = 23
    argument[-1] = 40000000
    return argument

print(bio_baru(data_ibnu))


def bio_baru_args(*args):
    '''
    args ini merupakan tuple jadi kia bisa lakukan indexing
    '''
    nama = args[0]
    umur = args[1]
    gajih = args[2]
    print(f"karyawan dengan nama {nama}, berumur {umur} memiliki gajih senilai {gajih}")
        
bio_baru_args("freya", 17, 500000000)


def tambah_tambahan( *args):
    hasil = 0
    for arg in args:
        hasil += arg
    return hasil

hasil = tambah_tambahan(1,2,3,4,1,2,3,4,5,5,6,)

print(hasil)