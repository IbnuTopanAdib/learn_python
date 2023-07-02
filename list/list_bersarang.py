hero_1 = ["YuZhong", "Fighter", "Exp"]
hero_2 = ["Kagura", "Mage", "Mid"]
hero_3 = ["Yve", "Mage", "Mid"]

daftar_hero = [hero_1, hero_2, hero_3]

for hero in daftar_hero:
    print(f"nama\t: {hero[0]}")
    print(f"role\t: {hero[1]}")
    print(f"lane\t: {hero[2]}\n")

# mengambil data dari nested list
nama_hero_1 = daftar_hero[0][0]
print(f"nama hero 1 {nama_hero_1}")


# mengcopy nested list dengan deepcopy
from copy import deepcopy

a = [[1,2,3],
     [4,5,6]]

b = deepcopy(a)

alamat_nested_list_a = hex(id(a))
alamat_nested_list_b = hex(id(b))

print(f"alamat nested list a\t: {alamat_nested_list_a}")
print(f"alamat nested list b\t: {alamat_nested_list_b}")

alamat_list_didalam_nested_list_a = hex(id(a[0]))
alamat_list_didalam_nested_list_b = hex(id(b[0]))

print(f"alamat nested list a\t: {alamat_nested_list_a}")
print(f"alamat nested list b\t: {alamat_nested_list_b}")


# memodifikasi elemen dari a
a[0][1] = 12

print(a)
print(b)
# elemen a berubah tapi elemen b tidak berubah yang menandakan kita berhasil mengcopy list a dengan deepcopy()