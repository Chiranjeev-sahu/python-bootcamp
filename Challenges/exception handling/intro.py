#exceptions are errors that occur during the execution of a program, disrupting the normal flow of instructions. Exceptions are raised when something goes wrong, like trying to divide by zero or accessing a variable that doesn't exist.
#handling them
try:
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    d = 7
    c = a / b + d
except ZeroDivisionError as e:
    print(f'Division by zero is not permitted: {e.args}')
except TypeError as e:
    print(f'Operations of different types are not permitted: {e}')
except Exception as e:
    print(f'A generic exception has occurred: {e}')
else:
    print('No errors.')
    print(f'c = {c}')
finally:
    print('Goodbye!')



#raisinbg an exception
age=-1
if age<0:
    raise Exception("Age cant be less than zero")