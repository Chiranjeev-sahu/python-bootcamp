# Consider the following string declaration which is part of the output of a Linux command.

my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'

# Write a Python script that extracts the MAC address (b4:6d:83:77:85:f3) from the string.'''

MAC=my_str[-17:]
print(MAC)

MAC2=my_str.split()[-1]
print(MAC2)

'''Display the following strings literally:

It displayed: "You've got an error!"
 means a new line.
\ is known as the escape character.'''

print(r"It displayed: \"You've got an error!\"")
print(r"\n means a new line.")
print(r"\ is known as the escape character.")


# Write a Python script that tests if a string is a palindrome.

a='pooop'
print(f"Is a palindrome? => {a==a[::-1]}")


# Change the solution of the previous challenge so that both the white spaces and the letter case are ignored when checking if the string is a palindrome.
a='Rats live on no evil star'
a=a.replace(' ','')
a=a.lower()
print(f"Is a palindrome? => {a==a[::-1]}")


# Write a Python script to get a string made of the first and the last 2 chars from a given string entered by the user.

# inpt=input("Enter something: ")

# print(inpt[:2]+inpt[-2:])

# Write a Python program to get a string from a given string where all occurrences of its first character have been changed to '$', except the first character itself.

a='mama'
first=a[0]
a=first+a[1:].replace(first,'$')
print(a)

# Write a Python script that removes the characters which have odd index values of a given string.
a='I will be somebody someday.'
print(a[::2])

# Write a Python script that prompts the user for the radius of a circle and calculates its area. Circle's area = pi * r ** 2 where pi = 3.1415
# Using an f-string display the area of the circle with 4 decimal places.

# radius=int(input('Enter the radius: '))
# print(f'area: {3.141*radius**2:.4f}')


# Write a Python script that displays a number with a comma (,) as the thousands separator (US and UK format) and with a period(.) as the thousands separator (EU format).

number=1234567
print(f'{number:,}')
# for 1.234.567
print((f'{number:,}').replace(',','.'))