from .user import User

class Library:

    def __init__(self):
        self.user_records = []
        self.books_available = {} #authors: [str]
        self.rented_books = {} #usernames: {bookname: daysToReturn}
    
    def get_book(self, author, book_name: str, days_to_return: int, user: User):
        for user in self.rented_books:
            currBooks = self.rented_books[user].keys()
            if book_name in currBooks:
                return f"The book \"{book_name}\" is already rented and will be available in {self.rented_books[user][book_name]} days!"
        
        for author in self.books_available:
            for book in self.books_available[author]:
                if book == book_name:
                    if not user.username in self.rented_books:
                        self.rented_books[user.username] = {book_name: days_to_return}
                    else:
                        self.rented_books[user.username][book_name] = days_to_return

                    user.books.append(book_name)
                    bookId = self.books_available[author].index(book_name)
                    del self.books_available[author][bookId]
                    return f"{book_name} successfully rented for the next {days_to_return} days!"


    def return_book(self, author: str, book_name: str, user: User):
        if book_name in user.books:
            self.books_available[author].append(book_name)
            del self.rented_books[user.username][book_name]
            bookId = user.books.index(book_name)
            del user.books[bookId]
        else:
            return f"{user.username} doesn't have this book in his/her records!"
