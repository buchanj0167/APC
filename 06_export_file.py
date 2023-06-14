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