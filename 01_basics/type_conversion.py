# Type Conversion

"""# Two Types
# 1. Type conversion
# 2. Type casting"""


"""# Type conversion is the process of converting one data type to another data type. It is done automatically by the Python interpreter when we perform operations on different data types."""


"""# Type casting is the process of converting one data type to another data type explicitly by the programmer. It is done using built-in functions like int(), float(), str(), etc."""

# EXample of type conversion

a = 2
b = 4.5

sum = a+b  #2.0 + 4.5 == 6.5

# The python automatically converts the int data type of variable a to float data type and then performs the addition operation and returns the result in float data type.

print("The sum of ", a, " and ", b, " is: ", sum)

a = "2"
b = 4.5

# sum = a+b  # This will give an error because we cannot add a string and a float data type.
# This is the error -->    
"""sum = a+b  # This will give an error because we cannot add a string and a float data type.
          ~^~
TypeError: can only concatenate str (not "float") to str"""

# type casting 

c = int(a)
sum = c+b  # This will work because we have converted the string data type of variable a to int data type using int() function and then performed the addition operation and returns the result in float data type.
print("The sum of ", c, " and ", b, " is: ", sum)