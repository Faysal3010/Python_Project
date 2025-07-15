#dictionary = A changeable, unordered collection of unique key:value pairs Fast because they use hashing, allow us to access a value quickly

capitals ={
    'USA':'Washington DC',
    'India':'New Dehli',
    'China':'Beijing',
    'Russian':'Moscow',
    'Bangladesh':'Dhaka'
}
# print (capitals['Bangladesh'])
# print (capitals['Pakistan'])# give error message so that use 'get'
# print (capitals.get('Pakistan'))
# print (capitals.keys())
# print (capitals.values())
# print (capitals.items())
# capitals.update({'Pakistan':'Islamabad'})
# capitals.pop('China')
# capitals.clear()
for key,value in capitals.items():
    print (key, value)
