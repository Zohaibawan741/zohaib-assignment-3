class Book:
    def __init__(self, title, author, copies=1):
        self.title, self.author, self.copies = title, author, copies

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search(self, key, value):
        return [b for b in self.books if getattr(b, key) == value.lower()]

    def manage_copies(self, title, action):
        for b in self.books:
            if b.title.lower() == title.lower() and getattr(b, 'copies') > 0:
                b.copies -= 1 if action == "borrow" else -1
                return f"Book '{title}' {action}ed. {b.copies} copies available."
        return f"Book '{title}' not available."

book1, book2 = Book("Intro to Python", "John Doe", 5), Book("Data Science", "Jane Smith", 3)
library = Library()
library.add_book(book1)
library.add_book(book2)

print(library.search("title", "Intro to Python"))
print(library.search("author", "Jane Smith"))

print(library.manage_copies("Intro to Python", "borrow"))
print(library.manage_copies("Intro to Python", "borrow"))
print(library.manage_copies("Intro to Python", "return"))

print(library.manage_copies("Intro to Python", "borrow"))