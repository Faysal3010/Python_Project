#slicing = create a substring by extracting elements from another string indexing[] or slice()

#       [start:stop:step]

# name = input('Forward_name: ')
# reverse_name = name[::-1]
# print("reverse_name: ",reverse_name)

name ="Faysal Mahmud"

first_name = name[:6]
last_name = name[7:]
funky_name = name[::2]
reverse_name = name[::-1]
reverse_1_name = name[::-2]

print("Full name:",name)
print("first_name:",first_name)
print("last_name:",last_name)
print("funky_name:",funky_name)
print("reverse_name:",reverse_name)
print("reverse_1_name:",reverse_1_name)

website1 ="http://google.com"
website2 ="http://wikipedia.org"
slice =slice(7,-4)
print(website1[slice],website2[slice])