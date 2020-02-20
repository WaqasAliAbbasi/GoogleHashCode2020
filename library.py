class Library:
    def __init__(self, numberOfBooks, signUpTime, capacityOfShipping, books):
        self.numberOfBooks = numberOfBooks
        self.signUpTime = signUpTime
        self.capacityOfShipping = capacityOfShipping
        self.books = books

    def __repr__(self):
        return "(Number of Books: {}, Sign Up Time: {}, Capacity of Shipping: {}, Total Books: {})".format(self.numberOfBooks, self.signUpTime, self.capacityOfShipping, len(self.books))
