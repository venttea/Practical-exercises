class Book:
    def __init__(self, author, pages, year, title):
        self.author = author
        self.pages = pages
        self.year = year
        self.title = title

    def __str__(self):
        return f"Автор книжки: {self.author}, назвается '{self.title}', количество страничек: {self.pages}, написана в {self.year} г."

author = input("Введите имя автора: ")
title = input("Введите название книги: ")
pages = int(input("Введите количество страниц: "))
year = int(input("Введите год издания: "))

if not author.isalpha():
    print("Автор должен содержать только буквы")
elif year > 2025:
    print("Год не может быть больше 2025")
elif not 5 <= pages <= 2000:
    print("Страниц должно быть от 5 до 2000")
elif len(title) > 100:
    print("Название слишком длинное")
else:
    book = Book(author, title, pages, year)
    print(book)