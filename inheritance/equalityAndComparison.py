# using __eq__ and __ge__ and __lt__

class Book:
    def __init__(self, title, author, price):
        self.tilte = title
        self.author = author
        self.price = price
    
    def __str__(self):
        return f"Book title is {self.tilte}, author is {self.author} and costs {self.price}"
    
    def __repr__(self):
        return f"Book title is {self.tilte}, author is {self.author} and price is {self.price} using __repr__"
    
    def __eq__(self, other):
        if not isinstance(other, Book):
            raise ValueError("can't compare to non book")
        return (self.tilte == other.tilte and self.author == other.author and self.price == other.price)
    
    def __ge__(self, other):
        if not isinstance(other, Book):
            raise ValueError("can't compare to non book")
        return self.price >= other.price

    def __lt__(self, other):
        if not isinstance(other, Book):
            raise ValueError("can't compare to non book")
        return self.price < other.price

class Newspaper:
    def __init__(self, title, author, price):
        self.tilte = title
        self.author = author
        self.price = price

b1 = Book('mockingjay', 'suzana', 50)
b2 = Book('roya', 'salmi', 40)
b3 = Book('mockingjay', 'suzana', 50)
n1 = Newspaper('mockingjay', 'suzana', 40)

print(b1 == b2)
print(b1 == b3)
#print(b1 == n1)  # it will give error because different class compare
print(b1 >= b2)
print(b2 < b1)

