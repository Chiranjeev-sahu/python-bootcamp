# a namespace is a container (table) that contains the names we define. This way we can have the same name defined in different namespaces

x = 10 #global
def my_func(): 
    x = 5 #local
    print(f'x inside the function: {x}') 
    
my_func() 
print(f'x outside the function: {x}')



#to accesss the global locally
x = 10 
def my_func(): 
    global x 
    x += 1 
    print(f'x inside the function: {x}') 
    
my_func() 
print(f'x outside the function: {x}')#both will return 11 as the global x will be altered

#unbound error case will arise because x must be created before using it:
# def func1(): 
#     print(x) 
#     x = 8

# prin(a)
# a=100

numbers = [1,2,3]
x=10
def my_func(numbers,x):
    numbers.append(5)
    x=66
    print(f'x inside the function: {x}')

my_func(numbers,x)
print('After calling the function,number is {numbers} and x is {x}')  