def count(list):
    even = 0
    odd = 0
    for i in list:
        if i%2 == 0:
            even +=1
        else:
            odd+=1
    return even,odd

list = [24,35,23,54,22,76,85,36]
even, odd = count(list)
print(odd)
print(even)