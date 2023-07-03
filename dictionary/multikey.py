anggota1 = {
    'name' : 'ibnu topan',
    'gender': 'male',
    'age' : 22
}
anggota2 = {
    'name' : 'abdul manaf',
    'gender': 'male',
    'age' : 19
}
anggota3 = {
    'name' : 'erik permana',
    'gender': 'male',
    'age' : 19
}

data_anggota = {
    'anggota': anggota1,
    'anggota1': anggota2,
    'anggota2': anggota3,

}

for key in data_anggota.keys():
    print(f"nama anggota:\t{data_anggota[key]['name']}")
    print(f"jenis kelamin anggota:\t{data_anggota[key]['gender']}")
    print(f"umur anggota:\t{data_anggota[key]['age']}")