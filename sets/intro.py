# A set is an unordered collection of unique elements.
# # Sets are mutable (you can add or remove items), but the elements themselves must be immutable (e.g., numbers, strings, tuples).

s1={1,2,3,'a','b',4}
print(s1)

print(s1[0]) #gives error

s1={1,2,3,'a','b',4,1,2,'a',3,10}
print(s1)

s1.add((10,20))
print(s1)

s1.remove('a')
print(s1)


# declaration
s2=set()
s3={}# this is dictionary


#str=>set
s4= set('hellloooooo!!!!')
print(s4)


#tuple=>set
s5=set((1,2,3,4,4,4,'abc'))
print(s5)


#list =>set
l2=[10,20,30,40]
print(set(l2))
