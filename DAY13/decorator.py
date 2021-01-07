def division(a,b):
    return a/b

def dec_func(func):

    def inner(a,b):
        if a < b:
            a, b = b,a
            return func(a,b)

    return inner

division1 = dec_func(division)

print(division1(2,4))


