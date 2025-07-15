'''
scope = the region that variable is recognized. A variable is only available from inside the region it is created. A global abd locally scoped versions of a variable can be created.
'''

name='Faysal' #global scope(available inside and outside fuction)

def display():
    name='Mahmud'#local scope(available only inside   this fuction)
    print(name)

display()
print(name)    
