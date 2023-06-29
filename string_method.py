# memperbersar tulisan dengan fungsi upper

nama = "ibnu topan"
nama = nama.upper()
print(nama)

#memperkecil tulisan dengan method lower
nama = nama.lower()

print(nama)

'''
rstrip()
    Metode pertama yang kita bahas dari kategori awalan dan akhiran adalah rstrip(). Metode ini akan menghapus 
    whitespace pada sebelah kanan string atau akhir string. Berikut contoh penerapan kode pada rstrip()
'''
halilintar = "atta    "
print(halilintar.rstrip())
'''
lstrip()
Selanjutnya kita bahas tentang lstrip() yang bertugas untuk menghapus whitespace pada sebelah kiri atau awal string. Berikut contoh penerapan kodenya:
'''

waduh = "     mamama"

print(waduh.lstrip())


# method strip untuk menghapus whitespace

dragon = "  jitkunedo  "

print(dragon.strip())


# kita juga bisa menentukan mana karakter atau bagian yang ingin dihilangkan, misalnya:
random_word = "formeitsforyouforusitsthem"

print(random_word.strip("for"))

# endswith vs startswith

kalimat = "makanan indonesia"

if (kalimat.endswith("indonesia")):
    print("rendang")
else:
    print("burgir")
kalimat = "kenapa makanan indonesia itu enak?"

if (kalimat.startswith("kenapa")):
    print("pertanyaan")
else:
    print("bukan pertanyaan")