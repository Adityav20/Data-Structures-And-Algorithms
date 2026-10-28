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


patterns = {
    1: pattern01,
    2: pattern02,
    3: pattern03
}

# Execute selected pattern
patterns[p](n)