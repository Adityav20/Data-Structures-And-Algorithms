#A desired pattern number from USER
p = int(input("Enter a pattern number from 17 to 25: "))
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


patterns = {
    17: pattern17,
    18: pattern18,
    19: pattern19,
    20: pattern20
}

patterns[p](n)