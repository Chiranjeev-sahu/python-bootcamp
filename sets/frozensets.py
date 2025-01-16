# A frozenset in Python is an immutable version of a set.
fset = frozenset([1, 2, 3, 4, 5])
print(fset) 
# Regular sets are mutable and unhashable, so they cannot be used as dictionary keys.
# frozenset is immutable and hashable, making it suitable for use as keys

# Using frozenset as a dictionary key
dict_keys = {frozenset({1, 2, 3}): "value"}
print(dict_keys)  # Output: {frozenset({1, 2, 3}): 'value'}

# Using frozenset as an element in a set
set_of_fsets = {frozenset({1, 2}), frozenset({3, 4})}
print(set_of_fsets)  # Output: {frozenset({3, 4}), frozenset({1, 2})}

# operations:
fset1 = frozenset({1, 2, 3})
fset2 = frozenset({3, 4, 5})

# Union
union_set = fset1 | fset2
print("Union:", union_set)  # Output: frozenset({1, 2, 3, 4, 5})

# Intersection
intersection_set = fset1 & fset2
print("Intersection:", intersection_set)  # Output: frozenset({3})

# Difference
difference_set = fset1 - fset2
print("Difference:", difference_set)  # Output: frozenset({1, 2})

# Symmetric Difference
symmetric_diff = fset1 ^ fset2
print("Symmetric Difference:", symmetric_diff)  # Output: frozenset({1, 2, 4, 5})

# When to Use frozenset?
# When you need an immutable set.

# When you need to use a set as a key in a dictionary or as an element in another set.

# When you want to ensure that the set cannot be modified accidentally.