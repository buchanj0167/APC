import math


# want instructions go here
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter yes or no")


want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == "yes":
    print('''\n
    *** This is a code that works out the area and perimeter of a shape ***
    *** You will be asked what shape you would like ***
    *** then you will be asked what value the sides are ***
    *** then watch the magic happen ***\n''')

print("Now its time for MATH!!!")
# main routine goes here
# asks user what shape the would like
print("Welcome to the Area and Perimeter Calculator!")
print("Please choose a shape: ")
print("1. Triangle")
print("2. Square")
print("3. Rectangle")

choice = int(input("Enter your choice (1-3): "))
# asks user what values they would like depending on what shape
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
# if user inputs invalid choice
else:
    print("Invalid choice!")

# Print the results
print("Perimeter:", perimeter)
print("Area:", area)

perimeter_txt = f"=== Your Perimeter is: {perimeter}"
area_txt = f"=== Your Area is: {area}"
choice_txt = f"=== You chose shape number: {choice}"


to_write = [choice_txt, perimeter_txt, area_txt]


# Write to file...
# create file to hold data (add .txt extension)
file_name = f"{choice}.txt"
text_file = open(file_name, "w+")

# heading
for item in to_write:
    text_file.write(str(item))
    text_file.write("\n\n")

# close file
text_file.close()

# Print Stuff
for item in to_write:
    print(item)
    print()