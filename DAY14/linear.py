#linear search
pos = -1
def lin_search(list, n):
    i=0
    while i<len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i = i+1
    return False

list = [3,4,6,2,9,7]
n = 9
if lin_search(list, n):
    print('FOUND at',pos+1)
else:
    print('Not found')


