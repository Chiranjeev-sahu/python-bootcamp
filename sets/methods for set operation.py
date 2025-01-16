# Set Operations and Methods in Python

# 1. Union (| or union())
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # Using |
print("Union using |:", union_set)  # Output: {1, 2, 3, 4, 5}
union_set = set1.union(set2)  # Using union()
print("Union using union():", union_set)  # Output: {1, 2, 3, 4, 5}

# 2. Intersection (& or intersection())
intersection_set = set1 & set2  # Using &
print("Intersection using &:", intersection_set)  # Output: {3}
intersection_set = set1.intersection(set2)  # Using intersection()
print("Intersection using intersection():", intersection_set)  # Output: {3}

# 3. Difference (- or difference())
difference_set = set1 - set2  # Using -
print("Difference using -:", difference_set)  # Output: {1, 2}
difference_set = set1.difference(set2)  # Using difference()=> this converts the argument tp the set if it can be
print("Difference using difference():", difference_set)  # Output: {1, 2}

# 4. Symmetric Difference (^ or symmetric_difference())
symmetric_diff = set1 ^ set2  # Using ^
print("Symmetric difference using ^:", symmetric_diff)  # Output: {1, 2, 4, 5}
symmetric_diff = set1.symmetric_difference(set2)  # Using symmetric_difference()
print("Symmetric difference using symmetric_difference():", symmetric_diff)  # Output: {1, 2, 4, 5}

# 5. Subset (<= or issubset())
set1 = {1, 2}
set2 = {1, 2, 3, 4}
is_subset = set1 <= set2  # Using <=
print("Subset using <=:", is_subset)  # Output: True
is_subset = set1.issubset(set2)  # Using issubset()
print("Subset using issubset():", is_subset)  # Output: True

# 6. Superset (>= or issuperset())
set1 = {1, 2, 3, 4}
set2 = {1, 2}
is_superset = set1 >= set2  # Using >=
print("Superset using >=:", is_superset)  # Output: True
is_superset = set1.issuperset(set2)  # Using issuperset()
print("Superset using issuperset():", is_superset)  # Output: True

# 7. Disjoint (isdisjoint())
set1 = {1, 2, 3}
set2 = {4, 5, 6}
is_disjoint = set1.isdisjoint(set2)  # Using isdisjoint()
print("Are sets disjoint?:", is_disjoint)  # Output: True