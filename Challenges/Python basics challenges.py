# Challenge #1

# Consider the following Python expression: a = 16 / 2 + 6 / 2 ** 2

# Add parenthesis to change the order of operations so that a is 1.0
a = (16 / (2 + 6) / 2) ** 2
print(a)


# Challenge #2

# An IPv6 address is represented using 128 bits.

# Write a Python script that calculates how many IPv6 addresses are available. You can also include reserved IP addresses.

no_of_ways=2**128
print(no_of_ways)
  



# Challenge #3

# A company's revenue is 45,897,513.

# Calculate the company's profit if the profit represents 12.7% of the revenue.

# Display the profit using 2 decimal places.

  
revenue=45_897_513
profit=revenue*12.7/100
print(format(profit,'.3f'))


# Challenge #5

# A junior Python programmer writes the following code snippet and gets surprised that the comparison operator returns False instead of True.

# a = 0.1
# b = 0.3
# print(a * 3 == b) # => False
# Your job is to modify the code so that the comparison returns True which is correct.
from decimal import Decimal

a = Decimal('0.1')
b = Decimal('0.3')
print(a * 3 == b)  # => True