# with open('apaantuh.txt', 'w') as f:
#     f.write('aku suka susunya')

# #copy text
# with open('apaantuh.txt', 'r') as rf:
#     with open('apaantuh_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)

# copy image
with open ('shinobu.jpg', 'rb') as rb:

    with open('shinobu_copy.jpg', 'wb') as wb:
        read_size = 2048
        content = rb.read(read_size)
        while len(content) > 0:
            wb.write(content)
            content = rb.read(read_size)
