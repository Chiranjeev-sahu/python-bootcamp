# extend()
# Adds each element of an iterable (like a list, tuple, string, etc.) to the end of the list

# Using extend() takes an iterable only such as - list, tuple, string
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])  # Adding a list
print(my_list)             # Output: [1, 2, 3, 4, 5, 6]

my_list.extend("abc")      # Adding a string
print(my_list)             # Output: [1, 2, 3, 4, 5, 6, 'a', 'b', 'c']


# append()
# Adds the given element to the end of the list as a single entity.
# Using append()
my_list = [1, 2, 3]
my_list.append(4)         # Adding an integer
print(my_list)            # Output: [1, 2, 3, 4]

my_list.append([5, 6])    # Adding a list
print(my_list)            # Output: [1, 2, 3, 4, [5, 6]]



#slicing

 #out of bound sclicing doesnt return error same as strin slicing work here too
 #we can use slicing fro insertions too:
numbers=[1,2,3,4,5,6]
numbers[0:2]=['x','y','z']
print(numbers)

#iteration
ip_list=['123.456.465','192.543.564','10.0.0.1']
for ip in ip_list:
    print(f'Connecting to {ip}.....')



# some gotchas
# 1.
l1=[1,2,3]
l2=l1
l2[0]='XX'
l2.append(10)
# both are same
print(l2)
print(l1)

print(id(l1))
print(id(l2))


# way to make a copy:
l3=l1.copy()
l3.append(10)
# both are not same anymore
print(l3)
print(l1)

print(id(l1))
print(id(l3))

# 2
nums=[1,2,3,4,5,6,7,0,1,2]

# wrong way:
for n in nums:
    if n < 5:
        nums.remove(n)
print(nums)
# reason:iterator that moves one entry at a time and modiying the list will not be updated
"""
Step-by-step execution explaination:

Start with nums = [1, 2, 3, 4, 5, 6, 7, 0, 1, 2].
n = 1: nums.remove(1) -> nums = [2, 3, 4, 5, 6, 7, 0, 1, 2].
The loop skips the next element (2), moving directly to 3.
The process repeats, skipping elements unintentionally.
Final Output: nums = [5, 6, 7, 1, 2] (not all numbers < 5 are removed).
"""

# right way:
new_list=list()
for n in nums:
    if n>=5:
        new_list.append(n)

# somthing called list comprehension;
 
my_list=[n for n in nums if n>=5]
print(my_list)