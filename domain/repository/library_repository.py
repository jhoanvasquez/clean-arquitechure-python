from abc import abstractmethod
from typing import List

from domain.models.book import Book


class LibraryRepository:
    @abstractmethod
    def create_book(self, book: Book) -> Book:
        pass

    @abstractmethod
    def search_by_title(self, title: str) -> List[Book]:
        pass

    @abstractmethod
    def search_by_author(self, author: str) -> List[Book]:
        pass

    @abstractmethod
    def search_by_year(self, year: str) -> List[Book]:
        pass

    @abstractmethod
    def delete_book(self, id_book: str) -> List[Book]:
        pass
