import numpy as np

arr = np.array([1,2,3])

print(arr)

arr2 = np.append(arr, [4,5])
print(arr2)

arr3 = np.delete(arr,[3,4])

print(arr3)

arr4 = np.concatenate((arr,np.array([4,5])),axis=0)

print(arr4)