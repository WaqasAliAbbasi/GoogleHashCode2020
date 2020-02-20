from .util import square


def solve(ns):
    # ns.bookScores is a dictionary of bookID to bookScore
    # ns.libraries is a list of library instances (check library.py for details)
    # ns.numberOfDifferentBooks
    # ns.numberOfLibraries
    # ns.numberOfDays

    output = ""
    for library in ns.libraries:
        output += "{} {}\n".format(library.libraryID, len(library.books))
    print(output)
