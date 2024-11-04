#Immutable types:int ,float,str,tuple,frozenset
#mutable types:lsits,sets,dict
a=2
print(a)
print(id(a))
a+=3
print(a)
print(id(a))
#new memory address id used for a 


# now for mutable

number=[1,2,4]
print(number)
print(id(number))
number.append(3)
print(number)
print(id(number))
# same memory will be used