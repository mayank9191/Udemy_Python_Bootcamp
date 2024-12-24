number = [1, 2, 3]
new_number = [item + 1 for item in number]
print(new_number)

name = "mayank"
new_list = [i for i in name]
print(new_list)

new_list = [2 * i for i in range(1, 5)]
print(new_list)

names = ["Alex", "Beth", "Carolina", "Dave", "Eleanor", "Freddie"]

short_names = [i for i in names if len(i) < 5]
print(short_names)

long_names = [i.title() for i in names if len(i) >= 5]
print(long_names)
