import numpy as np

vector_1d = np.array([1, 2, 3, 4, 5])
print("1D Vector:")
print(vector_1d)

matrix_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D Matrix:")
print(matrix_2d)

arange_vector = np.arange(0, 10, 2)
print("\nArange Vector:")
print(arange_vector)

zeros_matrix = np.zeros((2, 3))
print("\nZeros Matrix:")
print(zeros_matrix)

ones_vector = np.ones(4)
print("\nOnes Vector:")
print(ones_vector)

random_matrix = np.random.rand(3, 2)
print("\nRandom Matrix:")
print(random_matrix)

vector_a = np.array([10, 20, 30])
vector_b = np.array([1, 2, 3])
addition_result = vector_a + vector_b
print("\nVector Addition:")
print(addition_result)

scalar = 5
scalar_multiplication_result = vector_a * scalar
print("\nScalar Multiplication:")
print(scalar_multiplication_result)

matrix_x = np.array([[1, 2], [3, 4]])
matrix_y = np.array([[5, 6], [7, 8]])
matrix_multiplication_result = matrix_x @ matrix_y
print("\nMatrix Multiplication:")
print(matrix_multiplication_result)

transposed_matrix = matrix_x.T
print("\nTransposed Matrix:")
print(transposed_matrix)

sum_of_elements = np.sum(matrix_2d)
print("\nSum of Matrix Elements:")
print(sum_of_elements)

mean_value = np.mean(vector_1d)
print("\nMean Value of Vector:")
print(mean_value)

max_value = np.max(matrix_2d)
print("\nMax Value of Matrix:")
print(max_value)

reshaped_matrix = vector_1d.reshape(5, 1)
print("\nReshaped Matrix:")
print(reshaped_matrix)

sliced_vector = vector_1d[1:4]
print("\nSliced Vector:")
print(sliced_vector)