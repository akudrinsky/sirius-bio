import numpy
import unittest
import sys

def CountLocalAlignment(first, second, elemScore=lambda a, b:  1 if a == b else -1, emptySymbol='-'):
    '''Smith-Waterman algo
    
    returns list:
    - first str optimal position
    - second str optimal position
    - score
    '''

    matrix = numpy.zeros((len(first) + 1, len(second) + 1), dtype=int)

    # main loop
    for i in range(1, len(first) + 1):
        for j in range(1, len(second) + 1):
            matrix[i][j] = max(matrix[i - 1][j - 1] + elemScore(first[i - 1], second[j - 1]),
                               matrix[i - 1][j] + elemScore(first[i - 1], '-'),
                               matrix[i][j - 1] + elemScore('-', second[j - 1]),
                               0,
                               )

    # debug purposes
    print(matrix)

    maxValue = matrix.max()
    maxLen = max(len(first), len(second))

    result = numpy.where(matrix == numpy.amax(matrix))
    result = list(zip(result[0], result[1]))[0]
    print(result[0], result[1])

    retValue = [[], [], matrix[result[0]][result[1]]]

    i = result[0]
    j = result[1]

    while matrix[i][j] > 0:
        if matrix[i][j] == matrix[i - 1][j - 1] + elemScore(first[i - 1], second[j - 1]):
            if first[i - 1] != second[j - 1]:
                retValue[0].append(first[i - 1].lower())
                retValue[1].append(second[j - 1].lower())
            else:
                retValue[0].append(first[i - 1])
                retValue[1].append(second[j - 1])
            i -= 1
            j -= 1
            # print('diag')
        elif matrix[i][j] == matrix[i - 1][j] + elemScore(first[i - 1], '-'):
            retValue[0].append(first[i - 1])
            retValue[1].append(emptySymbol)
            i -= 1
            # print('first')
        elif matrix[i][j] == matrix[i][j - 1] + elemScore('-', second[j - 1]):
            retValue[0].append(emptySymbol)
            retValue[1].append(second[j - 1])
            j -= 1
            # print('second')
        else:
            raise Exception()
    
    retValue[0].reverse()
    retValue[1].reverse()
    retValue[0] = ''.join(retValue[0])
    retValue[1] = ''.join(retValue[1])

    return retValue
    
lines = sys.stdin.readlines()
strOne = lines[1].strip()
strTwo = lines[3].strip()
print(CountLocalAlignment(strOne, strTwo))