import numpy as np
from scipy.sparse import lil_matrix

# Create a 2x6 sparse matrix
sparse_matrix = lil_matrix((2, 6), dtype=np.int32)

# Set some values in the matrix
sparse_matrix[0, 1] = 1
sparse_matrix[0, 3] = 2
sparse_matrix[1, 2] = 3
sparse_matrix[1, 5] = 4

# Print the original sparse matrix
print("Original Sparse Matrix:")
print(sparse_matrix)

# Convert the lil_matrix to a dense NumPy array
dense_array = sparse_matrix.toarray()

# Print the dense array
print("\nDense Array:")
print(dense_array)
