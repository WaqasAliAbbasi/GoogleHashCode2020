class Library:
    def __init__(self, libraryID, numberOfBooks, signUpTime, capacityOfShipping, books):
        self.libraryID = libraryID
        self.numberOfBooks = numberOfBooks
        self.signUpTime = signUpTime
        self.capacityOfShipping = capacityOfShipping
        self.books = books

    def __repr__(self):
        return "(ID: {}, Number of Books: {}, Sign Up Time: {}, Capacity of Shipping: {}, Total Books: {})".format(self.libraryID, self.numberOfBooks, self.signUpTime, self.capacityOfShipping, len(self.books))


class Book:
    def __init__(self, bookID, bookWorth):
        self.bookID = bookID
        self.bookWorth = bookWorth

    def __lt__(self, other):
        return self.bookWorth > other.bookWorth

    def __repr__(self):
        return "(ID: {}, Worth: {})".format(self.bookID, self.bookWorth)
