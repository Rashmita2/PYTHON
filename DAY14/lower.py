def end_other(a, b):
    a = a.lower()
    b = b.lower()
    if b in a:
        return True
    else:
        return False

print(end_other('Hiabc', 'abc'))

