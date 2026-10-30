#A desired pattern number from USER
p = int(input("Enter a pattern number from 17 to 24: "))
n = int(input("Enter number of rows: "))


# Problem 17: Function to print a hollow right-angled triangle
# Example for num = 5:
# *
# **
# * *
# *  *
# *****
def pattern17(n):
    for i in range(n):
        for j in range(i+1):
            if i==n-1 or i<2 or i==n-1 or j==0 or j==i:
                print('*', end = '')
            else:
                print(' ', end = '')
        print()


# Problem 18: Function to print a hollow pyramid
# Example for num = 5:
#     *
#    * *
#   *   *
#  *     *
# *********
def pattern18(n):
    for i in range(1, n + 1):
        # Leading spaces
        print(' ' * (n - i), end='')
        # Print stars and inner spaces
        for j in range(2 * i - 1):
            if i==n or j==0 or j==2*i-2:
                print('*', end='')
            else:
                print(' ', end='')
        print()


# Problem 19: Function to print a hollow diamond
# Example for num = 5:
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *
def pattern19(n):
    for i in range(1, n):
        # Leading spaces
        print(' ' * (n - i), end='')
        # Print stars and inner spaces
        for j in range(2 * i - 1):
            if j==0 or j==2*i-2:
                print('*', end='')
            else:
                print(' ', end='')
        print()
    
    for i in range(n, 0, -1):
        # Leading spaces
        print(' ' * (n - i), end='')
        # Print stars and inner spaces
        for j in range(2 * i - 1):
            if j==0 or j==2*i-2:
                print('*', end='')
            else:
                print(' ', end='')
        print()


# Problem 20: Function to print an X pattern
# Example for num = 5:
# *   *
#  * *
#   *
#  * *
# *   *
def pattern20(n):
    for i in range(n):
        for j in range(n):
            if j==i or j==(n-i-1):
                print('*', end = '')
            else:
                print(' ', end = '')
        print()


# Problem 21: Function to print a butterfly pattern
# Example for num = 5:
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *
def pattern21(n):
    for i in range(1, n+1):
        print('*' * i, end = '')
        print(' ' * (2*(n-i)), end = '')
        print('*' * i)

    for i in range(n-1, 0, -1):
        print('*' * i, end = '')
        print(' ' * (2*(n-i)), end = '')
        print('*' * i)


# Problem 22: Function to print an hourglass pattern
# Example for num = 5:
# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********
def pattern22(n):
    k = n
    for i in range(n,0,-1):
        print(' ' * (k-i), end = '')
        print('*'* (i-1), end = '')
        for j in range(i):
            print('*', end = '')
        print()

    k = n
    for i in range(2,n+1):
        print(' ' * (k-i), end = '')
        print('*'* (i-1), end = '')
        for j in range(i):
            print('*', end = '')
        print()    


# Problem 23: Function to print Pascal's triangle
# Example for num = 5:
#         1
#       1   1
#     1   2   1
#   1   3   3   1
# 1   4   6   4   1
def pattern23(n):
    for i in range(n):
        # Leading spaces
        print(' ' * (2 * (n - i - 1)), end='')

        num = 1

        for j in range(i + 1):
            print(num, end='   ' if j < i else '')
            num = num * (i - j) // (j + 1) #Pascal formula

        print()


# Problem 25: Function to print a spiral number pattern
# Example for num = 5:
#  1  2  3  4  5
# 16 17 18 19  6
# 15 24 25 20  7
# 14 23 22 21  8
# 13 12 11 10  9
def pattern24(n):
    matrix = [[0] * n for _ in range(n)]

    top = 0
    bottom = n - 1
    left = 0
    right = n - 1

    num = 1

    while top <= bottom and left <= right:

        # 1. Left to Right
        for j in range(left, right + 1):
            matrix[top][j] = num
            num += 1

        top += 1

        # 2. Top to Bottom
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1

        right -= 1

        # 3. Right to Left
        if top <= bottom:
            for j in range(right, left - 1, -1):
                matrix[bottom][j] = num
                num += 1

            bottom -= 1

        # 4. Bottom to Top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1

            left += 1

    # Print matrix
    width = len(str(n * n))

    for row in matrix:
        for value in row:
            print(f"{value:{width}d}", end=" ")
        print()


patterns = {
    17: pattern17,
    18: pattern18,
    19: pattern19,
    20: pattern20,
    21: pattern21,
    22: pattern22,
    23: pattern23,
    24: pattern24
}

patterns[p](n)