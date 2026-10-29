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


patterns = {
    9: pattern09
}

# Execute selected pattern
patterns[p](n)