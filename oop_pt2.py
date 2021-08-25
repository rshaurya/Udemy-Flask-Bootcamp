# Special methods...

class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self):
        return f"Titel: {self.title}, Author: {self.author}"

    def __len__(self):
        return self.pages

myBook = Book('Python', 'Shaurya', 250)
length_book = len(myBook)
print(length_book)
