#A desired pattern number from USER
p = int(input("Enter a pattern number from 1 to 2: "))
n = int(input("Enter number of rows: "))

# Problem 1: Function to print a solid square pattern of asterisks
# Example for num = 4:
# ****
# ****
# ****
# ****
def pattern01(n):
    for i in range(n):
        for j in range(n):
            print('*', end = '')
        print()


# Problem 2: Function to print a right-angled triangle
# Example for num = 5:
# *
# **
# ***
# ****
# *****
def pattern02(n):
    for i in range(n+1):
        for j in range(i):
            print('*', end = '')
        print()


# Problem 3: Function to print an inverted right-angled triangle
# Example for num = 5:
# *****
# ****
# ***
# **
# *
def pattern03(n):
    for i in range(n):
        for j in range(n-i,0,-1):
            print('*', end = '')
        print()


# Problem 4: Function to print an increasing number triangle
# Example for num = 5:
# 1
# 12
# 123
# 1234
# 12345
def pattern04(n):
    for i in range(n+1):
        for j in range(1,i+1):
            print(j, end = '')
        print()


# Problem 5: Function to print a repeated number triangle
# Example for num = 5:
# 1
# 22
# 333
# 4444
# 55555
def pattern05(n):
    for i in range(1,n+1):
        for j in range(i):
            print(i, end = '')
        print()



patterns = {
    1: pattern01,
    2: pattern02,
    3: pattern03,
    4: pattern04,
    5: pattern05
}

# Execute selected pattern
patterns[p](n)