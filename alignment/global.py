import numpy
import unittest
import pprint
import sys
from collections import deque

lines = sys.stdin.readlines()
first = lines[1].strip('\n')
second = lines[3].strip('\n')

matrix = numpy.zeros((len(first) + 1, len(second) + 1), dtype=numpy.int)

for ver in range(len(first) + 1):
    matrix[ver][0] = -ver
for hor in range(len(second) + 1):
    matrix[0][hor] = -hor

# main loop
for ver in range(1, len(first) + 1):
    for hor in range(1, len(second) + 1):
        matrix[ver][hor] = max(matrix[ver - 1][hor - 1] + (1 if first[ver - 1] == second[hor - 1] else -1),
                           matrix[ver - 1][hor] - 1,
                           matrix[ver][hor - 1] - 1)

# debug purposes 
#print('     ', *second, sep='  ')
#print(*first, sep='\n')    
#print(matrix, file=sys.stderr)

#print final answer
print(matrix[len(first)][len(second)])

def PrintSubAnswer(hor, ver, first_history, second_history):
    #print(f'hor = {hor}\nver = {ver}\nfirst_history = {first_history}\nsecond_history = {second_history}\n\n')
    if hor == 0 and ver == 0:
        print(first_history, second_history, sep='\n')
        return
    
    if hor == 0:
        print(first[0:ver] + first_history, '-' * ver + second_history, sep='\n')
        return

    if ver == 0:
        print('-' * hor + first_history, second[0:hor] + second_history, sep='\n')
        return

    if matrix[ver - 1][hor - 1] + (1 if first[ver - 1] == second[hor - 1] else -1) == matrix[ver][hor]:
        if first[ver - 1] == second[hor - 1]:
            PrintSubAnswer(hor - 1, ver - 1, first[ver - 1] + first_history, second[hor - 1] + second_history)
        else:
            PrintSubAnswer(hor - 1, ver - 1, first[ver - 1].lower() + first_history, second[hor - 1].lower() + second_history)

    if matrix[ver - 1][hor] - 1 == matrix[ver][hor]:
        PrintSubAnswer(hor, ver - 1, first[ver - 1] + first_history, '-' + second_history)

    if matrix[ver][hor - 1] - 1 == matrix[ver][hor]:
        PrintSubAnswer(hor - 1, ver, '-' + first_history, second[hor - 1] + second_history)

PrintSubAnswer(len(second), len(first), '', '')