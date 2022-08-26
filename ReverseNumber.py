'''Reversing a number in Numpy arrays...'''

import numpy as np

x = int(input("Enter a number :"))
if x == 0:
    print(0)
# If value greater than 0
elif x > 0:
    # The number is converted as a string, then broken down to a list and then passed as an array
    array = np.array(list(str(x)))
    # Reversing the array and then joining
    print(int("".join(array[::-1])))
# If value lesser than 0
else:
    # The number is converted to a string in absolute form, then broken down to a list and then passed as an array
    array = np.array(list(str(abs(x))))
    # Reversing the array and then joining
    print(int("-".join(array[::-1])))