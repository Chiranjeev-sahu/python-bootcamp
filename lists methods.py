#append,extend,insert

#append-takes one argument,adds a singel elemnet
l1=[1,2.2,'abc']
l1.append(['X','Y'])
print(l1)

# extend: adds all items from an iterable (like another list) to the end of a list.
l1.extend(['X','Y'])
print(l1)

# insert adds a single item at a specific index within a list.
years=[2020,2022,2023]
years.insert(1,2021)
print(years)
#gotchas:
years.insert(-1,2025)#inserts on the second to last position
print(years)


#list.clear(): clears the whole thing
years.clear()
print(years)

#list.pop(): removes last element by default,but can take index as argument too

l2=[10,20,30,40]
x=l2.pop()
print(x)
print(l2)

y=l2.pop(1)# => 20
print(f"y={y},{l2}")

# l2.pop(100)#=> error

# list.remove(): removes the first match of the first occurrance of the given element
l3=[10,20,30,40,20]
l3.remove(10)
print(l3)

#Index,coun,sort,max,min,sum

#list.index(): find the first occurance from thr entire sequence but the search limit can be given 
my_list = [10, 20, 30, 20, 40, 20]
index_of_20 = my_list.index(20)  # Find the first 20 (default: start from 0)
print(index_of_20)      # Output: 1

index_of_20_from_2 = my_list.index(20, 2) # Find first 20, starting from index 2
print(index_of_20_from_2)     # Output: 3

index_of_20_limited = my_list.index(20, 2,5) # Find first 20 between indices 2 and 5.
print(index_of_20_limited) # Output:3

# list.count()
my_list = [10, 20, 30, 20, 40, 20]
count_of_20 = my_list.count(20)
print(count_of_20)  # Output: 3
my_list = [30, 10, 40, 20]

#sort
my_list.sort()           # Sorts in ascending order
print(my_list)           # Output: [10, 20, 30, 40]
my_list.sort(reverse=True) # Sorts in descending order
print(my_list)           # Output: [40, 30, 20, 10]

my_list2 = ["apple", "Banana", "cherry"]
my_list2.sort() # Sorts alphabetically by default
print(my_list2) # Output: ['Banana', 'apple', 'cherry']
my_list2.sort(key = str.lower) # Sorts alphabetically ignoring case.
print(my_list2) # Output: ['apple', 'Banana', 'cherry']


ages=[10,8,23,40,35]
la=sorted(ages)
print(la,ages)

# list.reverse()
l1=[1,3,'abc',10,'x']
l1.reverse()

#  max(): Get the maximum element
my_list = [10, 30, 20, 40]
maximum = max(my_list)
print(maximum) # Output: 40

l2 = [-9,10,5,100,66]
print(f'max')

# min(): Get the minimum element
my_list = [10, 30, 20, 40]
minimum = min(my_list)
print(minimum)   # Output: 10

my_list2 = ["apple", "Banana", "cherry"]
minimum2 = min(my_list2, key = str.lower)
print(minimum2) # Output: apple

# sum(): Calculate the sum of numeric elements 
my_list = [10, 20, 30, 40]
total = sum(my_list)  # Sum of all items
print(total)       # Output: 100

total_with_start = sum(my_list, 100) # Sum of items plus an additional 100 start value
print(total_with_start) #Output: 200