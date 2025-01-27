# A destructor is a special function (_del_()) that is automatically called when the lifetime of an object ends. The purpose of the destructor is to free the resources that the object may have acquired during its lifetime.
#in python its not always necessary

class Robot:
    """This class impleemnts a robot"""
    def __init__(self,name,year):#dunder class which will be looked by python for every instance if implemented
        self.name=name
        self.year=year
    def setEnergy(self,energy):
        self.energy=energy
def __del__(self):
    print('Robot destroyed!')