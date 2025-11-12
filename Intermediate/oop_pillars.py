class Book:
    # This is the constructor (__init__), it initializes the object's state (attributes)
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        # Encapsulation: The ISBN is a crucial piece of data bundled with the book
        self.isbn = isbn
        self.is_checked_out = False

    # A method (behavior) of the Book object
    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return f"'{self.title}' has been checked out."
        else:
            return f"'{self.title}' is already checked out."

# Creating objects (instantiation)
book1 = Book("Python Crash Course", "Eric Matthes", "978-1593276034") 
book2 = Book("Fluent Python", "Luciano Ramalho", "978-1449355739")

# Accessing attributes and calling methods
print(book1.title) # Output: Python Crash Course
print(book1.check_out()) # Output: 'Python Crash Course' has been checked out.

# Inheritance: Ebook inherits attributes and methods from the Book class
class Ebook(Book):
    def __init__(self, title, author, isbn, file_size):
        # Calls the parent (Book) constructor to handle common attributes
        super().__init__(title, author, isbn) 
        self.file_size = file_size
    
    # Polymorphism: Overriding the check_out method for specific Ebook behavior
    def check_out(self):
        # Ebooks don't physically "check out," they just grant a license
        self.is_checked_out = True 
        return f"'{self.title}' (Ebook) license granted. Download size: {self.file_size}MB."

# Creating an Ebook object
ebook1 = Ebook("Machine Learning for Dummies", "John Paul Mueller", "978-1119532855", 25.5)

# Calling the check_out method on both object types demonstrates Polymorphism:
print("\n--- Polymorphism Demo ---")
print(book2.check_out()) # Calls Book's check_out
print(ebook1.check_out()) # Calls Ebook's check_out (the overridden method)