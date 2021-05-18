import numpy as np

# numpy array
a = np.array([1, 4, 5, 8], float)
print("my numpy array - ", a, "and  type of array = ", type(a))

print("First two elem of array - ", a[:2])
print("Element at index 3 - ", a[3])
print("First element of array - ", a[0])
print("Just print arrray ", a)


# numpy 2Darray
a = np.array([ [1, 2, 3],
               [4, 5, 6]
              ], float)
print("2D numpy array - ", a)
print("First element of 2D array - ", a[0][0])
print("Element at index 2 in first row - ", a[0][2])

# Array slicing

a = np.array([[1, 2, 3], [4, 5, 6]], float)
print("Select second row of 2D np array - ", a[1,:])
print("Select only first two elem in first row - ", a[0, :2])
print("Select only first two elem of 2 row - ", a[ :, :2])

#methods shape, dtype, len, in, len, reshape, copy, tolist, tostring, fromstring, transpose, flatten, concatenate
print("Shape of array = ", a.shape)
print("Dtype of array = ", a.dtype)
#check occurance
print( 2 in a, 0 in a, 9 in a)
#reshape
n_10 =  np.array(range(10), float)
print("new array with 10 elem - " ,  n_10)
reshaped = n_10.reshape(5, 2)
#it does not modificate array it just create new array
print("Shaped array = ", reshaped)
reshaped2 =  n_10.reshape(2, 5)
print("Shaped 2 row with 5 elem", reshaped2)

a = np.array([1, 2, 3], float)
b =  a
c = a.copy()
#change the first elem
a[0] = 0
print("a array  = ", a)
print("b array  = ", b)
print("c array(with copy method)", c)

# tolist
a = np.array([1, 2, 3], float)
print("List a = ", a.tolist(), " same method with list() = ", list(a))
#tosring method
a = np.array([1, 2, 3], float)
s = a.tobytes()

print("String version = ", s)
#fromsring method
#d = np.fromstring(s)
#print("Fromstring to array", d)
d = np.frombuffer(s, dtype=np.float64)
print("With frombuffer method", d)

#array with same values
a = np.array([1, 2, 3], float)
a.fill(0)
print("Full with zeros", a)

# a.transpose()
a = np.array(range(6), float).reshape((2, 3))
print("a array = ", a)
print("tranposed array", a.transpose())
#flatten() method
a = np.array([[1, 2, 3], [4, 5, 6]], float)
print("Take array ", a.flatten())


a = np.array([1,2], float)
b = np.array([3,4,5,6], float)
c = np.array([7,8,9], float)
d = np.concatenate((a, b, c))
print("Concatenated = ", d)
#Concatenate with 2D array
a = np.array([[1, 2], [3, 4]], float)
b = np.array([[5, 6], [7,8]], float)
print("Concatenate by default ",  np.concatenate((a,b)))

print("Concatenate by row ",  np.concatenate((a,b), axis = 0))

print("Concatenate by row ",  np.concatenate((a,b), axis = 1 ))

#newaxis
a = np.array([1, 2, 3], float)
d = a[:,np.newaxis]
print("a = ", d, " shape = ", d.shape)
c = d[np.newaxis,:]
print("b = ", c , "shape = ", c.shape)












