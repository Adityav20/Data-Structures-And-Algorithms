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

patterns = {
    9: pattern09,
    10: pattern10
}

# Execute selected pattern
patterns[p](n)