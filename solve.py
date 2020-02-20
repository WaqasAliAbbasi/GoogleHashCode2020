import argparse
import random
from library import Library, Book
from sortedcontainers import SortedList
from utkarsh.main import printSquare as utkarshPrintSquare
from waqas.main import solve as waqasSolve
from divyansh.main import printSquare as divyanshPrintSquare
# inp is an input file as a single string
# return your output as a string


def ni(itr):
    return int(next(itr))

# parses the next string of itr as a list of integers


def nl(itr):
    return [int(v) for v in next(itr).split()]


def parseInput(inp):
    itr = (line for line in inp.split('\n'))
    numberOfDifferentBooks, numberOfLibraries, numberOfDays = nl(itr)
    bookScores = {bookID: int(bookScore)
                  for bookID, bookScore in enumerate(nl(itr))}
    libraries = {}
    for i in range(numberOfLibraries):
        numberOfBooks, signUpTime, capacityOfShipping = nl(itr)
        books = SortedList(Book(bookID, bookScores[bookID])
                           for bookID in nl(itr))
        libraries[i] = Library(i, numberOfBooks, signUpTime,
                               capacityOfShipping, books)
    return argparse.Namespace(numberOfDifferentBooks=numberOfDifferentBooks, numberOfLibraries=numberOfLibraries, numberOfDays=numberOfDays, bookScores=bookScores, libraries=libraries)


def solve(seed, inp, log):
    random.seed(seed)
    ns = parseInput(inp)
    # ns.bookScores is a dictionary of bookID to bookScore
    # ns.libraries is a dictionary of libraryID to library instances (check library.py for details)
    # ns.numberOfDifferentBooks
    # ns.numberOfLibraries
    # ns.numberOfDays

    return waqasSolve(ns)
