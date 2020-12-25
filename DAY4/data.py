#key-value pair
data = {1:'Red',
        2:'Blue',
        3:'Yellow'}
print(data)

#to fetch a particular value, we should use a key
print(data[2])
#second way to fetch the value,
# it prints the value with the key inside the get
print(data.get(1))
#if we don't have a key 5, it prints the message
print(data.get(5,'Not found'))

#merge two list to a dictionary
key = ['Harry', 'Loren', 'tapia']
value = ['burger', 'sandwich', 'Biryani']
data1 = dict(zip(key,value))
print(data1)
#add a new value to the dictionary
data1['Anthony'] = 'pizza'
print(data1)

#to delete the dictinary
del data1['Harry']
print(data1)