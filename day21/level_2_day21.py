class book:
    def __init__(self,avtor,book_name,pages):
        self.avtor=avtor
        self.book_name=book_name
        self.pages=pages
    def description_book(self):
        return(f'avtor of the book:{self.avtor},name of the bookP{self.book_name},has {self.pages} pages')
firstbook=book('me','book123',300)
print(firstbook.description_book())