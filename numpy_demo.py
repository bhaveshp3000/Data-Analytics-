import numpy as np

my_array = np.array([[1,2,3],[4,5,6]])
print(my_array)

print(my_array.reshape([1,6]))

zero_mat = np.zeros([4,4],dtype=int)

print(zero_mat)

one_mat = np.ones([5,5])
print(one_mat)