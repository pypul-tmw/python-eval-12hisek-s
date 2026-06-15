import numpy as np

# ----------------------------
# 1. Creating arrays
# ----------------------------
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

print("Array a:", a)
print("Array b:", b)

# ----------------------------
# 2. Basic operations
# ----------------------------
print("\nAddition:", a + b)
print("Subtraction:", b - a)
print("Multiplication:", a * b)
print("Division:", b / a)

# ----------------------------
# 3. Scalar operations
# ----------------------------
print("\nMultiply by 10:", a * 10)

# ----------------------------
# 4. 2D Array (Matrix)

matrix = np.array([
    [1,2,3,4],
    [5,6,7,8]
]
)
print("\nMatrix: \n",matrix)

# 5. shape, size, dimensions

print("\nShape:",matrix.shape)
print("Size:",matrix.size)
print("Dimensions:",matrix.ndim)

# 6. Reshaping
arr = np.array([1,2,3,4,5,6])
reshaped = arr.reshape(2,3)

# 7. Indexing & slicing
print("\n First element:",a[0])
print("Slice:",a[1:4])

#8. Mathematical functions
print("Sum:",np.sum(a))
print("Mean:",np.mean(a))
print("Min:",np.min(a))
print("Max:",np.max(a))

# 9. Axis operations
matrix2 = np.array([[1,2,3],[4,5,6]])
print("\n Column-wise sum:", np.sum(matrix2,axis=0))
print("Row-wise sum:", np.sum(matrix2, axis=1))


# 10. random numbers
print("Random floats:",np.random.rand(3))
print("Random integers:",np.random.randint(1,10,5))