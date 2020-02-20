class Library:
    def __init__(self, libraryID, numberOfBooks, signUpTime, capacityOfShipping, books):
        self.libraryID = libraryID
        self.numberOfBooks = numberOfBooks
        self.signUpTime = signUpTime
        self.capacityOfShipping = capacityOfShipping
        self.books = books

    def __repr__(self):
        return "(ID: {}, Number of Books: {}, Sign Up Time: {}, Capacity of Shipping: {}, Total Books: {})".format(self.libraryID, self.numberOfBooks, self.signUpTime, self.capacityOfShipping, len(self.books))
