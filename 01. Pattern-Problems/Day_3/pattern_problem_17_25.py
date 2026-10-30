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


patterns = {
    17: pattern17
}

patterns[p](n)