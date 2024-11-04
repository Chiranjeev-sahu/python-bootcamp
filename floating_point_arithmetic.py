#Floating point arithmethic  

print(0.125 == 1/10+2/100+5/100)

print(format(1/3,'.20f'))#approximating it to 20 decimal points

print(format(1/10,'.20f'))#approximating it to 20 decimal points
print(format(0.1,'.20f'))
print(format(0.125,'.40f'))#0.125 has an exact representation because it can be written as a fraction with a power of 2 in the denominator. hence can be represented well woth binary


#why its imp

a=0.1*3
b=0.3

print(a==b) #this should be True but is false as a is approximation of 0.3 and not 0.3 itself
print(format(a,'.25f'))

from math import isclose

x=0.00000001
y=0.00000002

print(x==y)#false
print(isclose(x,y,abs_tol=0.01))

x = 1000
y = 1005
print(isclose(x, y, rel_tol=0.01))  # True, as 0.5% difference is within 1%



a=3.4
b=2.3
print(a+b)# should be 5.7 but is not because
print(format(a,'.25f'))#of these
print(format(b,'.25f'))