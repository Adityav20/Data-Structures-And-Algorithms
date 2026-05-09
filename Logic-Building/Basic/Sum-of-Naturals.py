"""
Sum of the first n natural numbers.
"""
n = int(input("Enter a Number: "))
sum,i = 0,1
expression = ""

while i<=n:
    sum += i
    expression += str(i)
    
    if i != n:
        expression += " + "
    i+=1

print(expression, "=" ,sum)