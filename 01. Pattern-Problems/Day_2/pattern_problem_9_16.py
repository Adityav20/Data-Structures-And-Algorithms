#A desired pattern number from USER
p = int(input("Enter a pattern number from 1 to 8: "))
n = int(input("Enter number of rows: "))


# Problem 9: Function to print an inverted pyramid pattern
# Example for num = 5:
# *********
#  *******
#   *****
#    ***
#     *
def pattern09(n):
    k = n
    for i in range(n,0,-1):
        print(' ' * (k-i), end = '')
        print('*'* (i-1), end = '')
        for j in range(i):
            print('*', end = '')
        print()


# Problem 10: Function to print a diamond pattern
# Example for num = 5:
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
def pattern10(n):
    k = n
    for i in range(1, n+1):
        print(' ' * (i+k-2), end = '')
        print('*' * (i-1), end = '')
        for j in range(i):
            print('*', end = '')
        print()
        k-=2
    pattern09(n)


# Problem 11: Function to print a sequential number triangle
# Example for num = 5:
# 1
# 23
# 456
# 78910
# 1112131415
def pattern11(n):
    k = 1
    for i in range(1, n+1):
        for j in range(1,i+1):
            print(k, end = '')
            k+=1
        print()


# Problem 12: Function to print an inverted number triangle
# Example for num = 5:
# 12345
# 1234
# 123
# 12
# 1
def pattern12(n):
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(j, end = '')
        print()


# Problem 13: Function to print a binary triangle
# Example for num = 5:
# 1
# 01
# 101
# 0101
# 10101
def pattern13(n):
    for i in range(1, n+1):
        for j in range(1,i+1):
            print((i+j+1) % 2, end = '')
        print()


patterns = {
    9: pattern09,
    10: pattern10,
    11: pattern11,
    12: pattern12,
    13: pattern13
}

# Execute selected pattern
patterns[p](n)