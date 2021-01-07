a = 5
b = 0
try:
    print(a/b)

except Exception as e:
    print('Division error,', e)
    print('Cannot divide the number by 0')

finally:
    print('Resources closed')
