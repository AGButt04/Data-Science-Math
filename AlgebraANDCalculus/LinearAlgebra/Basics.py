import numpy as np

A = np.array([[1,2],[3,4]])
v = np.array([-2,-2,-2,-2])
u = np.array([0,0,0,0])
w = np.array([3,3,3,3])
matrix = np.column_stack((v, u, w))
print(matrix)
print(A.shape)
print(A[:,1])
#Inverse of a matrix
matrix_inv = np.linalg.inv(A)
print(matrix_inv)

# 2 x 3 matrix
A = np.array([[2,3,-4], [-2, 1, -3]])
print("A:", A)
# 2 x 3 matrix
B = np.array([[1,-1,4], [3,-3,3]])
print("B:", B)
# 3 x 2 matrix
C = np.array([[1, 2], [3, 4], [5, 6]])
print("C:", C)

# Calculate D = 4A - 2B
D = 4 * A - 2 * B
print("D:", D)
# Calculate E = AC
E = np.matmul(A, C)
print("E:", E)
# Calculate F = CA
F = np.matmul(C, A)
print("F:", F)

A = np.array([[1, 2, -2], [-1, 3, 0], [0, -2, 1]])
B = np.array([[3, 2, 6], [1, 1, 2], [2, 2, 5]])
print(A)
print(B)
# Matrix Multiplication
AB = np.matmul(A, B)
BA = np.matmul(B, A)
print(AB)
print(BA)
# Transpose of a matrix
A_t = A.T
B_t = B.T
print(A_t)
print(B_t)
# Magnitude of a vector
v = np.array([3, 6, -6])
print(np.linalg.norm(v))

# Solving linear systems of equation
# Represent the following system in NumPy matrix/vector form, then solve for x, y, and z:
'''
2a + 3d - 2c = 4
-c + 4b - a = 1
2d - 2c + 3a - b = 2
-2a + 3c - b = -2
'''
A = np.array([[2, 0, -2, 3], [-1, 0, -1, 4], [3, -1, -2, 2], [-2, -1, 3, 0]])
b = np.array([4, 1, 2, -2])
a, b, c, d = np.linalg.solve(A, b)
print(f"a: {a}, b: {b}, c: {c}, d: {d}")
