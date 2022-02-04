import numpy as np
a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(a)

# Get a specific element
print(a[1][5])

# Get a specific row
print(a[0])
print(a[0, :])

# Get a specific column
print(a[:, 3])

# Getting a little more fancy [startIndex:endIndex:stepSize]
print(a[0, 1:6:2])

# Change Value
a[1, 5] =30
print(a)
