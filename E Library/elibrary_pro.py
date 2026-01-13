from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Book:
    """
    Represents a single book in the library.
    """
    title: str
    author: str
    is_borrowed: bool = False

    def borrow(self) -> bool:
        """
        Borrow the book if available.
        Returns True if borrowed successfully, else False.
        """
        if self.is_borrowed:
            return False
        self.is_borrowed = True
        return True

    def return_book(self) -> bool:
        """
        Return the book if it was borrowed.
        Returns True if returned successfully, else False.
        """
        if not self.is_borrowed:
            return False
        self.is_borrowed = False
        return True

    def status(self) -> str:
        """
        Returns the status of the book in human-readable form.
        """
        return "Borrowed" if self.is_borrowed else "Available"


class ELibrary:
    """
    Manages the collection of books and library operations.
    """

    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, title: str, author: str) -> None:
        """
        Adds a new book to the library.
        """
        title = title.strip()
        author = author.strip()

        if not title or not author:
            print("\n❌ Title and Author cannot be empty.\n")
            return

        self.books.append(Book(title=title, author=author))
        print("\n✅ Book added successfully!\n")

    def view_books(self) -> None:
        """
        Displays all books in the library.
        """
        if not self.books:
            print("\n📌 No books available in the library yet.\n")
            return

        print("\n📚 ------ Library Book List ------\n")
        for idx, book in enumerate(self.books, start=1):
            print(f"{idx}. {book.title} by {book.author} - {book.status()}")
        print()

    def borrow_book(self, book_number: int) -> None:
        """
        Borrows a book by its number.
        """
        book = self._get_book_by_number(book_number)
        if not book:
            return

        if book.borrow():
            print("\n✅ Book borrowed successfully!\n")
        else:
            print("\n❌ This book is already borrowed.\n")

    def return_book(self, book_number: int) -> None:
        """
        Returns a borrowed book by its number.
        """
        book = self._get_book_by_number(book_number)
        if not book:
            return

        if book.return_book():
            print("\n✅ Book returned successfully!\n")
        else:
            print("\n❌ This book was not borrowed.\n")

    def search_books(self, keyword: str) -> None:
        """
        Searches books by title or author (case-insensitive).
        """
        keyword = keyword.strip().lower()

        if not keyword:
            print("\n❌ Please enter a valid keyword.\n")
            return

        results = [
            book for book in self.books
            if keyword in book.title.lower() or keyword in book.author.lower()
        ]

        print("\n🔍 ------ Search Results ------\n")
        if not results:
            print("❌ No match found!\n")
            return

        for book in results:
            print(f"{book.title} by {book.author} - {book.status()}")
        print()

    def remove_book(self, book_number: int) -> None:
        """
        Removes a book from the library by its number.
        """
        book = self._get_book_by_number(book_number)
        if not book:
            return

        removed_book = self.books.pop(book_number - 1)
        print(f"\n✅ Removed: {removed_book.title} by {removed_book.author}\n")

    def show_statistics(self) -> None:
        """
        Shows total, borrowed, and available books count.
        """
        total = len(self.books)
        borrowed = sum(book.is_borrowed for book in self.books)
        available = total - borrowed

        print("\n📊 ------ Library Statistics ------")
        print(f"Total Books   : {total}")
        print(f"Borrowed      : {borrowed}")
        print(f"Available     : {available}\n")

    def _get_book_by_number(self, book_number: int) -> Optional[Book]:
        """
        Private helper method to validate and return book object.
        """
        if not self.books:
            print("\n📌 Library is empty.\n")
            return None

        if not (1 <= book_number <= len(self.books)):
            print("\n❌ Invalid book number.\n")
            return None

        return self.books[book_number - 1]


def get_valid_number(message: str) -> int:
    """
    Safely takes integer input from user.
    Keeps asking until a valid integer is entered.
    """
    while True:
        user_input = input(message).strip()
        if user_input.isdigit():
            return int(user_input)
        print("❌ Please enter a valid number.")


def main() -> None:
    library = ELibrary()

    while True:
        print("\n=== 📚 E-Library Menu ===\n")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Book")
        print("6. Remove Book")
        print("7. Library Statistics")
        print("8. Exit\n")

        choice = input("Enter choice (1-8): ").strip()

        if choice == "1":
            title = input("Enter title : ")
            author = input("Enter author: ")
            library.add_book(title, author)

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            book_no = get_valid_number("Enter book number to borrow: ")
            library.borrow_book(book_no)

        elif choice == "4":
            book_no = get_valid_number("Enter book number to return: ")
            library.return_book(book_no)

        elif choice == "5":
            keyword = input("Enter title/author keyword: ")
            library.search_books(keyword)

        elif choice == "6":
            book_no = get_valid_number("Enter book number to remove: ")
            library.remove_book(book_no)

        elif choice == "7":
            library.show_statistics()

        elif choice == "8":
            print("\n✅ Thank you for using E-Library. Goodbye!\n")
            break

        else:
            print("\n❌ Invalid choice. Please select 1-8.\n")


if __name__ == "__main__":
    main()
