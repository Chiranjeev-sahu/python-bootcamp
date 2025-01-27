#class must be pascal case

class Robot:
    """This class impleemnts a robot"""
    def __init__(self,name,year):#dunder class which will be looked by python for every instance if implemented
        self.name=name
        self.year=year
        
        


r1=Robot('R1',2023)
print(r1.__doc__)
print(f'Robot name: {r1.name}')
print(r1.__dict__)

 