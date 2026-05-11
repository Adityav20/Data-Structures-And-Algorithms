"""
Guess the number on the opposite face of the cube.
"""
n = int(input("Enter the number on the face of the cube: "))
if n in range(1,7):
    print("Opposite face number on the cude:", 7-n)
else:
    print("Number is not in on the face of the cube.")