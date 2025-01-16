# Common methods: remove(), pop(), clear(), copy(), len(), in

s1={1,2,3}

s1.add('a')
s1.add(4.5)
s1.add(1)# this does nothin because of the repeatation

# element removal
#remove()
s1.remove(3)
print(s1)


#discard() =>removes if item is present and no error if item is absent unlike remove
s1.discard('a')
print(s1)
s1.discard('x')#=> NO ERROR

#pop() pops random element
x=s1.pop()
print(x,s1)

s2=set('abc')
s3=s2
s3.add('x')
print(s2)

# use copy to deal with this like this
# s2 = set('abc')  # s2 = {'a', 'b', 'c'}
# s3 = s2.copy()   # s3 is now an independent copy of s2
# s3.add('x')      # Only s3 is modified
# print(s2)  # Output: {'a', 'b', 'c'}
# print(s3)  # Output: {'a', 'b', 'c', 'x'}

# clear()
s3.clear()


