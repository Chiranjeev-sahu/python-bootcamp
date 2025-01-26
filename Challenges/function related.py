# Challenge #1
# Write a Python function that takes a list as an argument and returns a new list with unique elements of the first list in the same order.


def unique(lst):
    result=list(set(lst))
    result.sort()
    return result
print(unique([1, 2, 3, 3, 3, 3, 4, 5, 1, 3, 5, 5, 5]))


#Write a Python function to check whether a number is perfect or not. The function should return True if the number is perfect and False otherwise.
import math
def isperfect(n):
    listofdivs=[]
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            listofdivs.append(i)
            if i != 1 and i != n // i:  
                listofdivs.append(n // i)
        
    return sum(listofdivs)==n


print(isperfect(6))

# Challenge #3: Factorial Function

def factorial(n):
    if n == 0 or n == 1:  
        return 1
    return n * factorial(n - 1)  

print(factorial(5))  


#Challenge #4: Check Prime Number
def is_prime(n):
    if n < 2:  
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(29))

# Challenge #5: Find 5 Prime Numbers Greater than 1,000,000

def find_primes_above(limit, count):
    primes = []
    num = limit + 1
    while len(primes) < count:
        if is_prime(num):  # Using the `is_prime` function from Challenge #4
            primes.append(num)
        num += 1
    return primes

# Challenge #7: Equilibrium Index

def equilibrium_index(lst):
    total_sum = sum(lst)
    left_sum = 0
    
    for i, num in enumerate(lst):
        total_sum -= num  # Now total_sum is the right sum
        if left_sum == total_sum:
            return i
        left_sum += num
    
    return False