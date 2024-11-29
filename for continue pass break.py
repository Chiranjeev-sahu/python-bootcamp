# continue- used to just  Skip the rest of the code inside the loop for the current iteration and jumps to the next iteration.


for letter in 'Go python!':
    if letter=='o':
        continue
    print(letter,end='')


for n in range(10):
    if n%2==0:
        print(f'Found an even number: {n}')
        continue
    print(f'Found an odd number: {n}')


#pass- A placeholder that does nothing; it's used where syntactically a statement is required, but no action is desired.
for letter in 'Go python!':
    if letter == 'o':
        pass  # Does nothing when letter == 'o'
    print(letter, end='')
# O/P=Go python!








#break-braks out of loop,


for n in range(10):
    print(n)
    if n==5:
        break
# exit() #this stops the entire script
print('Outside the loop')


for letter in 'Python':
    if letter == 'o':
        print('Letter id o and now the loop will be broken out of')
        break
    print(letter)



for n in range(0,12):
    if n%13==0:
        print('There is a number divisible by 13 in the range')
        break
else: #belongs to for(not if) only be enacted after the for loop exhausted not with the break
    print('No num divisible by 13 ')