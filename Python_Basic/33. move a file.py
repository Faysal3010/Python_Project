import os

source = "path"
destination ="path_1"

try:
    if os.path.exists(destination):
     print()
    else:
       os.replace(source,destination)
       print(source,"was moved")

except FileNotFoundError:
    print(source,'was not found')    