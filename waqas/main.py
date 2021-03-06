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
        ns.libraries._reset(ns.numberOfLibraries**(1/3))
        library = ns.libraries.pop()
        daysLeftForSignUp -= library.signUpTime
        if daysLeftForSignUp < 0:
            break
        if len(library.getBooksToBeScanned(daysLeftForSignUp, sort=False)) < 1:
            break
        count += 1
        output += "{} {}\n".format(library.libraryID,
                                   len(library.getBooksToBeScanned(daysLeftForSignUp, sort=False)))
        output += " ".join([str(book.selectForScan().bookID)
                            for book in library.getBooksToBeScanned(daysLeftForSignUp)]) + "\n"
        for library in ns.libraries:
            library.setSelfWorth(daysLeftForSignUp)
    return "{}\n".format(count) + output
