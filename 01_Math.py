import math
# asks user what shape they would like
print("Welcome to the Area and Perimeter Calculator!")
print("Please choose a shape: ")
print("1. Triangle")
print("2. Square")
print("3. Rectangle")

choice = int(input("Enter your choice (1-3): "))
# asks user for values depending on shape they choose
if choice == 1:  # Triangle math
    base = float(input("Enter the base length: "))
    height = float(input("Enter the height: "))
    side_a = float(input("Enter the length of side a: "))
    side_b = float(input("Enter the length of side b: "))

    perimeter = side_a + side_b + base
    area = 0.5 * base * height

elif choice == 2:  # Square math
    side = float(input("Enter the side length: "))
    perimeter = 4 * side
    area = side ** 2

elif choice == 3:  # Rectangle math
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))

    perimeter = 2 * (length + width)
    area = length * width

# Print the results
print("Perimeter:", perimeter)
print("Area:", area)
