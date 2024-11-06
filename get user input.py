name=input()
print('Your name is ',name)

name=input("enter something-")
print('Your name is ',name)

#takes string as default

print(type(name))

#two ways to deal with this i.e. converting data types
price=input('Enter the price:')
quantity=input('Enter quantity:')
total_value=float(price)*float(quantity)
print(type(total_value))


price=int(input('Enter the price:'))
quantity=int(input('Enter quantity:'))
total_value=price*quantity
print(type(total_value))
