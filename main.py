import numpy as np

# Create a 2x3 array of random numbers
array = np.random.rand(2, 3)

print("Original Array:")
print(array)

# Perform element-wise multiplication
multiplied_array = array * 10

print("Array After Multiplication by 10:")
print(multiplied_array)

# Calculate the mean of the array
mean_value = np.mean(array)
print("Mean of the Array:")
print(mean_value)
