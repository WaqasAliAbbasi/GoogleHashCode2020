class Library:
    def __init__(self, libraryID, numberOfBooks, signUpTime, capacityOfShipping, books, days):
        self.libraryID = libraryID
        self.numberOfBooks = numberOfBooks
        self.signUpTime = signUpTime
        self.capacityOfShipping = capacityOfShipping
        self.books = books
        self.isSignedUp = False
        self.worth = self.setSelfWorth(days)

    def __lt__(self, other):
        return self.worth > other.worth

    def setSelfWorth(self, days):
        if self.isSignedUp:
            shippingDays = days
        else:
            shippingDays = days - self.signUpTime

        booksToBeScanned = self.getBooksToBeScanned(shippingDays)
        self.worth = sum([book.bookWorth for book in booksToBeScanned])
        return self.worth

    def getBooksToBeScanned(self, shippingDays):
        noOfBooksThatCanBeScanned = self.capacityOfShipping*shippingDays
        self.sortBookList()
        return self.books[:noOfBooksThatCanBeScanned]

    def sortBookList(self):
        cbr = self.numberOfBooks ** (1/3)
        self.books._reset(cbr)

    def signUpLibrary(self):
        self.isSignedUp = True

    def __repr__(self):
        return "(ID: {}, Number of Books: {}, Sign Up Time: {}, Capacity of Shipping: {}, Total Books: {})".format(self.libraryID, self.numberOfBooks, self.signUpTime, self.capacityOfShipping, len(self.books))


class Book:
    def __init__(self, bookID, bookWorth):
        self.bookID = bookID
        self.bookWorth = bookWorth
        self.scanned = False

    def selectForScan(self):
        self.scanned = True
        return self

    def getWorth(self):
        if self.scanned:
            return 0
        else:
            return self.bookWorth

    def __lt__(self, other):
        return self.getWorth() > other.getWorth()

    def __repr__(self):
        return "(ID: {}, Worth: {}, Scanned: {})".format(self.bookID, self.getWorth(), self.scanned)
