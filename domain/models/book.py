class Book:
    def __init__(self, title, author, year_released):
        self.title = title
        self.author = author
        self.year_released = year_released

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "year_released": self.year_released
        }
