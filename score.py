import argparse
from library import Library


def ni(itr):
    return int(next(itr))

# parses the next string of itr as a list of integers


def nl(itr):
    return [int(v) for v in next(itr).split()]


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
        libraries.append(Library(numberOfBooks, signUpTime,
                                 capacityOfShipping, books))
    return argparse.Namespace(numberOfDifferentBooks=numberOfDifferentBooks, numberOfLibraries=numberOfLibraries, numberOfDays=numberOfDays, bookScores=bookScores, libraries=libraries)

# inp: the input file as a single string
# out: the answer file produced by your solver, as a single string
# return the score of the output as an integer


def score(inp, out):
    ns = parse(inp)
    itr = (line for line in out.split('\n'))
    # TODO: implement

    return 0
