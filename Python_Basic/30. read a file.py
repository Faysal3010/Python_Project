try:
 with open('C:\\VScodeDrive\\VSCode\\Python\\text.txt') as text:
    print(text.read())
except FileNotFoundError:
  print("Could not found")    