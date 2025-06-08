with open("file1.txt") as file1:
    file1_data = (file1.readlines())

with open("file2.txt") as file2:
    file2_data = (file2.readlines())

new_list=[n.strip() for n in file1_data if n in file2_data]

print(new_list)

# https://replit.com/@appbrewery/day-26-3-exercise#main.py
