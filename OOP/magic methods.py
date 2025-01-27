#Magic methods (also known as dunder methods or special methods) are methods that have a double underscore (__) prefix and suffix. These methods allow you to define or customize the behavior of objects for built-in operations (like addition, string representation, comparison, etc.).


# a, b = 4, 5
# # a+b   
# a. add (b) #these two are same

# x, z = '4', '5'  
# x. add_(z)#these two are also same

class Robot: 
    """This class implements a Robot."""
    population = 0 # class attribute 
    def __init__(self, name, price):
        self.name = name 
        self.price=price 
        Robot.population += 1


    def __str__(self):
        my_str=f'My name is {self.name} and price is {self.price}.'
        return my_str
    
    def __add__(self,other):
        price=self.price+other.price
        return price
    
r1=Robot('Marvin', 150) 
r2=Robot('Gal', 45)
print(r1)
print(r1+r2)