"""
Given a number n, find the sum of its digits.
"""
n = str(input("Enter a Number n: "))
sum = 0

for i in n:
    sum += int(i)

print("Sum of digits of", n, ":", sum)