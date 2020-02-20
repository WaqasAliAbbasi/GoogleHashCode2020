import argparse
from library import Library


def ni(itr):
    return int(next(itr))

# parses the next string of itr as a list of integers


def nl(itr):
    return [int(v) for v in next(itr).split()]


def parse(inp):
    return 'a'

# inp: the input file as a single string
# out: the answer file produced by your solver, as a single string
# return the score of the output as an integer


def score(inp, out):
    ns = parse(inp)
    itr = (line for line in out.split('\n'))
    print(nl(itr))

    return 0
