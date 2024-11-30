# Create a Python script that asks the user for a number and then prints out a list of all the divisors of each number less than the asked number.
x = int(input("Enter a number: "))
all_divisors = list()
for i in range(2, x//2+1):
    if x % i == 0:
        all_divisors.append(i)

print(all_divisors)




# Write a Python program to check if an integer (x) is the power of another integer (y). Prompt the user to input both integers.

a=int(input('Enter first number'))
b=int(input(f'Enter second number to see if its power of {a}'))

for i in range(2,b):
    if a**i==b:
        print("yes it is")


#Write a Python program that counts and displays the vowels of a given string ignoring the letter case.

a=input("Say something: ")
vowels=[]
count=0
for i in a:
    
    if i in ['a','e','i','o','u']:
        if i not in vowels:
            vowels.append(i) 
        count+=1

print(f'vowels:{vowels} count:{count}')


# Challenge #6
# Given the string s1, write a program to return the sum and the average of the digits that appear in the string, ignoring all other characters.
my_str=input()
total, count = 0, 0
for char in my_str:
    if char.isdigit():
        total += int(char)
        count += 1

print(f'Sum: {total} Average: {total/count}')


# Challenge #8
# Write a Python script that displays the following pattern from 1 to n where n is entered by the user.
"""
1

22

333

4444

55555

666666
"""
n=int(input())
for i in range(1,n+1):
    print(str(i)*i)



# Challenge #10
# Write a Python program that iterates over the integers from 1 to 50. For multiples of three print "Foo" instead of the number and for multiples of five print "Bar". For numbers that are multiples of both three and five print "FooBar".

for i in range(1,50):
    if i%3==0 and i%5==0:
        print(f"{i}:FooBar")
    elif i%3==0:
        print(f'{i}:Foo')
    elif i%5==0:
        print(f'{i}:Bar')
    else:
        print(f'{i}:   ')
        

# Challenge #11
# Write a Python script that prints out the Fibonacci series up to a given number n.
n=int(input("Enter the fib number limit"))
a, b = 0, 1
while a <= n:
    print(a, ' ', end=' ')
    a, b = b, a + b

# Challenge #12
# Write a Python script that draws the following pattern using for loops.
"""
*

* *

* * *

* * * *

* * * * *

* * * *

* * *

* *

*
"""

n = 10
for i in range(n):
    for j in range(i):
        print ('* ', end='')
    print('')

for i in range(n, 0, -1):
    for j in range(i):
        print('* ', end='')
    print('')

    