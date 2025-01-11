# List comprehension in Python is a concise way to create lists.

# Syntax: [expression for item in iterable if condition]

# This:
# clicks=[10,5,15,20]
# doubles_list=list()
# for c in clicks:
#     doubles_list.append(c*2)

# can be done in one line as
clicks=[10,5,15,20]
doubles_list=[x*2 for x in clicks]


friends=['Andrei','diana','paul','Marry']
reversed_name=[item[::-1] for item in friends]
print(reversed_name)

#with if condition

nums=[1,7,8,14,21,23,50]
div_by_seven=[n for n in nums if n %7==0]
print(div_by_seven)


#list with common strings

friends=['john','dan','marry']
neighbours=['tim','steve','dan','john']
friends_and_neighbours=[name for name in friends if name in neighbours]
print(friends_and_neighbours)