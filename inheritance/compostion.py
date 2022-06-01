# using composition to build complex object

from unittest import result


class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price
        self.author = author
        self.chapters = list()

    def addChapter(self, chapter):
        self.chapters.append(chapter)
        
    def getBookPageCount(self):
        result = 0
        for ch in self.chapters:
            result += ch.pageCount
        return result
        
class Author:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def __str__(self):
        return f"{self.firstName} {self.lastName} "

class Chapter:
    def __init__(self, name, pageCount):
        self.name = name
        self.pageCount = pageCount
  

auth = Author('Leo', 'Tolstoy')
b1 = Book("war and peace", 39, auth)
b1.addChapter(Chapter('chapter 1', 323))
b1.addChapter(Chapter('chapter 2', 123))
b1.addChapter(Chapter('chapter 3', 432))
print(b1.getBookPageCount())
print(b1.title)
print(b1.author)
print(b1.author.firstName)
'salman'
