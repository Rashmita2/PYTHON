computer = ['mouse','keyboard', 'monitor', 'speaker']

for i in computer:
    print(i)

print()
print(computer[3])
print(computer[0:3])

#list are mutable, we get the same id
another = computer
print(id(computer))
print(id(another))
#concatening the list, as it is mutable
computer += ['CPU']
print(computer)
print(another)