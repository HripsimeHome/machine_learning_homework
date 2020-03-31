import numpy as np

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


# Numpy Math operations
print("Add example 1")
a = np.array([12, 24, 33])
print(np.add(a, 12)) # amen elementin gumarvum e 12

print("Add example 2")
a = np.array([10, 20, 30])
b = np.array([14, 22, 3])
print(np.add(a, b))

print("Subtract example 1")
a = np.array([[15, 22, 32],[28, 39, 48]])
b = np.array([[1, 2, 3], [2, 2, 2]])
print(np.subtract(a, b))

print("Subtract example 2")
a = np.array([[24, 42, 132],[208, 309, 418]])
b = np.array([[10, 12, 3], [8, 9, 18]])
print(np.subtract(a[1], b[1]))

print("Multiply example 1")
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([2, 4, 10])
print(np.multiply(a, b))

print("Multiply example 2")
a = np.array([ [[10, 20, 30], [40, 50, 60]],
              [[70, 80, 90], [33, 56, 70]] ])
b = np.array([ [[1, 4, 3], [2, 5, 6]],
              [[7, 10, 20], [3, 5, 7]] ])
print(np.multiply(a, b))

print("Divide")
a = np.array([[[10], [20], [30]], [[40], [50], [60]]])
b = np.array([[[2], [4], [10]], [[5], [25], [30]]])
print(np.divide(a, b))

print("Power")
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.power(a, 2))

print('Square root')
a = np.array([16,25,36, 49,64,81])
print(np.sqrt(a[2:]))

print('Sinus')
a = np.array([30, 45, 60, 180])
print(np.sin(a))

print('Log')
a = np.array([130, 45, 60, 180])
print(np.log(a))

print('Abs') #Абсолю́тная величина́, или мо́дуль числа — неотрицательное число
a = np.array([[-18, 18], [5, -5]])
print(np.abs(a))

print("Equal True example") # True if two arrays have the same elements, False otherwise.
a = np.array([[[203, 2], [506, 3], [785, 4], [300, 5]], [[551, 6], [978, 7], [20, 1], [16, 90]]])
b = np.array([[[203, 2], [506, 3], [785, 4], [300, 5]], [[551, 6], [978, 7], [20, 1], [16, 90]]])
print(np.array_equal(a, b)) # the same shape and elements

print("Equal False example")
a = np.array([[[203, 2], [506, 3], [785, 4], [300, 5]], [[551, 6], [978, 7], [20, 1], [16, 90]]])
b = np.array([[[3, 2], [56, 3], [75, 4], [30, 50]], [[51, 65], [78, 75], [20, 12], [160, 950]]])
print(np.array_equal(a, b)) #different elements

# Rounding
print("Rounding")
a = np.array([1.2, 3.9, 15.4, 62.5, -5.2])
print(np.ceil(a))
print(np.floor(a))
print(np.round(a))


print("Mean")
a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(np.mean(a, axis=0))

print("Sum example 1")
a = np.array([[10, 20, 30], [40, 50, 60]])
print(np.sum(a, axis=1))

print("Sum example 2")
b = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(np.sum(b))

print("Variance")
a = np.array([[1, 2], [3, 4]])
print(np.var(a))

print("Standard deviation")
a = np.array([[1, 2], [3, 4]])
print(np.std(a, axis=1))

print("Correlation coefficient")
#Коэффициент корреляции - это величина, которая может варьировать в пределах от +1 до -1.
# В случае полной положительной корреляции этот коэффициент равен плюс 1, а при полной отрицательной - минус 1.

x = np.array([50, 15, 30])
y = np.array([27, 45, 55])
print(np.corrcoef(x, y))

print("Median") # медиана — это такое число выборки, что ровно половина из элементов выборки больше него, а другая половина меньше него
a = np.array([[10, 20, 30], [40, 50, 60]])
print(np.median(a))



#Linear Regression

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Apranqi vacharq
x = np.array([100, 120, 110, 130, 135]).reshape(-1, 1)
y = np.array([105, 125, 95, 110, 120])

model = LinearRegression().fit(x, y)
print("R squared", model.score(x, y))
print("Intercept: ", model.intercept_)
print("Slope: ", model.coef_)
y_pred = model.intercept_ + model.coef_ * x
print('Predicted response:', y_pred) # Vax@ klini

plt.scatter(x, y, color="r")
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(x, model.predict(x))
plt.show()