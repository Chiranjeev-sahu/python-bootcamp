my_tuple=(1.4,10,'abc',True,(30,40),'x')
#concatenation
t1=my_tuple+tuple('yz')
print(t1)
#multiplication
t2=(1,3,4)*3
print(t2)
print(my_tuple[0:2])
print(my_tuple[3])
print(my_tuple[2:])
print(my_tuple[::])
print(my_tuple[::2])
print(my_tuple[-1:0:-1])


movies = ('The Wizard of ','The legend','Casablanca')

for movie in movies:
    print(f'We are watching: {movies}')

print('The legend' in movies)
print('The legend' not in movies)