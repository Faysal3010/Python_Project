'''
nested functions calls = function calls inside other function calls innermost function calls are resloved first returned value is used as argument for the next outer function
'''

# num = input("Enter a whole positive number: ")
# num = float(num)
# num=abs(num)
# num = round(num)
# print(num)

#  |
#  |
#  |
# \ /
#  '

print(abs(round(float(input("Enter a whole positive number: ")))))