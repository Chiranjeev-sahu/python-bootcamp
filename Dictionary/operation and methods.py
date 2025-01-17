person={'name':'john','age':30,'location':'USA'}
#assignment
friends = person


neighbour= person.copy()
person['location']='Europe'#added only to person
print(neighbour,person)
# .update() method for dictionaries is used to update a dictionary with elements from another dictionary or from an iterable of key-value pairs. 
countries = {'ro': 'Romania', 'us': 'United States of America', 'de': 'Germany'} 
countries.update({'hu': 'Hungary', 'fr': 'France'})
print(countries)
#ex-2
dict1 = {'a': 1, 'b': 2}
dict1.update(b=3, c=4)

# #clear
# person.clear()
# print(person,friends)

#dict.keys => used for the key retrieval
k=person.keys
print(k)
print(type(k))

#dict.value()
print(person.values())
print(list(person.values()))

#dict.items() => key value pairs in tuple form
print(person.items())

print('name' in person)
print(10 in person.keys()) 
print('Berlin' in person.values())
print('USA' in person.values()) 
print(('age', 30) in person.items())

d1={10:'a',20:'b',30:'c'}
v= d1.values()
print(v)
d1[10]='X'
print(v)# X will be present here because the methods are dynamic i.e they show 

d1={10:'a',20:'b'}
d2={10:'c',30:'b'}
k1=d1.keys()
k2=d2.keys()

print(k1,k2)

print(k1 & k2)
print(k1 | k2)


for k in person.keys:
    print(f'key is {k}')

for v in person.values():
    print(f'values us {v}')

for k in person.keys:
    print(f'Key is {k} and value us {person[k]}')

for k,v in person.items:
    print(f'Key is {k} and value is {v}')