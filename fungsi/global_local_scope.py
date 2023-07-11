# belajar local dan global scope

nama_global = "Ibnu" # <- variabel ini merupakan variabel global scope

def sayhi():
    print(f"hello {nama_global}")
# kita bisa mengaksesnya dari mana saja
sayhi()

def sayhello():
    nama_lokal = "Freya" # <- variabel ini merupakan variabel local scope
    print(f"hi {nama_lokal}")

try:
    print(nama_lokal)
except Exception as e:
    print(f"{e}, gabisa akses variabel local")


# penggunaan global scope 1:
nama = "topan"

def sapa(pesan):
    print(f"kepada {nama}, {pesan}")

sapa("hallo, bisa berhenti nonton bokep?")


# mengubah global scope variabel
umur = 17
namanya = "Freya"

def mengubah():
    global umur
    global namanya
    umur += 1
    namanya += " Jayawardana"

print(f"nama sebelum diubah {namanya}")
print(f"umur sebelum diubah {umur}")

mengubah()

print(f"nama setelah diubah {namanya}")
print(f"umur setelah diubah {umur}")

