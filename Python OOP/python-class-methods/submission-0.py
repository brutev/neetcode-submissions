class Library:
    books_available = 100    # Total books in library

    # TODO: Implement class methods to manage book lending
    @classmethod
    def lend_books(cls,no_of:int)->int:
        cls.books_available -= no_of

    # TODO: Implement return_books method to increase the number of books available
    @classmethod
    def return_books(cls,no_of_books:int)-> int:
        cls.books_available += no_of_books



# Don't change the code below
print(f"Initial status: {Library.books_available} books available")
Library.lend_books(30)
print(f"After lending: {Library.books_available} books available")
Library.return_books(10)
print(f"After return: {Library.books_available} books available")
