#list inside list
number = [
    [1,2,3], #row0
    [4,5,6], #row1
    [7,8,9],
    [0]
]
for row in number:
    for col in row:
        print(col)
    