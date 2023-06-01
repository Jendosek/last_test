#12
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

get_info = Book(title="Black and Rad", author="Zenichka")
print(f"Назва книжки: {get_info.title}")
print(f"Автор книжки: {get_info.author}")

