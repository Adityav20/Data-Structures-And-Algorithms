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

patterns = {
    1: pattern01
}

# Execute selected pattern
patterns[p](n)