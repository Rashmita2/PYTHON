#don't need to close the file in width
with open("sample.txt",'r') as new_file:
    for line in new_file:
        if "JAB" in line.upper():
            print(line, end='')