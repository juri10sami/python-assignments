import random

import numpy as np
array_2d = np.zeros((4, 5))
print(array_2d)


# Create a 2D list of size 4x5 using np.zeros
array_2d_reshaped = np.reshape(array_2d, (5, 4))
print(array_2d_reshaped)

# Create a 3D list of size 2x3x4 using np.full and set the value to any double value
array_3d = np.full((2, 3, 4), 1.5)
print(array_3d)

arr = np.arange(255, 476, 0.5).reshape(476-255, 2)
print(arr)

array_2d = np.linspace(2.5, 75.5, 200).reshape(-1, 1)
print(array_2d)

# Create a list of 100 integer values
values = list(range(1, 101))

# Shuffle the list using random.shuffle()
random.shuffle(values)

# Print the shuffled list
print(values)

# Create a list of 59 integer values
values = list(range(1, 60))

# Select a random element from the list using random.choice()
random_value = random.choice(values)

# Print the selected random value
print("Randomly selected value:", random_value)