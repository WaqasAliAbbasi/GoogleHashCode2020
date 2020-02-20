import argparse
import random
from library import Library
from score import ni, nl
from utkarsh.main import printSquare as utkarshPrintSquare
from waqas.main import solve as waqasSolve
from divyansh.main import printSquare as divyanshPrintSquare
# inp is an input file as a single string
# return your output as a string


def parse(inp):
    itr = (line for line in inp.split('\n'))
    numberOfDifferentBooks, numberOfLibraries, numberOfDays = nl(itr)
    bookScores = {bookID: int(bookScore)
                  for bookID, bookScore in enumerate(nl(itr))}
    libraries = []
    for i in range(numberOfLibraries):
        numberOfBooks, signUpTime, capacityOfShipping = nl(itr)
        books = [bookID
                 for bookID in nl(itr)]
        libraries.append(Library(i, numberOfBooks, signUpTime,
                                 capacityOfShipping, books))
    return argparse.Namespace(numberOfDifferentBooks=numberOfDifferentBooks, numberOfLibraries=numberOfLibraries, numberOfDays=numberOfDays, bookScores=bookScores, libraries=libraries)


def solve(seed, inp, log):
    random.seed(seed)
    ns = parse(inp)
    print(ns)

    # ns.bookScores is a dictionary of bookID to bookScore
    # ns.libraries is a list of library instances (check library.py for details)
    # ns.numberOfDifferentBooks
    # ns.numberOfLibraries
    # ns.numberOfDays

    return waqasSolve(ns)
