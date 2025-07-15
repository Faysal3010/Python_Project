import os
path='F:\\PDF\\Python\\Learning_Python.pdf'
if os.path.exists(path):
    print("That file already exists")
    if os.path.isfile(path):
        print("That is file")
    elif os.path.isdir(path):
        print("That is a directory")    
else:
    print("That file does not exist")