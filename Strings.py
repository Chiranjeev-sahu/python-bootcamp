print('Hi there! I\'m Andrei')#\ is called an escape character used to signal that the character immediately following it should be treated differently from how it would normally be interpreted
# \n for a new line
# \t for a tab
# \\ to include a backslash itself


message='yo'
print(type(message))

print('\\ is special character in python.')

# Concatenation
# has ro be str 
language='Python'
version=3.11
print(language +str(version))

#  *=> used for repetiion
print('#'*50)

price='10.5'
print(price * 5) #this will write 10.5 five times
print(float(price)*5)


#slicing
# string_variable[start:stop:step]
movie='The Godfather'
print(movie[0:12])#last index excluded
print(movie[0:2])
print(movie[:2])
print(movie[4:])
print(movie[-2:])

print(movie[:4]+movie[4:])

print(movie[:42])# Doesn’t raise an error for out-of-range indices and stops at the end of the sequence.

print(movie[0:10:2])
print(movie[::])
print(movie[::-1])#used for printing chars in reverse aslo if we take like -3 or soemthing it will print them in reverse for var steps of 3

# you can also do this
print('Python 3!!!'[:7:2])

# also this
s='hello'
s[::-1][::-1] == s
# basically its used for both string literal and string varaible