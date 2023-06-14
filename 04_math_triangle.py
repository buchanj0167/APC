import math
# Triangle math
base = float(input("Enter the base length: "))
height = float(input("Enter the height: "))
side_a = float(input("Enter the length of side a: "))
side_b = float(input("Enter the length of side b: "))

perimeter = side_a + side_b + base
area = 0.5 * base * height

# Print the results
print("Perimeter:", perimeter)
print("Area:", area)