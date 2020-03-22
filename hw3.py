import numpy as np

# arr=np.array([50, 60, 70, 20])

# print(np.log(arr))



# Indexing
# Numpy Indexing & Slicing

print("1d array indexes")
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18])
print(arr1[1])
print(arr1[4:10])
print(arr1[5:])

print("2d array indexes")
arr2 = np.array([[100, 22, 307], [47, 505, 677], [70, 87, 970], [107, 101, 125], [103, 145, 155], [106, 157, 198]])
print(arr2[1])
print(arr2[-1])
print(arr2[:-3])

print("3d array indexes")
arr3 = np.array([ [[29, 40], [33, 21], [102, 63]],
                  [[56, 789], [89, 502], [405, 906]] ])
print(arr3[1])
print(arr3[:,2])


# Numpy Accessing by Array of Indexes
print("Numpy Accessing by Array of Indexes")
elements = np.array([203, 104, 5569, 30, 8, -5, 698, 20, 10, 18, 36, 457])
indexes = [4, 6, 8, -1]
print(list(elements[indexes]))



print("Sum") #will return the sum of the array
a = np.array([1, 2, 3, 4, 5])
print(np.sum(a))

b = np.array([ [[1, 2, 3, 4, 5]], [[6, 7, 8, 9, 10]]])
print(b)
print(np.sum(b))

print("Multiply array")
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([2, 4, 10])
print(np.multiply(a, b))

a = np.array([ [[10, 20, 30], [40, 50, 60]],
              [[70, 80, 90], [33, 56, 70]] ])
b = np.array([ [[1, 4, 3], [2, 5, 6]],
              [[7, 10, 20], [3, 5, 7]] ])
print(np.multiply(a, b))


