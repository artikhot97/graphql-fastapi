import strawberry
from typing import List


@strawberry.type
class Book:
    title: str
    author: str

    @staticmethod
    def fetch_books()-> List["Book"]:
        return [
        Book(title="1984", author="George Orwell"),
        Book(title="Clean Code", author="Robert C. Martin")
    ]

@strawberry.type
class Query:
    @strawberry.field
    def fetch_books()->List[Book]:
        return Book.fetch_books()

