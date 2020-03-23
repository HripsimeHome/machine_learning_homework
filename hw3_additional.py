import numpy as np

# Numpy Basic Operations
# Convert from list to ndarray
numpy_array = np.array([5, 2])
print(numpy_array)

# Generating random ndarray
# Example 1
rarray = np.random.rand(2,2) # 2x2 array of number from 0 to 1
print(rarray)

# Example 2
rarray = np.random.rand(3,2)*15 # 3x2 array of number from 0 to 15
print(rarray)

#Creating array of zeros
zarray = np.zeros((2,3)) # 2x3 array with 0s
print(zarray)

#Create an array and fill with some values
varray = np.full((2, 3), 7) # 2x3 array with 7s
print(varray)

# Odnomerni-i depqum ktpi mi hatik element@
a = np.array([1, 2, 3])
print (a[1])

# Dvumerni-i depqum ktpi index-ov massiv@
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
print(arr[1])

# Trexmerni-i depqum ktpi @ndhanur arandnacvvac massiv@
arr = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],[[10, 11, 12], [13, 14, 15], [16, 17, 18]]])
print(arr[1])

#Numpy Sorting & Reshaping

print("Sort")
arr = np.array([50, 60, 70, 20])
print(np.sort(arr))

print("Transpose") # Perestavlyaet osi x, y
a = np.array([[1, 2], [3, 4]])
print(a.T)

# Reshape
print("Reshape example 1")
arr1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr1d)
arr2d = np.reshape(arr1d, (-1, 3))
print(arr2d)

print("Reshape example 2")
a = np.array([[1,2,3], [4,5,6]])
print(np.reshape(a, 6))
print(np.reshape(a, 6, order='F'))

print("Reshape Matrix example 3")
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [10, 11, 12]])
print(matrix.reshape(6, 2))

print("Reshape example 4")
x = np.array([[2,3,4], [5,6,7]])
print(np.reshape(x, (3, 2)))

# Resize
print("Resize")
a = np.array([[1, 2], [3, 4]])
print(np.resize(a, (3, 2))) # po okonchanii povtoryayetsya

print("Size of array")
arr = np.array([50, 60, 70, 20])
print(np.size(arr))

# Concatenate
print("Concatenate") # add array 2 as columns to the end of array 1
array1 = np.array([[1, 3, 5, 8, 15], [5, 20, 30, 40, 10]])
array2 = np.array([[60, 1, 3, 5, 7], [50, 77, 88, 99, 102]])
array_result = np.concatenate((array1, array2), axis=1)
print(array_result)

#Split
print("Split")
a = np.array([1, 2, 3, 4, 5, 6]) # bajanum e 3 submassiv-i
print(np.split(a, 3))

# Append
print("Append")
first_array = ([40, 22, 35, 55])
second_array = np.append (first_array, [7, 23, 56, 88, 44, 78])
print (second_array)

# Insert
print("Insert")
a = np.array([5, 10, 20, 19, 22])
b = np.insert(a, 3, [17, 18])
print(b)

# Delete Row
print("Delete row")
arr = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(np.delete(arr, 2, 0)) # 2-rd ryad@  [9, 10, 11, 12] ]jnjvec - 0-n da axis=0

# Delete Column
print("Delete column")
arr = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(np.delete(arr, 3, 1)) # 3 elementi indexov kolonkan  [4, 8, 12] jnjvec - 1-@ da axis=1

# Minimum
print("Minimum")
arr = ([5, 60, 2])
print(np.min(arr))

# Maximum
print("Maximum") # nuin@ minimumi hamar
b = np.array([[1, 20, 13, 4, 5], [16, 70, 18, 92, 1]])
print(np.max(b, axis=0)) # max of each column
print(np.max(b, axis=1)) # max from row,arandzin 1-ic [1, 20, 13, 4, 5], arandzin 2-ic [16, 70, 18, 92, 1]
