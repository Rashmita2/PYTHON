import re
text = "A random string"
pattern = re.compile("[ABC]")
#search for the text using that pattern
result = pattern.search(text)
print(result)