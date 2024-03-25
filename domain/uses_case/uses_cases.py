from typing import List

from domain.models.book import Book
from domain.repository.library_repository import LibraryRepository


class LibraryUsesCase:
    def __init__(self, library_repository: LibraryRepository):
        self.library_repository = library_repository

    def create_book(self, book: Book) -> Book:
        return self.library_repository.create_book(book)

    def search_by_title(self, title: str) -> List[Book]:
        return self.library_repository.search_by_title(title)

    def search_by_author(self, author: str) -> List[Book]:
        return self.library_repository.search_by_author(author)

    def search_by_year(self, year: str) -> List[Book]:
        return self.library_repository.search_by_year(year)

    def delete_book(self, id_book: str) -> List[Book]:
        return self.library_repository.delete_book(id_book)
