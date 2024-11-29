r=range(2,10,3) #10 exclusive
# help(range)
print(type(r))
print(r)
print(list(r))

print(list(range(0,11,2)))
s=sum(range(0,10))
print(s)

#Summary
#1. range(stop)
print(list(range(10))) #range(0,10,1)

#2.range(start,stop)
print(list(range(3,9)))#range(3,9,1)

#3.range(start,stop,step)
print(list(range(10,-2,-3)))
