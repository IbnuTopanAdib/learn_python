# data tuple merupakan data yang tidak bisa dirubah atau dimanipulasi

data_tuple = (1,4,5,6,4,5,3)

print(data_tuple[2])

try:
    data_tuple[0] = "Ibnu"
except TypeError:
    print("gabisa melakukan assignment di tuple")

# data set merupakan data yang bisa diubah namun tidak bisa dilakukan subscription atau indexing
data_set = {2,3,4,5,6,7,8,9,10,11}
# data_set.append(10)
try:
    print(data_set[0])
except TypeError:
    print("gabisa melakukan subscription di set")

