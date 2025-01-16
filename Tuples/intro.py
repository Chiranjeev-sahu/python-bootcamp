# Tuples are immutable and similar to list ,use when the data will not change 
# they are faster more efficient 
t1=tuple()
t2=()
t3=(1,3.4,'Python',True)
#FOR ONE ELEMENT    
t4=(10,)
t5=6.9,True,10,'abc'
t6 =tuple('hello')
t7=tuple([1,2,3,4])
#indexing and slicing
print(t5[-1])

# this will give error because of immutability
# t5[0]='x'

# one thing I learned is that tuples can be used as a key in the dictionaries and lists cannot

#storage efficiency
import sys

l1=[1,2,3,4,5,6]
l2=(1,2,3,4,5,6)

print(f'List memory :{sys.getsizeof(l1)}')
print(f'Tuple memory :{sys.getsizeof(l2)}')