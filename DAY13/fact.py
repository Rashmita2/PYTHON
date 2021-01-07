def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact(num-1)





answer = fact(5)
print(answer)