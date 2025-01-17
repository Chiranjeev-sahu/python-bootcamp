# similar to list but with curly braces
# for the sets
names={'tom','Ann','john','dan'}
names={n.capitalize for n in names}
print(names)



# for the dictionary
d1={'a':1,'b':2,'c':3}
d2={k*2:v*2 for k,v in d1.items()}
print(d2)
d3={k.upper():v*2 for k,v in d1.items() if v%3==0}
print(d3)


# The zip() function in Python is a built-in function that is used to combine two or more iterables (like lists, tuples, or strings) into a single iterable of tuples. Each tuple contains elements from the input iterables that are at the same position.
years=[2017,2018,2019]
revenues=[30000,40000,50000]
z=zip(years,revenues)
sales=list(z)
print(sales)

my_sales=dict(zip(years,revenues))
print(my_sales)


profit={k:v*0.15 for k,v in my_sales.items()}
print(profit)