programming_dictionary = {
    "Bug": "An error in a program that prevents the program  from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}


print(programming_dictionary["Bug"])

programming_dictionary["Loop"] = "The action of doing something over and over again."


empty_dictionary = {}

# Wipe an existing dictionary

# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary

programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)


# Loop through a Dictionary for keys
for key in programming_dictionary:  # or by programming_dictionary.keys()
    print(key)
    print(programming_dictionary[key])  # to print value of that key


# Loop through a Dictionary for values
for value in programming_dictionary.values():
    print(value)

# Loop through a Dictionary for keys and values
for key, value in programming_dictionary.items():
    print(key, value)
