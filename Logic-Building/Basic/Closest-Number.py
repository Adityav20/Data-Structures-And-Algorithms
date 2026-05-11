"""
Given two integers n and m (m != 0). Find the number closest to n and divisible by m. 
If there is more than one such number, then output the one having maximum absolute value.
"""

n = int(input("Enter a Number n: "))
m = int(input("Enter a Number m: "))
ans = 0

if m > 0:
    if n % m == 0:
        ans = n
    else:
        if abs(n - (n // m) * m) <= abs(n - ((n // m) + 1) * m):
            ans = (n // m) * m
        else:
            ans = ((n // m) + 1) * m
    
    print("Number closest to", n, "and divisible by", m, "is:", ans)