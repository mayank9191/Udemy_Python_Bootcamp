# import prettytable

# table = prettytable.PrettyTable()

from prettytable import PrettyTable

table = PrettyTable()
# print(table)

# Way 1
# table.field_names = ["Pokemon Name", "Type"]
# table.add_row(["Pikachu", "Electric"])
# table.add_row(["Squirtle", "Water"])
# table.add_row(["Charmander", "Fire"])

# print(table)

# Way 2

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"
print(table)
