firstname='John'
lastname='Smith'
age=40
# this gives error becauseint cant be ocncatenated to str we have to change to str
# print('Hello' +firstname+lastname+'!you are'+age+'years old')

print('Hello ' +firstname+lastname+'! You are '+str(age)+' years old!')
# this is tedious and looks horrendous

# String formatting helps us deal with this issue makes code more readable and concise
print(f'Hello {firstname}{lastname}! You are {age} years old!')
# F-strings automatically convert any values inside the curly braces {} into a string representation. By default, this includes evaluating expressions and converting the result to a string.

s = f'{2.3 * 4.2 / 5.1}'
print(type(s))

# further formatting
# General Syntax: f"{expression:format_specifier}"
s = f'{2.3 * 4.2 / 5.1}'
s = f'{2.3 * 4.2 / 5.1:4f}'#here f at last specifies that the format is float
print(s)

# Number Padding:
f"{5:03d}"  # Pad with leading zeros to make the number three digits
# Output: '005'

# Thousands Separator:

large_number = 1000000
f"{large_number:,}"  # Thousands separator
# Output: '1,000,000'

# Percentage:
value = 0.456
f"{value:.2%}"  # Convert to percentage
# Output: '45.60%'

# Conditional Expressions:
# You can embed conditional expressions directly inside f-strings.

age = 20
f"You are {'an adult' if age >= 18 else 'a minor'}."


# Multiple Format Specifiers for Different Types:
# You can use different types for formatting in a single f-string expression.
num = 255
s = f'{num:x} {num:b} {num:o}'  # Hexadecimal, binary, and octal
print(s)  # Output: 'ff 11111111 377'


# Using Percentage Formatting with Precision:
# You can also apply percentage formatting along with precision.
value = 0.12345
s = f'{value:.2%}'  # Convert to percentage with 2 decimal places
print(s)  # Output: '12.35%'

# farhenheit = celcius*1.8+32

celsius=15.4
print(f'{celsius}degrees Celsius = {celsius*1.8+32} Fahrenheit')





# F-Strings with = for debugging
# just for readibility as it prints variable name 
# It is easier to track where the value of variables is coming from, especially when dealing with many variables in a function or during a complex process.
name,age='Alice',30
print(f'your name is {name} and you are {age} years old.')
print(f'your name is {name=} and you are {age=} years old.')
r=13.3
PI=3.141592

print(f'Circle area with a radius of {r} is {PI * r**2:.2f}')
print(f'Circle area with a radius of {r=} is {PI * r**2=:.2f}')