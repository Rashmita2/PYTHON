pos = -1

def bin_search(list1, target):
    low = 0
    high = len(list1)-1
    while low <= high:
        mid = (high+low) // 2

        if list1[mid] == target:
            globals()['pos'] = mid
            return  True
        else:
            if list1[mid] < target:
                low = mid
            else:
                high = mid

list2 = [3,5,35,65,75,76]
target = 75

if bin_search(list2, target):
    print("found at ", pos+1)
else:
    print("not found")