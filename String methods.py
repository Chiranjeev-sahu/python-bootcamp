# len(),type(),sum(),min(),round()

# ways to look for them:
# print(dir(str))

# help(str.replace)#used help to look about 'reaplce' method

s='Python'
print(s.upper())
print(s)#will be unchanged because immutabiiility but we can store in another varaible
new_s=s.upper()
print(new_s)

# same for .lower(), also we can use it in string literal btw
print('progRaMMinG'.lower())



my_str='I learn Python Programming'

# 1. str.upper()
print(my_str.upper())

#2. str.lower()
print(my_str.lower())

#3. str.strip()

ip='    123.456.78.9    '
ip=ip.strip()
print(ip)

value='$$200$$$$'
print(value.strip('$'))

# 4. str.replace()

new_value=value.replace('$','#')
print(new_value)

# help(str.replace)


#5.str.count()
txt='I learn Python,Python is cool as fak yo!'
n=txt.count('Python')
print(n)

# its case sensiteive so if we do this , this will return 0
txt='I learn PyThon,python is cool as fak yo!'
n=txt.count('Python')
print(n)
# we can do this to solve it
n = txt.lower().count('python') 
print(n)


# 6. str.split()-->splits string to list

my_list=txt.split()
print(my_list)

# can give separator
print('10.1.2.3'.split('.'))


#7. separator.join(iterable)
# iterable-An iterable is any Python object that can return its elements one at a time, making it possible to loop over it. In simpler terms, an iterable is an object that you can “iterate” through, or go through one item at a time, such as using a for loop.
ip='10.1.2.3'
ip_list=ip.split('.')
print(ip_list)

ip_str='.'.join(ip_list)
print(ip_str)

# 8. str.find()  -> find the firt occurance of a specific substring in a string
txt='I learn PyThon,python is cool as fak yo!'
print(my_str.find('Python'))


# check if its present w/o knowing position
print('Python' in my_str)

# check if its not present w/o knowing position
print('Python' not in my_str)
