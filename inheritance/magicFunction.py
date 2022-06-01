# using __str__ and __repr__

class Book:
    def __init__(self, title, author, price):
        self.tilte = title
        self.author = author
        self.price = price
    
    def __str__(self):
        return f"Book title is {self.tilte}, author is {self.author} and costs {self.price}"
    
    def __repr__(self):
        return f"Book title is {self.tilte}, author is {self.author} and price is {self.price} using __repr__"

b1 = Book('mockingjay', 'suzana', 40)
b2 = Book('roya', 'salmi', 50)
print(b1)
print(repr(b1))