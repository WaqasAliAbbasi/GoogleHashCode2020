import argparse
import random
from score import parse
from utkarsh.main import printSquare as utkarshPrintSquare
from waqas.main import printSquare as waqasPrintSquare
from divyansh.main import printSquare as divyanshPrintSquare
# inp is an input file as a single string
# return your output as a string


def solve(seed, inp, log):
    random.seed(seed)
    ns = parse(inp)

    # ns.bookScores is a dictionary of bookID to bookScore
    # ns.libraries is a list of library instances (check library.py for details)
    # ns.numberOfDifferentBooks
    # ns.numberOfLibraries
    # ns.numberOfDays

    print(ns)

    # TODO: Solve the problem

    return '0'
