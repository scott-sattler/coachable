from __future__ import annotations

# nearly impossible to not be labeled a "cheater"... bro...

''' TODO

(Bonus) Stretch Goal (10%):

Now that we have an inventory system. Libararies typically don't have multiple books in store unless a book is high in 
demand.

Your goal is to create a sub system such that if a book is high in demand say: ~50% of checkout attempts for the last 10 
checkouts, we should increase the inventory for that book by 1.

E.g. If the last 5 of the 10 attempts from the call `check_out_book()` was for George Orwell's 1984, then we should 
increase the inventory for 1984's copies/inventory by 1.


While we have tests for this, we do not and will not have starter code for this. It's meant to be more vague, and how 
easy this is task will be is dependent on how well the structure of the code was constructed for the previous 
requirements, i.e. if OOD principles were utilized. Show us what you got!
'''

'''
notes:
-Borrowers should not be able to return books if the library doesn't own them.
-Borrowers cannot have more than 3 books that have been checkout by them, 
 and we should also know what books they have checked out.

-(UPDATE 1 BELOW) Books that are added to the library can be assumed to be unique.
-When books are already checked out, they cannot be taken and/or checkout again.


-(UPDATE 1) The library should now support multiple copies of the same book.
'''

'''
NOTE:
this system will not track individual borrower damage to books that is not caught at the time of return.

proposals:
Book.unique_id: books should be stamped with a (ms accurate) timestamp upon manual entry into database
Borrower.unique_id should be assigned a upon account creation
'''

'''
Your goal is to create a sub system such that if a book is high in demand say: ~50% of checkout attempts for the last 10 
checkouts, we should increase the inventory for that book by 1.

E.g. If the last 5 of the 10 attempts from the call `check_out_book()` was for George Orwell's 1984, then we should 
increase the inventory for 1984's copies/inventory by 1.
'''


# individual book objects
# vs book object representing... unique ISBN number

class Book:
    def __init__(self, title: str, author: str, isbn: int):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out_by: Borrower = None

    def check_out(self, borrower: Borrower) -> bool:
        ''' returns bool indicating successful operation '''
        if self.checked_out_by:
            return False
        self.checked_out_by = borrower
        return True

    def check_in(self, borrower: Borrower) -> bool:
        ''' returns bool indicating successful operation '''
        if self.checked_out_by:
            self.checked_out_by = None
            return True
        return False

    # def checked_out_by(self) -> list[str]:
    #     self._borrowers.sort()
    #     return self._borrowers


class Inventory:
    def __init__(self, foo):
        self.foo = foo


class Author:
    def __init__(self, name: str):
        self.name = name
        self.books = set()

    def get_books(self) -> list[str]:
        self.books.sort()
        return self.books


class Borrower:
    def __init__(self, name, email):
        # todo implement better unique ID (eg DL number, phone number)
        self.name = name
        self.email = email
        self.books_checked_out = []


class Library:
    def __init__(self):
        self.books = {}  # book_name: Book
        self.borrowers = {}  # borrower_email: Borrower
        self.authors = {}  # author_name: Author
        # todo search by author

        # self.borrowers = {}  # borrower_name: checked_out books_name(s)

    def add_book(self, title, author_name, isbn):
        ''' TODO returns bool indicating successful operation '''
        # Find or register the author
        # Register the book to the library
        author = self.find_or_create_author(author_name)
        author.books.add(title)
        added_book = Book(title, author, isbn)

        self.books[title] = added_book  # todo update

    def add_borrower(self, name, email) -> bool:
        ''' returns bool indicating successful operation '''
        # Register the borrower to the library
        # assumes no shenanigans (bad assumption)

        # pseudo_unique_id = name + email
        # if pseudo_unique_id in self.borrowers:
        #     return False

        if email in self.borrowers:
            return False  # id already in use

        self.borrowers[email] = Borrower(name, email)
        return True

    def find_or_create_author(self, author_name) -> Author:
        # If the author is registered with the library, return the author info
        # Else, register the author with the library, then return the author.
        if author_name not in self.authors:
            self.authors[author_name] = Author(author_name)

        return self.authors[author_name]

    def find_book(self, book_title) -> None | Book:
        # If the book belongs to the library, return the book object
        # Else, return nothing.
        if book_title in self.books:
            return self.books[book_title]
        return None

    def find_borrower(self, borrower_email) -> None | Borrower:
        # If the borrower is registered with the library, return the borrower info
        # Else, return nothing.
        if borrower_email in self.borrowers:
            return self.borrowers[borrower_email]
        return None

    def in_stock(self, book_title) -> bool:
        # todo update multiple copies
        if book_title in self.books:
            return True
        return False

    def check_out_book(self, book_title, borrower_email) -> None | Book:
        borrower = self.borrowers[borrower_email]
        if len(borrower.books_checked_out) > 2:
            return None

        # todo review this todo     todo update multiple copies
        if self.in_stock(book_title):
            # todo review this todo decrement available books
            book = self.books[book_title]
            borrower.books_checked_out.append(book)

            if book.check_out(borrower):
                return book
            else:
                return None
        else:
            return None

    def check_in_book(self, book):
        ''' returns bool indicating successful operation '''
        # If the book belongs to the library,
        # and the borrower of the book is registered to the library,
        # add it back in, and return True
        # Else, return False
        # need unique id
        if book in self.books:
            return self.books[book].check_in(book.email)
        return False



import unittest
# from library import Book, Library


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.library.add_borrower("Alice", "alice@example.com")
        self.library.add_borrower("Bob", "bob@example.com")
        self.library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "978-3-16-148410-0")
        self.library.add_book("To Kill a Mockingbird", "Harper Lee", "978-0-446-31078-9")
        self.library.add_book("To Kill a Mockingbird", "Harper Lee", "978-0-446-31078-9")
        self.library.add_book("1984", "George Orwell", "978-0-143-03928-8")
        self.library.add_book("Animal Farm", "George Orwell", "978-1-379-38828-7")

    def test_check_out_book(self):
        # Valid check-out
        book1 = self.library.check_out_book("The Great Gatsby", "alice@example.com")
        self.assertEqual(book1.checked_out_by.name, "Alice")

        # Book already checked out
        book3 = self.library.check_out_book("The Great Gatsby", "bob@example.com")
        self.assertIsNone(book3)

        # Book not found
        book4 = self.library.check_out_book("Moby Dick", "alice@example.com")
        self.assertIsNone(book4)

        # Borrower not found
        book5 = self.library.check_out_book("To Kill a Mockingbird", "charlie@example.com")
        self.assertIsNone(book5)

    def test_check_in_book(self):
        # Valid check-in
        book1 = self.library.check_out_book("The Great Gatsby", "alice@example.com")
        status = self.library.check_in_book(book1)
        self.assertIs(status, True)
        self.assertIsNone(self.library.find_book("The Great Gatsby").checked_out_by)

        # Book not from library
        book2 = Book("Moby Dick", "Alice", "978-2-628-32749-0")
        status = self.library.check_in_book(book2)
        self.assertIs(status, False)

        # Borrower not from library
        book3 = Book("Moby Dick", "Alice", "978-2-628-32749-0")
        book3.author = "John"
        status = self.library.check_in_book(book2)
        self.assertIs(status, False)

    def test_find_book(self):
        # Book found
        book = self.library.find_book("The Great Gatsby")
        self.assertEqual(book.title, "The Great Gatsby")

        # Book not found
        book = self.library.find_book("Moby Dick")
        self.assertIsNone(book)

    def test_find_borrower(self):
        # Borrower found
        borrower = self.library.find_borrower("alice@example.com")
        self.assertEqual(borrower.name, "Alice")
        self.assertEqual(borrower.email, "alice@example.com")

        # Borrower not found
        borrower = self.library.find_borrower("charlie@example.com")
        self.assertIsNone(borrower)

    def test_find_or_create_author(self):
        # Author found
        author = self.library.find_or_create_author("F. Scott Fitzgerald")
        self.assertEqual(author.name, "F. Scott Fitzgerald")

        # Author created
        author = self.library.find_or_create_author("Ernest Hemingway")
        self.assertEqual(author.name, "Ernest Hemingway")
        self.assertEqual(len(self.library.authors), 4)  # 3 pre-existing authors + new author

    # Updated requirement tests
    def test_check_out_multiple_books(self):
        # Valid check-out multiple copies
        book2_0 = self.library.check_out_book("To Kill a Mockingbird", "alice@example.com")
        self.assertEqual(book2_0.checked_out_by.name, "Alice")
        book2_1 = self.library.check_out_book("To Kill a Mockingbird", "bob@example.com")
        self.assertEqual(book2_1.checked_out_by.name, "Bob")

    def test_author_information(self):
        # Author books written
        self.assertEqual(self.library.authors["George Orwell"].books, {"1984", "Animal Farm"})

    def test_borrower_limit(self):
        # Borrower limit
        book1 = self.library.check_out_book("The Great Gatsby", "alice@example.com")
        book2 = self.library.check_out_book("To Kill a Mockingbird", "alice@example.com")
        book3 = self.library.check_out_book("1984", "alice@example.com")
        book4 = self.library.check_out_book("Animal Farm", "alice@example.com")
        self.assertEqual(book1.checked_out_by.name, "Alice")
        self.assertEqual(book2.checked_out_by.name, "Alice")
        self.assertEqual(book3.checked_out_by.name, "Alice")
        self.assertIsNone(book4)
        # self.assertIsFalse(book4)

    def test_comprehensive(self):
        # Comprehensive
        book1 = self.library.check_out_book("To Kill a Mockingbird", "alice@example.com")
        self.assertEqual(book1.checked_out_by.name, "Alice")
        book2 = self.library.check_out_book("1984", "bob@example.com")
        self.assertEqual(book2.checked_out_by.name, "Bob")
        book3 = self.library.check_out_book("1984", "bob@example.com")
        self.assertIsNone(book3)
        book4 = self.library.check_out_book("Animal Farm", "bob@example.com")
        self.assertEqual(book4.checked_out_by.name, "Bob")
        book5 = self.library.check_out_book("1984", "charlie@example.com")
        self.assertIsNone(book5)
        book6 = self.library.check_out_book("To Kill a Mockingbird", "charlie@example.com")
        self.assertIsNone(book6)
        book7 = self.library.check_out_book("1984", "david@example.com")
        self.assertIsNone(book7)
        book8 = self.library.check_out_book("Animal Farm", "david@example.com")
        self.assertIsNone(book8)
        self.library.add_borrower("David", "david@example.com")
        book9 = self.library.check_out_book("To Kill a Mockingbird", "david@example.com")
        self.assertEqual(book9.checked_out_by.name, "David")
        book10 = self.library.check_out_book("The Great Gatsby", "alice@example.com")
        self.assertEqual(book10.checked_out_by.name, "Alice")

    # Strecth goal tests
    def test_supply_management(self):
        # Supply management
        self.library.add_borrower("Charlie", "charlie@example.com")
        self.library.add_borrower("David", "david@example.com")

        # Simulate check-outs for a given day
        book1 = self.library.check_out_book("1984", "alice@example.com")
        self.assertEqual(book1.checked_out_by.name, "Alice")
        book2 = self.library.check_out_book("1984", "bob@example.com")
        self.assertEqual(book2.checked_out_by.name, "Bob")
        book3 = self.library.check_out_book("1984", "bob@example.com")
        self.assertIsNone(book3)
        book4 = self.library.check_out_book("Animal Farm", "bob@example.com")
        self.assertEqual(book4.checked_out_by.name, "Bob")
        book5 = self.library.check_out_book("1984", "charlie@example.com")
        self.assertIsNone(book5)
        book6 = self.library.check_out_book("To Kill a Mockingbird", "charlie@example.com")
        self.assertEqual(book6.checked_out_by.name, "Charlie")
        book7 = self.library.check_out_book("1984", "david@example.com")
        self.assertIsNone(book7)
        book8 = self.library.check_out_book("Animal Farm", "david@example.com")
        self.assertIsNone(book8)
        book9 = self.library.check_out_book("To Kill a Mockingbird", "david@example.com")
        self.assertEqual(book9.checked_out_by.name, "David")
        book10 = self.library.check_out_book("The Great Gatsby", "alice@example.com")
        self.assertEqual(book10.checked_out_by.name, "Alice")

        # Simulate total inventory after check-outs
        self.library.check_in_book(book1)
        self.assertEqual(self.library.in_stock("1984"), 2)

        # Simulate edge cases
        # Just becase the history of checkouts for a given book is pass 5
        # does not mean that we need to order more copies of the book
        # In this case, we still have copies in stock, so the order should not be placed
        book11 = self.library.check_out_book("1984", "bob@example.com")
        self.assertEqual(book11.checked_out_by.name, "Bob")
        self.library.check_in_book(book11)
        self.assertEqual(self.library.in_stock("1984"), 2)


if __name__ == '__main__':
    unittest.main()
