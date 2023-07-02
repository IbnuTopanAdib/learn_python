a = ["Freya", "Alucard", "Balmond"]
# berikut adalah cara yang salah untuk mengcopy sebuah list
b = a
print(a)
print(b)
# jika kita mengubah salah satu elemen dar list maka list lain  di copy akan berubah
# ini tidak seharusnya terjadi

a[2] = "Aamoon"
print(a)
print(b)

# berikut adalah reference dari list(alamat memori)

print(f"alamat dari list a {hex(id(a))}")
print(f"alamat dari list b {hex(id(b))}")

# mengcopy list dengan method copy list.copy()

c = a.copy()

c[1] = "YuZhong"
print(a)
print(c)

# jika kita mengubah salah satu elemen dar list maka list lain  di copy tidak akan berubah
a[2] = "Kagura"

print(a)
print(c)
