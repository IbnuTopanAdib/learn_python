data_list = ["Freya", "Ibnu"]
def penjumlahan(a, b):
    return a + b

data_dict = {
    'buah' : ['Semangka', 'Pisang', 'Alpukat'],
    'nama' : 'Ibnu',
    'jurusan' : 'Informatika',
    1 : '1',
    'couple' : data_list,
    'dict_baru' : {
        'kucing' : 'meong',
        'sapi' : 'moo',
        'anjing' : 'guk guk'
    },
    'penjumlahan' : penjumlahan(2, 4)
}

print(data_dict['buah'])
print(data_dict['nama'])
print(data_dict['jurusan'])
print(data_dict[1])
print(data_dict['couple'][0])
print(data_dict['dict_baru']['anjing'])
print(data_dict['penjumlahan'])