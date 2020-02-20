import argparse
from solve import parseInput


def ni(itr):
    return int(next(itr))

# parses the next string of itr as a list of integers


def nl(itr):
    return [int(v) for v in next(itr).split()]


# inp: the input file as a single string
# out: the answer file produced by your solver, as a single string
# return the score of the output as an integer


def score(inp, out):
    ns = parseInput(inp)
    itr = (line for line in out.split('\n'))
    numberOfLibrariesSignedUp = ni(itr)
    score = 0
    print(ns.numberOfDays)
    daysLeftForSignUp = ns.numberOfDays
    scannedBooks = set()
    for _ in range(numberOfLibrariesSignedUp):
        libraryID, totalBooks = nl(itr)
        library = ns.libraries[libraryID]
        print(library.signUpTime)
        daysLeftForSignUp -= library.signUpTime
        print(daysLeftForSignUp)
        print(library.capacityOfShipping)
        totalBooksForSigning = daysLeftForSignUp * library.capacityOfShipping
        for bookID in nl(itr)[:min(totalBooks, totalBooksForSigning)]:
            scannedBooks.add(bookID)
    return 0
