from prettytable import PrettyTable
table=PrettyTable()
table.field_names=["Pokemon Name","Type"]
table.add_rows([
    ["Pikachu","Electic"],
    ["Squirtle","Water"],
    ["Charmander","Fire"]])
print(table)
