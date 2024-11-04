#Identity operators in Python (is and is not) are used to check if two variables point to the same object in memory.

# Using `is`
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)       # True, since `b` points to the same object as `a`
print(a is c)       # False, since `c` is a separate object with the same value as `a`

# Using `is not`
print(a is not c)   # True, as `a` and `c` are different objects in memory


'''Identity vs. Equality
Identity (is): Checks if two references are to the same object.
Equality (==): Checks if the values of two variables are the same.
Example:'''
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)    # True, as x and y have the same values
print(x is y)    # False, as x and y are different objects in memory



