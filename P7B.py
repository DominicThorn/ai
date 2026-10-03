import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[6, 5, 4], [3, 2, 1]])

print("Array A: ")
print(A)

print("In Array B:")
print(B)

print("In Addition of A and B:")
print(A + B)

print("In Subtraction of A and B: ")
print(A - B)

print("In Multiplication of A and B:")
print(A * B)

print("In Transpose of Array A:")
print(A.T)

print("In Sum of elements in Array A: ")
print(np.sum(A))

print("In Maximum element in Array A: ")
print(np.max(A))

print("In Minimum element in Array A: ")
print(np.min(A))
