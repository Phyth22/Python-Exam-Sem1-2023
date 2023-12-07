#



#define class
#A Class is an object constructor for creating objects

#define object
#An object is a data field that has unique attributes and behaviors

#2
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

    def get_title_and_author(self):
        return f"{self.title} by {self.author}"

class Ebook(Book):
    def __init__(self, title, author, pages, book_format):
        super().__init__(title, author, pages)
        self.format = book_format

    def display_info(self):
        super().display_info()
        print(f"Format: {self.format}")

#  instance of  Book class
book_instance = Book(title="Sample Book", author="John Doe", pages=200)

# Display information about the book
book_instance.display_info()

# Create an instance of the Ebook class
ebook_instance = Ebook(title="Ebook Title", author="Jane Smith", pages=150, book_format="PDF")

# Display information about the ebook
ebook_instance.display_info()

# Accessing the method from the base class
title_and_author = book_instance.get_title_and_author()
print(title_and_author)
