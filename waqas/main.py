from .util import square


def solve(ns):
    # ns.bookScores is a dictionary of bookID to bookScore
    # ns.libraries is a list of library instances (check library.py for details)
    # ns.numberOfDifferentBooks
    # ns.numberOfLibraries
    # ns.numberOfDays

    output = ""
    count = 0
    daysLeftForSignUp = ns.numberOfDays
    for _ in range(ns.numberOfLibraries):
        ns.libraries._reset(1000)
        _, library = ns.libraries.popitem()
        daysLeftForSignUp -= library.signUpTime
        if daysLeftForSignUp < 0:
            break
        count += 1
        output += "{} {}\n".format(library.libraryID,
                                   len(library.getBooksToBeScanned(daysLeftForSignUp)))
        output += " ".join([str(book.selectForScan().bookID)
                            for book in library.getBooksToBeScanned(daysLeftForSignUp)]) + "\n"
        for library in ns.libraries.values():
            library.setSelfWorth(daysLeftForSignUp)
    return "{}\n".format(count) + output
