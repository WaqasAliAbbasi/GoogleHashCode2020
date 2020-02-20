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
    daysLeftForSignUp = ns.numberOfDays
    scannedBooks = {}
    for _ in range(numberOfLibrariesSignedUp):
        libraryID, totalBooks = nl(itr)
        library = ns.libraries[libraryID]
        daysLeftForSignUp -= library.signUpTime
        if daysLeftForSignUp <= 0:
            break
        totalBooksForSigning = daysLeftForSignUp * library.capacityOfShipping
        for bookID in nl(itr)[:min(totalBooks, totalBooksForSigning)]:
            if bookID not in scannedBooks:
                score += ns.bookScores[bookID]
                scannedBooks[bookID] = True
    return score
