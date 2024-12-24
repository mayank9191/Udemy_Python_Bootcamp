# FileNotFoundError

try:
    file = open("Day_30/a_file.txt")
    a_dict = {"key": "value"}
    print(a_dict["key"])

except FileNotFoundError:
    file = open("Day_30/a_file.txt", "w")
    file.write("Something")

except KeyError as error_message:
    print(f"The key {error_message} does not exist")

else:
    content = file.read()
    print(content)

finally:
    raise FileExistsError("This file not exisit")
    file.close()
    print("File was closed.")
