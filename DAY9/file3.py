
f = open('data.txt','r')
#print(f.read())
# read prints all from the file and readline prints the first line
#print(f.readline())
#readline(4) is to read the fourth character
print(f.readline(), end="#")

f1 = open('data2.txt', 'w')
f1.write("something")
