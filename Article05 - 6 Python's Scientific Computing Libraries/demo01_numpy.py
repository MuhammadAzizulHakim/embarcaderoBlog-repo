import numpy as np
 
arr = np.array([7, 10, 3, 11, 29, 15, 18])
# Sort ascending the values in an array
print(np.sort(arr))
 
a = np.array([1, 2, 3, 4, 5, 6])
b = np.array([7, 8, 9, 10, 11, 12])
# Combine the values of two arrays into one
print(np.concatenate((a, b)))
 
# Change the dimension of the array
c = a.reshape(3, 2)
print(c)