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
        ans = n - (n % m)
        if abs(ans + m - n) <= abs(ans - n):
            ans += m

    """for i in range(n-m,n+m+1):
        if i%m == 0: 
            ans = i
            break"""
    
    print(ans)