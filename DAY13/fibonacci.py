def fib(num):
    a = 0
    b = 1
    if num == 1:
        print(a)
    else:
        for i in range(0,num):
            a,b = b, a+b
            print(b)



fib(10)



