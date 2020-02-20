from .util import square


import operator
from math import ceil


def input_vals():
    numOfBooks = int(input())
    numOfLib = int(input())
    numOfDays = int(input())
    # worth_multimap = []
    worth = []
    library = []
    for i in range(numOfBooks):
        x = int(input())
        worth.append(x)
        # worth_multimap[x].append(i)
    for i in range(numOfLib):
        book = int(input())
        signup = int(input())
        rate = int(input())
        id = i
        bookList = []
        for j in range(book):
            x = int(input())
            bookList.append(x)
        library.append([book, signup, rate, id, bookList])
    return numOfBooks, numOfLib, numOfDays, worth, library


def solve(numOfBooks, numOfLib, numOfDays, worth, library12):
    library12.sort(key=operator.itemgetter(0), reverse=True)
    library12.sort(key=operator.itemgetter(1))
    library12.sort(key=operator.itemgetter(2))
    count = 0
    output = ""
    for i in library12:
        if i[1] + ceil(i[0] / i[2]) < numOfDays:
            output += str(i[3]) + " " + str(i[0]) + '\n'
            for j in i[4]:
                output += str(j) + " "
                worth[j] = 0
        elif i[1] >= numOfDays:
            continue
        else:
            leftover = numOfDays * i[2]
            output += str(i[3]) + " " + str(leftover) + '\n'
            temp = []
            for j in i[4]:
                temp.append([worth[j], j])
            temp.sort(key=operator.itemgetter(0), reverse=True)
            temp = temp[:leftover]
            for x, y in temp:
                output += str(y) + " "
                worth[y] = 0
        count += 1
        numOfDays -= i[1]
        output += '\n'

    file1 = open('op.txt','w')
    file1.write(str(count)+'\n')
    file1.write(output)


if __name__ == '__main__':
    numOfBooks, numOfLib, numOfDays, worth, library12 = input_vals()
    solve(numOfBooks, numOfLib, numOfDays, worth, library12)

