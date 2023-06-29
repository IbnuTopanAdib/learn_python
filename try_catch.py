# apaya = int(input("masukan angka"))
# list1 = [0,1,2,3,4,5,6,7,8,9,10]

# try:
#     for angka in list1 :
#         pembagian = apaya/angka
#         print(pembagian, end = "")
# except ZeroDivisionError:
#     print("sepertinya list mengandung bilangan 0 deh")
# else:
#     print("mantap")
# finally:
#     print("oke")
filename = "assets/apaantuh.txt"

try:
    with open(filename, 'r') as f:
        readsize = 100
        content = f.read(readsize)
        while len(content)> 0:
            print(content)
            content = f.read(readsize)
except Exception as e:
    print(e)
