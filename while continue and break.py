# x=12
# while x<100:
#     x=x+1
#     if x%13 !=0:
#         continue
#     print(x)


# #break

# while True:

#     guess=int(input('Enter your kucky number[1-10]:'))
#     if guess == 7:
#         print('you won')
#         break
#     print(f'{guess} was not a lucky number!')



#to find all primes below given value

a=int(input('Enter the number'))
while a>1:
    b=a//2
    while b>1:
        if a%b==0:
            break
        b-=1
    else:
        print(f'{a} is a prime number')
    a-=1
