import prettytable

table = prettytable.PrettyTable()

table.field_names = [
    "City name", "Area(in Sq Km)", "Population(in millions)", "Annual Rainfall (in mm ) "]
table.add_row(["Delhi", "1483", 33.8, 774.4])
table.add_row(["Mumbai", "603.4", 21.7, 2000])
table.add_row(["Kolkata", "206.08", 15.6, 1836.5])

print(table)
