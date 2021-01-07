nums = [2,5,6,7]
it = iter(nums)
#gives the next value
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(next(it))