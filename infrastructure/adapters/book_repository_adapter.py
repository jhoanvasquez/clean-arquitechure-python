from typing import List

from domain.models.book import Book
from domain.repository.library_repository import LibraryRepository


class BookRepositoryAdapter(LibraryRepository):
    def __init__(self):
        new_book = Book("don quijote", "Miguel de cervantes", "1605")
        new_book_1 = Book("El hobbit", "Tolkien", "1937")
        new_book_2 = Book("Prueba", "Prueba", "1937")
        self.list_book: List[Book] = []

        self.list_book.append(new_book.to_dict())
        self.list_book.append(new_book_1.to_dict())
        self.list_book.append(new_book_2.to_dict())

    def create_book(self, book: Book) -> Book:
        self.list_book.append(book.to_dict())
        return book.to_dict()

    def search_by_title(self, title: str) -> List[Book]:
        filtered_list = list(filter(lambda i: i['title'].lower() == title.lower(), self.list_book))
        return filtered_list

    def search_by_author(self, author: str) -> List[Book]:
        filtered_list = list(filter(lambda i: i['author'].lower() == author.lower(), self.list_book))
        return filtered_list

    def search_by_year(self, year: str) -> List[Book]:
        filtered_list = list(filter(lambda i: i['year_released'] == year, self.list_book))
        return filtered_list

    def delete_book(self, title: str) -> List[Book]:
        result_search = self.search_by_title(title)
        self.list_book = list(filter(lambda i: i['title'].lower() != title.lower(), self.list_book))
        return result_search
