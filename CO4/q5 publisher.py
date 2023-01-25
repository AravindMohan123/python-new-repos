class Publisher:
    def __init__(self,publisher_name):
        self.publisher_name = publisher_name

class Book(Publisher):
    def __init__(self,publisher_name,title,author):
        Publisher.__init__(self,publisher_name)
        self.title = title
        self.author = author

class Python(Book):
    def __init__(self,publisher_name,title,author,price,no_of_pages):
        Book.__init__(self,publisher_name,title,author)
        self.price = price
        self.no_of_pages = no_of_pages

publ = input("publisher name:")
tbook = input("books title")
author = input("author's name")
price = int(input("price of the book"))
pages   = int(input("No of pages"))

book1 = Python(publ,tbook,author,price,pages)

print(vars(book1))