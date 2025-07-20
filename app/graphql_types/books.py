import strawberry
from typing import List
from data import db_books

@strawberry.type
class Book:
    title: str
    author: str
    description: str

    @staticmethod
    def fetch_books() -> List["Book"]:
        """
        Returns all books in the database.
        """
        return [
            Book(title=book["title"], author=book["author"], description=book["description"])
            for book in db_books
        ]

    @staticmethod
    def search_books(search_text: str) -> List["Book"]:
        """
        Returns books where the search text matches the title, author, or description (case-insensitive).
        """
        q = search_text.lower()
        return [
            Book(title=book["title"], author=book["author"], description=book["description"])
            for book in db_books
            if q in book["title"].lower() or q in book["author"].lower() or q in book["description"].lower()
        ]

@strawberry.type
class Query:
    @strawberry.field
    def fetch_books(self) -> List[Book]:
        """
        Fetch all books.
        """
        return Book.fetch_books()

    @strawberry.field
    def search_books(self, search_text: str) -> List[Book]:
        """
        Search for books by a query string in the title, author, or description.
        """
        return Book.search_books(search_text)

