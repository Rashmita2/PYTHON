computer = ['mouse','keyboard', 'monitor', 'speaker']
another = computer
a = b = c = d = e = f = another

print(a)
print()
b += ['CPU']
print(b)
print(a)
print(len(computer))
computer.append('webcam')
print(computer)

print()
print()
for i in computer:
    print('{}. {}'.format(computer.index(i)+1, i))