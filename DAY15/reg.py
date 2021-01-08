import re
patterns = ['term1','term2']
text = 'This is string with term1, not others'

for pattern in patterns:
    print('I am searching for: ' + pattern)

#search the pattern in the text
    if re.search(pattern, text):
        print("match")
    else:
        print("no match")