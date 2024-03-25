from domain.models.book import Book
from domain.uses_case.uses_cases import LibraryUsesCase
from infrastructure.adapters.book_repository_adapter import BookRepositoryAdapter

book_repository = BookRepositoryAdapter()
book_uses_cases = LibraryUsesCase(book_repository)


class Console:
    @staticmethod
    def validate_response(response):
        if not response:
            return "Libro no existente"
        return response

    def __init__(self):
        done = False
        while not done:
            print("######### Bienvenido al menú de la biblioteca #########")
            print("1.Agregar libro")
            print("2.Buscar libro por titulo")
            print("3.Buscar libro por autor")
            print("4.Buscar libro por año")
            print("5.Eliminar libro")
            print("6.Salir")

            text_input = input("Digite una opción: ")
            if text_input == "1":
                title_input = input("Titulo: ")
                author_input = input("Autor: ")
                year_input = input("Año lanzamiento: ")
                new_book = Book(title_input, author_input, year_input)
                response = book_uses_cases.create_book(new_book)
                print(response)

            if text_input == "2":
                title_input = input("Titulo: ")
                response = book_uses_cases.search_by_title(title_input)
                print(self.validate_response(response))

            if text_input == "3":
                author_input = input("Autor: ")
                response = book_uses_cases.search_by_author(author_input)
                print(self.validate_response(response))

            if text_input == "4":
                year_input = input("Año lanzamiento: ")
                response = book_uses_cases.search_by_year(year_input)
                print(self.validate_response(response))

            if text_input == "5":
                title_input = input("Titulo: ")
                response = book_uses_cases.delete_book(title_input)
                print(self.validate_response(response))

            if text_input == "6":
                done = True
