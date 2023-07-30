from __future__ import annotations


class Book:

    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out_by: None | Borrower = None

    def check_out(self, borrower: Borrower) -> None | Borrower:
        if not self.checked_out_by:
            self.checked_out_by = borrower
            return self.checked_out_by

    def check_in(self, borrower: Borrower) -> None:
        if self.checked_out_by:
            self.checked_out_by = None


class Author:

    def __init__(self, name: str):
        self.name = name
        self.books = set()

    def get_books(self) -> list[str]:
        return sorted(list(self.books))


class Borrower:

    def __init__(self, name, email):
        # todo implement better unique ID (eg DL number, phone number)
        self.name = name
        self.email = email
        self.books_checked_out = []


class Log:

    def __init__(self):
        self.demand_threshold: float = .5  # exclusive
        self.lookback_size = 10  # inclusive

        self.book_count: dict[str, int] = dict()  # {title: count}
        self.book_list: list[str] = list()  # [title, title, title..]

    def update_log(self, book_title: str) -> None:
        if book_title in self.book_count:
            self.book_count[book_title] += 1
        else:
            self.book_count[book_title] = 1

        self.book_list.append(book_title)
        if len(self.book_list) > 10:
            removed_book = self.book_list.pop(0)

            self.book_count[removed_book] -= 1

    def find_high_demand(self) -> None | str:
        if len(self.book_list) < self.lookback_size - 1:
            return None

        for k, v in self.book_count.items():
            if (v / len(self.book_list)) > self.demand_threshold:
                return k


class Library:

    def __init__(self):
        self.checkout_limit = 2

        self.books: dict[str, list[Book]] = dict()  # book_title: [Book,]
        self.borrowers: dict[str, Borrower] = dict()  # borrower_email: Borrower
        self.authors: dict[str, Author] = dict()  # author_name: Author

        self.log: Log = Log()

    def add_book(self, title, author_name, isbn):
        # find/register the author
        # register book to library
        author = self.find_or_create_author(author_name)
        author.books.add(title)
        added_book = Book(title, author_name, isbn)

        if title in self.books:
            self.books[title].append(added_book)
        else:
            self.books[title] = [added_book]

    # warning: assumes an absence of shenanigans (bad assumption)
    def add_borrower(self, name, email) -> bool:
        if email in self.borrowers:
            return False  # id already in use

        # register the borrower to the library
        self.borrowers[email] = Borrower(name, email)
        return True

    def find_or_create_author(self, author_name) -> Author:
        # if author is registered with the library, return author info
        # else, register the author with the library, then return the author
        if author_name not in self.authors:
            self.authors[author_name] = Author(author_name)

        return self.authors[author_name]

    def find_book(self, book_title) -> None | Book:
        # # erroneous specifications
        # # implementation exceeds specifications

        # # if book belongs to library
        # # return book object; else return nothing
        if book_title in self.books:
            if len(self.books[book_title]) > 0:  # consider removal
                return self.books[book_title].pop()

    def get_book_copy(self, book_title) -> tuple[str, str, str]:
        # search library
        if len(self.books[book_title]) > 0:
            book = self.books[book_title][0]
            return book.title, book.author, book.isbn
        # search borrowers
        for borrower in self.borrowers.values():
            for book in borrower.books_checked_out:
                if book.title == book_title:
                    return book.title, book.author, book.isbn

    def find_borrower(self, borrower_email) -> None | Borrower:
        # if borrower is registered with the library
        # return borrower info; else, return nothing
        if borrower_email in self.borrowers:
            return self.borrowers[borrower_email]

    def in_stock(self, book_title) -> int:
        # if book is in library
        if book_title in self.books:
            # return count
            return len(self.books[book_title])
        return 0

    def check_out_book(self, book_title, borrower_email) -> None | Book:
        # unregistered borrower
        if borrower_email not in self.borrowers:
            return None

        # borrower exceeded checkout_limit
        borrower = self.borrowers[borrower_email]
        if len(borrower.books_checked_out) > self.checkout_limit:
            return None

        # stretch goal
        self.log.update_log(book_title)
        check = self.log.find_high_demand()
        if check:
            book_info = self.get_book_copy(check)
            self.add_book(book_info[0], book_info[1], book_info[2])

        # stock check
        if self.in_stock(book_title) > 0:
            book = self.books[book_title].pop()
            # update book.checked_out_by
            book.check_out(borrower)
            # update borrower books_checked_out
            borrower.books_checked_out.append(book)

            return book
        else:
            return None

    def check_in_book(self, book) -> bool:
        # if (book belongs to library) and (was checked out)
        if book.title in self.books and book.checked_out_by:
            # if borrower is registered
            if book.checked_out_by.email in self.borrowers:
                # check-in book to library
                book.check_in(book.checked_out_by.email)
                self.books[book.title].append(book)
                return True
        return False



import unittest  # noqa
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
        self.assertIsNone(book2)
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
