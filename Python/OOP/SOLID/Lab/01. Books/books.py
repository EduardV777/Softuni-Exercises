"""
[Single Responsibility Principle]
Refactor the provided code,
so there is a separate class called Library,
which contains books and has a method called find_book(title) that returns the book with the given title.
Remove the unnecessary code from the Book class.
"""


class Book:
    def __init__(self, title, author, location, bookLength):
        self.title = title
        self.author = author
        self.location = location
        self.pagesContents = []
        
        for k in range(0, bookLength):
            self.pagesContents.append([])


    def __len__(self):
        #return book length
        return len(self.pagesContents)

    def __getitem__(self, ind):
        if ind < len(self.pagesContents):
            return self.pagesContents[ind]
        else:
            return "---Page not found!---"

    def __setitem__(self, ind, value):
        if ind < len(self.pagesContents):
            self.pagesContents[ind] = value
        else:
            return "---Page not found!---"

class Library:

    def __init__(self):
        self.books = []

    def find_book(self, title):

        for k in range(0, len(self.books)):

            if self.books[k].title == title:
                return self.books[k]

    def add_book(self, book: Book):
        for k in range(0, len(self.books)):
            if self.books[k].title == book.title:
                return -1
        
        self.books.append(book)


class ReadBook:

    def __init__(self, bookName, library: Library):
        self.openBook = bookName
        self.err = 1

        for k in range(0, len(library.books)):
            if library.books[k].title == bookName:
                self.openBook = library.books[k]
                self.err = 0

        if self.err == 1:
            raise ValueError("Book not found!")

    def turn_page(self, page):
        return self.openBook[page - 1]

class ModifyBookContents:

    def __init__(self, bookName, library: Library):
        self.bookToModify = bookName
        self.err = 1

        for k in range(0, len(library.books)):
            if library.books[k].title == bookName:
                self.bookToModify = library.books[k]
                self.err = 0
        
        if self.err == 1:
            raise ValueError("Book not found")
        

    def addContentsAtPage(self, contents, page: int):
        self.bookToModify[page - 1] = contents



library = Library()
newBook = Book('We are all dreams', 'Unknown', 'Bulgaria', 650)
library.add_book(newBook)
bookModify = ModifyBookContents("We are all dreams", library)
bookModify.addContentsAtPage("Contents to be added", 1)
bookRead = ReadBook("We are all dreams", library)
print(bookRead.turn_page(1))