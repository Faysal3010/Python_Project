'''
*args = parameter that will pack arguments into a tuple useful so that a function can accept a varying number of arguments
'''

# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
# print(add(1,2,3,5,6,8))  


#if u want to change the value , we know that tuple is not changeable. So, make it list and then change the value


def add(*args):
    sum = 0
    args=list(args)# make it list
    args[2]=0
    for i in args:
        sum += i
    return sum
print(add(1,2,3,5,6,8))  

