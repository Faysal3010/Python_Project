'''
str.format() = optinal method that gives users more control when displaying output
'''

animal='cow'
item='moon'

# print('The '+animal+' jumped over the '+item)
# print('The {} jumped over the {}'.format(animal, item))
# print('The {1} jumped over the {0}'.format(animal, item))
# print('The {animal} jumped over the {item}'.format(animal='cat', item='sun')) 

# text='The {} jumped over the {}'
# print(text.format(animal, item))


text='The {:10} jumped over the {}'#make space
print(text.format(animal, item))
text='The {:>10} jumped over the {}'#make space
print(text.format(animal, item))
text='The {:<10} jumped over the {}'#make space
print(text.format(animal, item))
text='The {:^10} jumped over the {}'#make space
print(text.format(animal, item))

number = 3.1416
print("Number is pi {:.2f}".format(number))

number1 = 10000
print("Number is pi {:,}".format(number1))
print("Number is pi {:b}".format(number1))
print("Number is pi {:o}".format(number1))
print("Number is pi {:x}".format(number1))
print("Number is pi {:e}".format(number1))
print("Number is pi {:E}".format(number1))