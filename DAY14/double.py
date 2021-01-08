#print double character
def doubleChar(str):
    result = ""
    for char in str:
        result += char * 2
    return result

print(doubleChar('T'))