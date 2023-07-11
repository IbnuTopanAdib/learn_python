import os

os.system("cls")

def kuadrat(a):
    return a **2

hasil = kuadrat(5)
print(hasil)


# format penulisan lambda function output =lambda argument: expression
hasil = lambda n : n**2
print(hasil(10))


## dua argument
hasil = lambda x, y : x**y
print(hasil(10, 10))


## kegunaan lambda function

mylist = ["ibnu", "john", "jane"]
mylist.sort()

print(mylist)

## urutin pake panjang nama nya
# bikin fungsi dulu 

def panjang(nama):
    return len(nama)

mylist.sort(key = panjang, reverse = True)
print(mylist)

## kita gunain lambda

mylist.sort(key = lambda x : len(x), reverse = True)
print(mylist)

# filter dengan lambda
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def kurang_dari_lima(x):
    return x < 5
data_baru = list(filter(kurang_dari_lima, data))

print(data_baru)

# kita juga bisa menggunakan lambda

data_baru = list(filter(lambda x: x>=3 , data))
print(data_baru)

#kita bisa juga membuat bilangan genap 

data_genap = list(filter(lambda x: x%2 ==0, data))
print(data_genap)

data_ganjil = list(filter(lambda x: x%2!=0 , data))
print(data_ganjil)

#kita bisa juga membuat bilangan kelipatan
data_kelipatan_3 = list(filter(lambda x: x%3==0 , data))
print(data_kelipatan_3)

