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


# main routine goes here
want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == "yes":
    print('''\n
    *** This is a code that works out the area and perimeter of a shape ***
    *** You will be asked what shape you would like ***
    *** then you will be asked what value the sides are ***
    *** then watch the magic happen ***\n''')

print("we are done")
