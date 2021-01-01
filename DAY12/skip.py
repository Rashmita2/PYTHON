for i in range(5):
    if i == 3:
        #skips 3
        continue
    print(i)

print()
for i in range(5):
    if i == 3:
        #breaks when reach 3
        break
    print('Hello', i)

#defining the function, pass statement is to keep it empty
def fun():
    pass

