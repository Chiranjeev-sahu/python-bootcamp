# The walrus operator (:=) in Python is also known as the assignment expression operator. It allows you to assign a value to a variable as part of an expression.

print(x:=2+3)#valid
# print(x=2+3)#invalid


while (value:=input('Enter something: ')) != '':
    print(f'You Entered: {value}')

#does the same thing as this:
# value=input('Enter something')
# while value != '':
#     print(f'Yov enterd: {value}')
#     value=input('Enter something')


# ex-2
# data=input('Enter your name: ')
# if len(data)>0:
#     print(f'Youre name has {len(data)} charaters.')
# else:
#     print('Your name cant be empty')


data=input('Enter your name: ')
if(n:= len(data))>0:
    print(f'Your name has {n} characers.')
else:
    print('Your name cannot be empty')