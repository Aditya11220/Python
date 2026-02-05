# Data Types in Python: 
"""
1. Numeric Data Type: Its a kind of data type which contains numerical values. 
    a. Int: Its a numerical integer value. 
    b. float: its numerical whole number value which can contain decimal also
    c. complex: Its a complex number, decimal number

2. Sequence Data Types: A sequence is an ordered collection of data which is stored and represented sequentially. 
they can be of similar or different kind of data types. 
    a. string: Python strings are arrays of bytes representing unicode characters.
    b. list: Lists are similar to arrays found in different languages, They are an ordered and mutable collection of items. There is no need of data should be of same data type inside a list
    c. Tuple: A Tuple is an ordered collection of python objects. The only difference between a tuple and a list is that tuples are immutable and lists are mutable after creation. 

3. Boolean Data Type: Data type is one of the most basic data types in Python. It can have only two values: True or False.
    a. Truthy and Falsy Values: In python truthy and falsy values are values that evaluate to True or False. 

4. Set Data Type: A set is an unordered collection of data type that is iterable, mutable and has no duplicate values
"""
print("Data Types in Python: ")
## Numeric Data Types
# Int Data type example
a = 3
print("a = ", a)
print(type(a)) # type is a function in python to get the type of data variable has. 

# float data type example
b = 3.33
print("b = ", b)
print(type(b))

# complex data type example
c = 2+3j
print("c = ", c)
print(type(c))

## Sequence Data Types
# string data type example
d = "Hello World"
print("d = ", d)
print(type(d))

# list data type example
e = [1, 2, 3, "Python", 3.33]
print("e = ", e)
print(type(e))

# tuple data type example
f = (1, 2, 3, "Python", 3.33)
print("f = ", f)
print(type(f))

## Boolean Data Type
g = True
print("g = ", g)
print(type(g))

h = False
print("h = ", h)
print(type(h))

# Truthy and Falsy Values
# Truthy values
if 1:
    print("1 is a Truthy value")
if not 0:
    print("0 is a Falsy value")

## Set Data type
# set data type example

s1 = set()
s1 = set("JhonDoeIsRich")
print("set with the use of String: ", s1)

s2 = set()
s2 = set(["Python", "is", "a", "programming", "language"])
print("set with the use of list: ", s2)