# Python program to print the mean of elements

n_num = [1, 2, 3, 4, 5]                    # List of elements to calculate mean
n = len(n_num) 		                   # Calculate the number of elements
get_sum = sum(n_num)                       # Calculate the sum of elements
mean = get_sum / n	                   # Calculate the mean
print("Mean / Average is: " + str(mean))      #Print result 
        

# Python program to print the median of elements

# List of elements to calculate the median
n_num = [1, 2, 3, 4, 5]

# Number of elements in the list
n = len(n_num)

# Sort the list
n_num.sort()


# Calculate median
if n % 2 == 0:
    median1 = n_num[n // 2]
    median2 = n_num[n // 2 - 1]
    median = (median1 + median2) / 2
else:
    median = n_num[n // 2]

print("Median is:", median)
        

# Python program to print the mode of elements
from collections import Counter

# List of elements to calculate mode
n_num = [1, 2, 3, 4, 5, 5]

# Count the frequency of each element
data = Counter(n_num)

# Get the mode(s)
get_mode = dict(data)
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]

# Check if there is a mode
if len(mode) == len(n_num):
    get_mode = "No mode found"
else:
    get_mode = "Mode is/are: " + ', '.join(map(str, mode))

# Print the result
print(get_mode)


# Python program to get the variance of a list

# Importing the NumPy module
import numpy as np

# Taking a list of elements
numbers = [2, 4, 4, 4, 5, 5, 7, 9]

# Calculating variance using var()
variance = np.var(numbers)

# Printing the variance
print("Variance of the list is:", variance)




# Python program to get the standard deviation of a list

# Importing the NumPy module
import numpy as np

# Taking a list of elements
numbers = [2, 4, 4, 4, 5, 5, 7, 9]

# Calculating standard deviation using std()
std_deviation = np.std(numbers)

# Printing the standard deviation
print("Standard Deviation of the list is:", std_deviation)
