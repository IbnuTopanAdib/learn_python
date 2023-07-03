filename = "puisi.txt"


# with open(filename, 'r') as f:
#     f_contents = f.read()
#     print(f_contents)

# membuat isi contentg dari file menjadi sebuah list
# with open(filename, 'r') as f:
#     file_contents = f.readlines()
#     print(file_contents)

# read file line by line using built in method readline
# with open(filename, 'r') as f:
#     file_content = f.readline()
#     print(file_content, end = "")
#     file_content = f.readline()
#     print(file_content, end = "")

# untuk mengurangi memori kita bisa mengiterasi seluruh line didalam file
# with open(filename, "r") as f:
#     for line in f:
#         print(line, end = "")

# kita juga bisa menspesifikasi berapa line yang akan dibaca oleh read() method
with open(filename, 'r') as f:
    read_size = 10
    content = f.read(read_size) # akan membaca 10 karakter pertama
    print(f.tell())
    while len(content) > 0:
        print(content, end= "[]")
        content = f.read(read_size)