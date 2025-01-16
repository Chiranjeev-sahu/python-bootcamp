#index and count
help(tuple.index)
t1=(1,2,3,4,5,1)

#1.tuple.index()=> only the first position of the occurance of the element
i=t1.index(2)
print(f'2 is at position {i}') 
# i=t1.index('x') #error

x=10
if x in t1:
    i=t1.index(x)
    print(f'x is at index {i}')
else:
    print(f'{x} is not in tuple')

# tuple.count()
n=t1.count(100)



# len(),sum(),max(),min(),sorted() can also be used but append(), remove(), or sort()

print(len(t1))
print(sum(t1))
print(max(t1))
print(min(t1))

t2=sorted(t1,reverse=True)
print(t2)