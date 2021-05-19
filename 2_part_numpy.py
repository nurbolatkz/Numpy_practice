import numpy as np

#arange()
my_arr =  np.arange(5, dtype = float)
print("array crated with arange - ", my_arr)


#ones
my_arr = np.ones((2,3), dtype = float)
print("Array filled with only 1  = ", my_arr)

#zeros
my_arr = np.zeros((2,3), dtype = int)
print("Array filled with only 0  = ", my_arr)

#zeros_like

a = np.array([[1,2,3], [4,5,6]], float)
d = np.zeros_like(a)
print("Array filled with only 0  = ", d)

#ones_like
d = np.ones_like(a)
print("Array filled with only 1  = ", d)


#indentity
id_arr = np.identity(4, dtype = float)
print("Arrar = ", id_arr)

#eye
eye_arr =  np.eye(4, k = 2, dtype = float)
print("New array ", eye_arr)

#math operations

a = np.array([4, 5, 6], float)
b = np.array([5, 2 ,6], dtype = float)
print("a + b = ", a + b)

# -
print("a - b = ", a - b )
# *
print("a * b = ", a * b)
# /
print("a / b = ", a / b)
# **
print("a ** b = ", a ** b)

#2d array !note size should be equal

a =  np.array([[1, 2], [3, 4]], float)
b = np.array([[2, 0], [1, 3]], float)
print("a * b(2D array) = ", a * b )

# if size not equal
a = np.array([[1, 2], [3, 4], [5, 6]], float)

b = np.array([-1, 3], float)
print(a)
print(b)
print("a + b  = ", a + b)

# abs, sign, sqrt, log, log10, exp, sin, cos, tan, arcsin, arccos, arctan, sinh, cosh, tanh, arcsinh, arccosh, arctanh
a = np.array([1, 4, 9], float)
print(np.sqrt(a))

a = np.array([1.1, 1.5, 1.9])
#floor
print("Floor method = ", np.floor(a))
#ceil
print("Ceil method = ", np.ceil(a))
#rint
print("Rint method = ", np.rint(a))
#constants pi, e
print("Pi = ", np.pi)
print("e = ", np.e)

#loops on numpy arrays
a = np.array([1,2,3,5], int)
sums = 0
for i in a:
          sums += i
          print(i)
print("Sum of arrays = ", sums)

#2D array
a = np.array([ [1, 2],
               [3, 4],
               [5, 6]

              ], float)
k = 1
for row in a :
          print(k, "- row of array = ", row)
          k += 1
a = np.array([ [1, 2],
               [3, 4],
               [5, 6] ], float)
for (x, y) in a:
          print("x * y = ", x * y)

#basic operations
a = np.array([2, 4, 3], float)
print("Sum of array = ", a.sum())
print("Prod method = ", a.prod() ) #2 * 4 * 3 = 24

a = np.array([2, 1, 9], float)
print("Mean of array  = ", a.mean())
print("Variation of array = ", a.var())
print("Deviattion of array = ", a.std())
          
#max and min
print("Max of arr = ", a.max())
print("Min of arr = ", a.min())

#argmin and argmax
print("Index of max element = ", a.argmax())
print("Index of min element  = ", a.argmin())


a = np.array([[0, 2], [3, -1], [3, 5]], float)
print("Mean by row = ", a.mean(axis = 0))
print("Min by col = ", a.min(axis = 1))

#sort
a = np.array([6,2, 4,  2, 5, -1, 0], float)
print("Sorted array  = ", sorted(a))
a.sort()
print("Sorted array  = ", a)

#unique element of array
print("unique element of array = ", np.unique(a))

#diagonal
a = np.array([[0, 2], [3, -1], [3, 5]], float)
print("Diagonal of array = ", a.diagonal())
#LET'S GO 3RD PART OF LEARNING
