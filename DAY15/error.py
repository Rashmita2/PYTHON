try:
    f = open('sample.txt','r')
    f.write('This is first line')
except IOError:
    print('Could not find the file or read data')
else:
    print("Success")
    f.close()