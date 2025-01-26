# syntax: lambda parameter_list: expression
#A lambda expression in Python is a concise way to create small, anonymous (unnamed) functions.


def add(a, b, c): 
    result = a + b + c
    return result 


result=(lambda a, b, c: a + b + c)(3,4,5)#way to give args as 3,4,5
print(result)

square=lambda x:x**2
print(square(4))


#all types of args in lambda:
# Lambda combining all argument types
# combined_lambda = lambda x, y=10, *args, **kwargs: x + y + sum(args) + sum(kwargs.values())

# # x=1, y=default(10), args=(2, 3), kwargs={'a': 4, 'b': 5}
# print(combined_lambda(1, 2, 3, a=4, b=5))  # Output: 25




#when to use lambda:
# friends = [('Diana', 30), ('Ana', 25), ('Tudor', 22)]
# friends.sort()
# print(friends)#=> this sorts based on the key and we wanna sort based on the val than

friends = [('Diana', 30), ('Ana', 25), ('Tudor', 22)]
friends.sort(key=lambda x:x[1])
print(friends)#=> this sorts based on the key and we wanna sort based on the val than

#or we wanna sort by the length of their names:
friends = [('Diana', 30), ('Ana', 25), ('Tudor', 22)]
friends.sort(key=lambda x:len(x[0]))
print(friends)#=> this sorts based on the key and we wanna sort based on the val than
