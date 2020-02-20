import argparse
import random
from library import Library
from utkarsh.main import printSquare as utkarshPrintSquare
from waqas.main import solve as waqasSolve
from divyansh.main import printSquare as divyanshPrintSquare
# inp is an input file as a single string
# return your output as a string


def parse(inp):
    lines = inp.split('\n')
    numberOfDifferentBooks, numberOfLibraries, numberOfDays = map(
        int, lines[0].split())
    bookScores = {bookID: int(bookScore)
                  for bookID, bookScore in enumerate(lines[1].split(' '))}
    libraries = []
    for i in range(numberOfLibraries):
        line_number = 1 + i*2 + 1
        numberOfBooks, signUpTime, capacityOfShipping = map(
            int, lines[line_number].split())
        books = [int(bookID)
                 for bookID in lines[line_number + 1].split(' ')]
        libraries.append(Library(i, numberOfBooks, signUpTime,
                                 capacityOfShipping, books))
    return argparse.Namespace(numberOfDifferentBooks=numberOfDifferentBooks, numberOfLibraries=numberOfLibraries, numberOfDays=numberOfDays, bookScores=bookScores, libraries=libraries)


def solve(seed, inp, log):
    random.seed(seed)
    ns = parse(inp)

    # ns.bookScores is a dictionary of bookID to bookScore
    # ns.libraries is a list of library instances (check library.py for details)
    # ns.numberOfDifferentBooks
    # ns.numberOfLibraries
    # ns.numberOfDays

    return waqasSolve(ns)
