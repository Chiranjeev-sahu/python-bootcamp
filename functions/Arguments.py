# # 1. Positional Arguments: Arguments passed in the correct order as defined in the function.
# def add(a, b):
#     return a + b

# print("Positional Arguments Example:", add(3, 5))  # Output: 8

# # 2. Keyword Arguments: Arguments passed with the parameter name, so order doesn’t matter.
# def greet(name, age):
#     return f"Hello, {name}! You are {age} years old."

# print("Keyword Arguments Example:", greet(age=25, name="Alice"))  # Output: Hello, Alice! You are 25 years old.

# # 3. Default Arguments: Arguments with predefined values if no value is provided.
# def greet_default(name, message="Hello"):
#     return f"{message}, {name}!"

# print("Default Arguments Example 1:", greet_default("Alice"))  # Output: Hello, Alice!
# print("Default Arguments Example 2:", greet_default("Bob", "Hi"))  # Output: Hi, Bob!

# # 4. Variable-Length Positional Arguments (*args): Allows passing a variable number of positional arguments.
# def add_numbers(*args):
#     return sum(args)

# print("Variable-Length Positional Args Example:", add_numbers(1, 2, 3, 4))  # Output: 10

# # 5. Variable-Length Keyword Arguments (**kwargs): Allows passing a variable number of keyword arguments.
# def display_info(**kwargs):
#     return ", ".join([f"{key}: {value}" for key, value in kwargs.items()])

# print("Variable-Length Keyword Args Example:", display_info(name="Alice", age=25, city="New York"))
# # Output: name: Alice, age: 25, city: New York
# Positional Arguments: add(3, 5) passes 3 to a and 5 to b.

# Keyword Arguments: greet(age=25, name="Alice") specifies the arguments by name, so order doesn’t matter.

# Default Arguments: greet_default("Alice") uses the default message="Hello", while greet_default("Bob", "Hi") overrides it.

# Variable-Length Positional Arguments (*args): add_numbers(1, 2, 3, 4) accepts any number of arguments and sums them.

# Variable-Length Keyword Arguments (**kwargs): display_info(name="Alice", age=25, city="New York") collects keyword arguments into a dictionary.

#---POSITIONAL ARGUMENTS
def difference(a,b):
    result = a-b
    print(result)

difference(1,5)#the arguments should be same number as in th function definition


#parameter vs argument
# Parameters are the placeholders in the function definition.
# Arguments are the actual values passed to the function when it’s called.


def func1(x,y):#parameters
    print(f'1st parameter x is {x}')
    print(f'2nd parameter y is {y}')
func1('python',55)#arguments


#--Keyword Arguments
def func1(x, y, z): 
    print(f'1st parameter x is {x}') 
    print(f'2nd parameter y is {y}') 
    print(f'3rd parameter z is {z}') 
    
func1(y=7, x=3, z=9) 
func1(10, 20, 30 )
func1(6, z=1, y=9)
# func1(x=8,3,4) =>error,because other two can be taken by anyone




#--Default args
def add(x,y=10,z=10):#rule is that if there is a default args than these must be followed by the other default args only or else the eror will rise
    print(f'x is {x} , y is {y} and z is {z}')
    print(f'{x} + {y} = {x+y+z}')

add(2,3)
add(6)
add(4,7,8)
add(x=1,z=7)