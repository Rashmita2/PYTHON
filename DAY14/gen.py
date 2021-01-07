def top_ten():
    yield 4
    yield 5


values = top_ten()

print(values.__next__())
print(values.__next__())