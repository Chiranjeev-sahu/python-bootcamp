import random
import string
# print(string.ascii_letters + string.digits + string.punctuation)
chars=string.ascii_letters + string.digits + string.punctuation

print(random.choice(chars))

length=int(input('Password length: '))
password=''

for _ in range(length):
    c=random.choice(chars)
    password+=c
print(f'Your random password is:{password}')
