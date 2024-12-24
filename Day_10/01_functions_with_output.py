def format_name(first_name, last_name):
    """Take a first and last name and format it to return the title case version of the name."""  # Docstring: way to describe a function in words for proper documentation

    if (first_name == "" or last_name == ""):
        return "You did not provide valid inputs"
    return (first_name+" "+last_name).title()


first_name = input("Enter your First name: ")
last_name = input("Enter your Last name: ")

name = format_name(first_name, last_name)

print(name)
