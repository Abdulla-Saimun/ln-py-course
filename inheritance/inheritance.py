class Publications:
    def __init__(self, title, price):
        self.title = title
        self.price = price

class Periodical(Publications):
    def __init__(self, title, price, publisher, period):
        super().__init__(title, price)
        self.publisher = publisher
        self.period = period


class Book(Publications):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages


class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)

class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)

b1 = Book('mockingjay', 'suzan', 120, 320)
n1 = Newspaper('Prothom-Alo', 'transcom', 12, 1)
print(b1.title)
print(n1.publisher)