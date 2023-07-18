import numpy as np
np.set_printoptions(legacy = '1.13')
row, column  = input().split()
row = int(row)
column = int(column)
print(type(row))
print(type(column))

print(np.eye(row, column))
# print(np.eye(row, column))
