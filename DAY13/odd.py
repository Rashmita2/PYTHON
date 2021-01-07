def is_even(n):
    return n%2 == 0
nums = [3,4,6,23,52,24,75]

#filter takes function and iterable
even = list(filter(is_even, nums))
doubles = list(map(lambda n: n*2, even))
print(even)
print(doubles)