"""
Sum of squares of first n natural numbers.
"""
n = int(input("Enter a Number: "))
sum = 0
expression = ""

for i in range(1,n+1):
    sum = sum + (i*i)
    expression += str(i) + "^" + "2"

    if i != n:
        expression += " + "

print(expression, "=", sum)