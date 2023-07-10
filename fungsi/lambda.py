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



