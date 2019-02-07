class User(object):
    def __init__(self, name, email):
        self.email = email
        self.name = name
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("{name}'s email has been changed.".format(name=self.name))

    def __repr__(self):
        return "User, {name}, with email {email} has read {num} books.".format(name=self.name, email=self.email, num=len(self.books))

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        total = 0
        for value in self.books.values():
            if type(value) == 'num':
                total += value
        return total / len(self.books)


class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn

    def set_isbn(self, number):
        self.isbn = number
        print("{name}'s isbn has been changed.".format(name=self.title))

    def add_rating(self, new_rating):
        if new_rating >= 0 and new_rating <= 4:
            self.ratings.append(new_rating)
        else:
            print("Invalid rating")

    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn

    def get_average_rating(self):
        total = 0
        for rating in self.ratings:
            total += rating
        return total / len(self.ratings)

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)


class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        return new_book

    def create_novel(self, title, author, isbn):
        new_novel = Fiction(title, author, isbn)
        return new_novel

    def create_non_fiction(self, title, subject, level, isbn):
        new_non_fiction = Non_Fiction(title, subject, level, isbn)
        return new_non_fiction

    def add_book_to_user(self, book, email, rating=None):
        user = self.users[email]
        if email in self.users:
            user.read_book(book, rating)
            if rating != None:
                book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with email {email}".format(email=email))
    
    def add_user(self, name, email, user_books=None):
        new_user = User(name, email)
        self.users[email] = new_user 
        if user_books != None:
            for book in user_books:
                self.add_book_to_user(book, email)
                
    def print_catalog(self):
        for key in self.books.keys():
            print(key)

    def print_users(self):
        for value in self.users.values():
            print(value)

    def most_read_book(self):
        most = 0
        fav_book = ''
        for key, value in self.books.items():
            if value > most:
                most = value
                fav_book = key
        return fav_book

    def highest_rated_book(self):
        highest = 0
        high_book = ''
        for book in self.books.keys():
            if book.get_average_rating() > highest:
                highest = book.get_average_rating()
                high_book = book
        return high_book

    def most_positive_user(self):
        positive = 0
        for value in self.users.values():
            if value.get_average_rating() > positive:
                positive = value.get_average_rating()
        return value