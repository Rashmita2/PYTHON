list1 = [1,2,3,4]
list2 = ['one','two','three','four']
zipped = list(zip(list1,list2))
print(zipped)
#unzip the list
unzipped = list(zip(*zipped))
print(unzipped)

for l1,l2 in zip(list1,list2):
    print(l1)
    print(l2)

items = ['Apple','Banana','Orange']
counts = [3,6,4]
prices = [0.99,0.25,0.50]
sentences = []
for (item,count,price) in zip(items,counts,prices):
    item,count,price = str(item), str(count), str(price)
    sentence = 'I bought '+ count + ' '+ item + ' at ' + price
    sentences.append(sentence)
print(sentences)
