# Docstrings are a way to document Python functions, classes, modules, and methods. They are written as a string literal that appears immediately after the definition of a function, class, or method. Docstrings are used to describe what the code does, its parameters, return values, and any other relevant information.

def say_hello(name):
    """This function says hello to you!"""
    print(f'Hello {name}!:')

say_hello('Chir')

help(say_hello)
print(say_hello.__doc__)




# multiline docstring
def say_hello2(name):
    """This function says hello to you!
    The parameter will be concatenated to string Hello.
    The function does not return explicitly.
    """
    print(f'Hello {name}!:')

say_hello2('Chir')

