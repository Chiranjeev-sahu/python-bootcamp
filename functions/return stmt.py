# can only be used in func and method

n=len([1,2,4,5])
print(n)

def add1(a,b):
    print(f'Sum:{a+b}')

def add2(a,b):
    s=a+b 
    return s

add1(10,20)

mysum=add2(30,34)
print(mysum)

# a func that doesnt return anything explicitly, returns None implicitly
def func():
    pass

x=func()
print(x)
print(add1(1,2))

# it should be at the very last as it exists the function

def add3(a,b):
    return a+b
    print('XXXXXX')#won't print

print(add3(2,3))

# it can return multiple things
def my_func(x):
    return x,x**2,x**3,x**4

print(my_func(3))#this returns a tuple

# tuple unpacking
a,b,c,d=my_func(10)
print(a,b,c,d)

#if the number of elements on return are not known then use:
x,*y=my_func(4)
print(x,y)
