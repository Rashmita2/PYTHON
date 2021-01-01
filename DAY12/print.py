for i in range(4):
    print('*'*i)

print()
print("####")
print("####")
print("####")
print('#'*4)
print()

for i in range(4):
    for j in range(4):
        print("#", end=" ")

for i in range(4):
    for j in range(4-i):
        print('# ',end="")

    print()