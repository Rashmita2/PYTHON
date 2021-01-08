def func():
    print('Func() in name.py')

print('Top level name.py')

if __name__ == '__main__':
    print("name.py is run directly")
else:
    print("name.py is imported")