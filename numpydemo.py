import pandas as pd
import numpy as np

# 1D Vector using Pandas Series
vector_1d_pd = pd.Series([1, 2, 3, 4, 5])
print("Pandas 1D Vector (Series):")
print(vector_1d_pd)

# 2D Matrix using Pandas DataFrame
matrix_2d_pd = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nPandas 2D Matrix (DataFrame):")
print(matrix_2d_pd)

# Arange Vector using Pandas Series with numpy arange
arange_vector_pd = pd.Series(np.arange(0, 10, 2))
print("\nPandas Arange Vector (Series):")
print(arange_vector_pd)

# Zeros Matrix using Pandas DataFrame with numpy zeros
zeros_matrix_pd = pd.DataFrame(np.zeros((2, 3)))
print("\nPandas Zeros Matrix (DataFrame):")
print(zeros_matrix_pd)

# Ones Vector using Pandas Series with numpy ones
ones_vector_pd = pd.Series(np.ones(4))
print("\nPandas Ones Vector (Series):")
print(ones_vector_pd)

# Random Matrix using Pandas DataFrame with numpy random
random_matrix_pd = pd.DataFrame(np.random.rand(3, 2))
print("\nPandas Random Matrix (DataFrame):")
print(random_matrix_pd)

# Vector Addition using Pandas Series
vector_a_pd = pd.Series([10, 20, 30])
vector_b_pd = pd.Series([1, 2, 3])
addition_result_pd = vector_a_pd + vector_b_pd
print("\nPandas Vector Addition (Series):")
print(addition_result_pd)

# Scalar Multiplication using Pandas Series
scalar = 5
scalar_multiplication_result_pd = vector_a_pd * scalar
print("\nPandas Scalar Multiplication (Series):")
print(scalar_multiplication_result_pd)

# Matrix Multiplication using Pandas DataFrame (using to_numpy for matrix op)
matrix_x_pd = pd.DataFrame([[1, 2], [3, 4]])
matrix_y_pd = pd.DataFrame([[5, 6], [7, 8]])
matrix_multiplication_result_pd = pd.DataFrame(matrix_x_pd.to_numpy() @ matrix_y_pd.to_numpy())
print("\nPandas Matrix Multiplication (DataFrame):")
print(matrix_multiplication_result_pd)

# Transposed Matrix using Pandas DataFrame
transposed_matrix_pd = matrix_x_pd.T
print("\nPandas Transposed Matrix (DataFrame):")
print(transposed_matrix_pd)

# Sum of Matrix Elements using Pandas DataFrame
sum_of_elements_pd = matrix_2d_pd.sum().sum() # sum() twice to sum all elements in DataFrame
print("\nPandas Sum of Matrix Elements (DataFrame):")
print(sum_of_elements_pd)

# Mean Value of Vector using Pandas Series
mean_value_pd = vector_1d_pd.mean()
print("\nPandas Mean Value of Vector (Series):")
print(mean_value_pd)

# Max Value of Matrix using Pandas DataFrame
max_value_pd = matrix_2d_pd.max().max() # max() twice to get max of all elements in DataFrame
print("\nPandas Max Value of Matrix (DataFrame):")
print(max_value_pd)

# Reshaped Matrix using Pandas DataFrame (reshape numpy array then to DataFrame)
reshaped_matrix_pd = pd.DataFrame(vector_1d_pd.values.reshape(5, 1))
print("\nPandas Reshaped Matrix (DataFrame):")
print(reshaped_matrix_pd)

# Sliced Vector using Pandas Series
sliced_vector_pd = vector_1d_pd[1:4]
print("\nPandas Sliced Vector (Series):")
print(sliced_vector_pd)