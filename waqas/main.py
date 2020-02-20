from .util import square


def solve(ns):
    # ns.bookScores is a dictionary of bookID to bookScore
    # ns.libraries is a list of library instances (check library.py for details)
    # ns.numberOfDifferentBooks
    # ns.numberOfLibraries
    # ns.numberOfDays

    output = "{}\n".format(ns.numberOfLibraries)
    for library in ns.libraries.values():
        output += "{} {}\n".format(library.libraryID, len(library.books))
        output += " ".join(map(str, library.books)) + "\n"
    return output
