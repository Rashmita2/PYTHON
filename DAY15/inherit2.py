class Book():
    def __init__(self,title,pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return "Title: {}, Pages: {} ".format(self.title, self.pages)

    def __len__(self):
        return self.pages
    
    def __del__(self):
        print('A book is deleted')

b = Book("Python",200)
print(b)
print(len(b))
del b

