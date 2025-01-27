# class Robot:
#     species = "Android"  # class attribute
    
#     def __init__(self, name, year):
#         self.name = name  # instance attribute
#         self.year = year  # instance attribute
class Robot:
    """This class impleemnts a robot"""
    population = 0 #class attr
    def __init(self, name, year): 
        self.name = name 
        self.year=year 
        Robot.population+1#accessing class attr


    def setEnergy(self,energy):
        self.energy=energy

        
print(f'Robots alive: {Robot.population}')
r1=Robot('R1',2023)
r1.setEnergy(500)
print(r1.energy)
print(getattr(r1,'energy'))#way to get the value of an attribute that doesn't exist
print(r1.__dict__)


# print(r1.brand) => this will give exception

print(getattr(r1,'brand','N/A'))#pass a default value to not get exception




