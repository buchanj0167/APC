import pandas as pd


# Function to check which shape the user wishes to calculate
def shape_checker(question):
    while True:
        response = input(question).lower()

        if response in ["1", "t", "triangle"]:
            return "triangle"

        elif response in ["2", "s", "square"]:
            return "square"

        elif response in ["3", "r", "rectangle"]:
            return "rectangle"

        elif response in ["4", "c", "circle"]:
            return "circle"

        else:
            print("Please enter a valid integer or shape name!")


# Function to check if user inputs a valid response for yes/no questions
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter yes or no")


# Function to check if user inputs a valid response for number questions
def num_check(question, error, num_type):
    valid = False
    while not valid:
        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Create an empty DataFrame to store calculation history
calc_history = pd.DataFrame(columns=['Shape', 'Perimeter', 'Area'])


# Ask user if they want instructions
want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == "yes":
    print('''
    *** This is a code that works out the area and perimeter of a shape ***
    *** You will be asked what shape you would like ***
    *** then you will be asked what value the sides are ***
    *** then watch the magic happen ***\n''')

print("Now it's time for MATH!!!")

while True:
    print("Welcome to the Area and Perimeter Calculator!")
    print("Please choose a shape: ")
    print("1. Triangle")
    print("2. Square")
    print("3. Rectangle")
    print("4. Circle")

    choice = shape_checker("Enter your choice (1-4): ")

    # Variables for perimeter and area
    perimeter = 0
    area = 0

    # Calculate perimeter and area based on the user's choice
    if choice == "triangle":  # Triangle math
        base = num_check("Enter the base length: ", "Please enter a valid number: ", float)
        height = num_check("Enter the height: ", "Please enter a valid number: ", float)
        side_a = num_check("Enter the length of side a: ", "Please enter a valid number: ", float)
        side_b = num_check("Enter the length of side b: ", "Please enter a valid number: ", float)

        perimeter = side_a + side_b + base
        area = 0.5 * base * height

    elif choice == "square":  # Square math
        side = num_check("Enter the side length: ", "Please enter a valid number: ", float)

        perimeter = 4 * side
        area = side ** 2

    elif choice == "rectangle":  # Rectangle math
        length = num_check("Enter the length: ", "Please enter a valid number: ", float)
        width = num_check("Enter the width: ", "Please enter a valid number: ", float)

        perimeter = 2 * (length + width)
        area = length * width

    elif choice == "circle":  # Circle math
        radius = num_check("Enter the radius: ", "Please enter a valid number: ", float)

        perimeter = 2 * 3.14159 * radius
        area = 3.14159 * radius ** 2

    else:
        print("Invalid choice!")

    # Print the results
    print("Perimeter:", perimeter)
    print("Area:", area)

    perimeter_txt = f"=== Your Perimeter is: {perimeter}"
    area_txt = f"=== Your Area is: {area}"
    choice_txt = f"=== You chose shape: {choice}"

    to_write = [choice_txt, perimeter_txt, area_txt]

    file_name = f"{choice}.txt"
    text_file = open(file_name, "w+")

    for item in to_write:
        text_file.write(str(item))
        text_file.write("\n\n")

    text_file.close()
    for item in to_write:
        print(item)
        print()

    # Append the calculation results to the DataFrame
    calc_history = pd.concat(
        [calc_history, pd.DataFrame([[choice, perimeter, area]], columns=['Shape', 'Perimeter', 'Area'])])

    # Display the calculation history
    print("\nCalculation History:\n")
    print(calc_history)

    if yes_no("\nDo you wish to continue using the program: ") == "yes":
        continue

    else:
        print("\nThank you for using this program, MATH OUT!!!")
        quit()

