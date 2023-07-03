import random 
import string

template_anggota = {
    'name' : "Ibnu",
    'age' : 20,
    'gender' : "Male",
}
data_anggota = {}
while True:
    anggota = dict.fromkeys(template_anggota.keys())
    anggota['name'] = input("Masukan nama anggota: ")
    anggota['age'] = int(input("Masukan umur anggota: "))
    anggota['gender'] = input("Masukan gender anggota: ")
    print()
    KEY = "".join(random.choice(string.ascii_lowercase) for i in range(1, 7))
    data_anggota.update({KEY: anggota})
    for key in data_anggota.keys():
        print(f"key:\t{key}")
        print(f"nama anggota:\t{data_anggota[key]['name']}")
        print(f"jenis kelamin anggota:\t{data_anggota[key]['gender']}")
        print(f"umur anggota:\t{data_anggota[key]['age']}\n")

    udahan = input("apakah sudah selesai? (y/n): \n")
    if udahan == "y":
        break
