def multiply(x,y):
    result = x*y
    return result

for val in range(1,10):
    res = multiply(2,val)
    print('2 * {} = {}'.format(val,res))
