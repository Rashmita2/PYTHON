#key: value 
hobby = {"Loren": "Swimming",
         "Harry": "Basketball",
         "Sam": "Coding",
         "Tim": "Chess"}

print(hobby)
print(hobby["Tim"])
hobby["Smith"] = "Reading"
print(hobby)
print()
print()
while True:
    dic_key = input('Please enter the name: ')
    if dic_key == 'quit':
        break
    dict_value = hobby.get(dic_key)
    print(dict_value)

hobby_key = hobby.keys()
print(hobby_key)
