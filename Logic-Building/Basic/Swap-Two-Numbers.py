"""
Swap two numbers.
"""
n1 = int(input("Enter first Number x: "))
n2 = int(input("Enter second Number y: "))
"""temp = n1
n1 = n2
n2 = temp"""
n1 = n1 + n2
n2 = n1 - n2
n1 = n1 - n2
print("Now x =", n1, "and y =", n2)
