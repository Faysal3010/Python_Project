'''
keyword arguments = arguments preceded by an identifier when we pass them to a function. The order of the arguments does not matter, unlike positional arguments Python knows the name of the arguments that out function receives.
'''

def hello(middle,first,last):
    print('Hello',first,middle,last)

hello(middle='Mahmud',first='Faysal',last='Sajen')