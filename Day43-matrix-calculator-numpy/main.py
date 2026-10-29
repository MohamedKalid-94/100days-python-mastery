# Day 43 - Matrix Calculator
# Concept: NumPy
# Goal: Practice creating and manipulating arrays/matrices using NumPy

# Requires: pip install numpy
import numpy as np

# --- Creating an array from a Python list ---
array_1d = np.array([1, 2, 3, 4, 5])
print("1D array:", array_1d)
print("Type:", type(array_1d))

# --- Creating a 2D array (a matrix) - a list of lists ---
matrix_a = np.array([
    [1, 2, 3],
    [4, 5, 6],
])
print("\nMatrix A:\n", matrix_a)

# --- Useful array properties ---
print("\nShape (rows, columns):", matrix_a.shape)
print("Number of dimensions:", matrix_a.ndim)
print("Total number of elements:", matrix_a.size)
print("Data type of elements:", matrix_a.dtype)

# --- Creating arrays with built-in helper functions ---
zeros = np.zeros((2, 3))          # a 2x3 matrix of all zeros
ones = np.ones((3, 3))            # a 3x3 matrix of all ones
identity = np.eye(3)              # a 3x3 identity matrix (1s on the diagonal)
range_array = np.arange(0, 10, 2)   # like Python's range(), but returns an array

print("\nZeros:\n", zeros)
print("\nOnes:\n", ones)
print("\nIdentity matrix:\n", identity)
print("\nRange array:", range_array)

# --- Creating a second matrix for arithmetic ---
matrix_b = np.array([
    [7, 8, 9],
    [10, 11, 12],
])
print("\nMatrix B:\n", matrix_b)

# --- Element-wise arithmetic - operations apply to EVERY matching element ---
print("\n--- Element-wise operations ---")
print("A + B:\n", matrix_a + matrix_b)
print("A - B:\n", matrix_a - matrix_b)
print("A * B (element-wise, NOT matrix multiplication):\n", matrix_a * matrix_b)
print("A * 2 (scalar multiplication):\n", matrix_a * 2)

# --- Real matrix multiplication - uses @ or np.dot(), NOT * ---
# For this, the number of columns in A must match the number of rows in B
matrix_c = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
])
print("\nMatrix A shape:", matrix_a.shape, "| Matrix C shape:", matrix_c.shape)
matrix_product = matrix_a @ matrix_c   # (2x3) @ (3x2) = (2x2)
print("A @ C (real matrix multiplication):\n", matrix_product)

# --- Transposing a matrix - flips rows and columns ---
print("\nMatrix A transposed:\n", matrix_a.T)

# --- Reshaping an array - same data, different shape ---
flat = np.arange(1, 7)   # [1, 2, 3, 4, 5, 6]
reshaped = flat.reshape(2, 3)
print("\nFlat array:", flat)
print("Reshaped to 2x3:\n", reshaped)

# --- Indexing and slicing - similar to lists, but with two dimensions ---
print("\n--- Indexing ---")
print("Element at row 0, col 1:", matrix_a[0, 1])
print("Entire first row:", matrix_a[0])
print("Entire second column:", matrix_a[:, 1])
print("Sub-matrix (rows 0-1, cols 0-1):\n", matrix_a[0:2, 0:2])

# --- Aggregate functions ---
print("\n--- Aggregate functions ---")
print("Sum of all elements:", matrix_a.sum())
print("Sum of each column:", matrix_a.sum(axis=0))
print("Sum of each row:", matrix_a.sum(axis=1))
print("Mean:", matrix_a.mean())
print("Max:", matrix_a.max())
print("Min:", matrix_a.min())

# --- Why NumPy instead of plain Python lists? Speed comparison ---
import time

python_list = list(range(1000000))
numpy_array = np.arange(1000000)

start = time.time()
python_result = [x * 2 for x in python_list]
python_time = time.time() - start

start = time.time()
numpy_result = numpy_array * 2
numpy_time = time.time() - start

print(f"\nPython list comprehension time: {python_time:.5f} seconds")
print(f"NumPy vectorized operation time: {numpy_time:.5f} seconds")
print(f"NumPy was roughly {python_time / numpy_time:.1f}x faster")


# ============================================================
# A simple matrix calculator function
# ============================================================
def matrix_calculator(matrix1, matrix2, operation):
    if operation == "add":
        return matrix1 + matrix2
    elif operation == "subtract":
        return matrix1 - matrix2
    elif operation == "multiply":
        return matrix1 @ matrix2
    else:
        return "Invalid operation. Choose add, subtract, or multiply."


print("\n--- Using the matrix calculator function ---")
result = matrix_calculator(matrix_a, matrix_b, "add")
print("Result:\n", result)


# ============================================================
# Interactive part: build and multiply two small matrices
# ============================================================
print("\n--- Build your own 2x2 matrices ---")
print("Enter Matrix 1 (4 numbers, row by row):")
values1 = [float(input(f"  Value {i+1}: ")) for i in range(4)]
user_matrix1 = np.array(values1).reshape(2, 2)

print("Enter Matrix 2 (4 numbers, row by row):")
values2 = [float(input(f"  Value {i+1}: ")) for i in range(4)]
user_matrix2 = np.array(values2).reshape(2, 2)

print("\nMatrix 1:\n", user_matrix1)
print("Matrix 2:\n", user_matrix2)
print("Sum:\n", user_matrix1 + user_matrix2)
print("Product (matrix multiplication):\n", user_matrix1 @ user_matrix2)