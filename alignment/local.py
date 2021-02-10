import numpy
import unittest
import pprint
import sys
from collections import deque

lines = sys.stdin.readlines()
first = lines[1].strip('\n')
second = lines[3].strip('\n')

matrix = numpy.zeros((len(first) + 1, len(second) + 1), dtype=numpy.int)

# main loop
for ver in range(1, len(first) + 1):
    for hor in range(1, len(second) + 1):
        matrix[ver][hor] = max(matrix[ver - 1][hor - 1] + (1 if first[ver - 1] == second[hor - 1] else -1),
                           matrix[ver - 1][hor] - 1,
                           matrix[ver][hor - 1] - 1,
                           0)

# debug purposes 
#print('     ', *second, sep='  ')
#print(*first, sep='\n')    
print(matrix, file=sys.stderr)

#print final answer
print(matrix.max())

def PrintSubAnswer(hor, ver, first_history, second_history):
    #print(f'hor = {hor}\nver = {ver}\nfirst_history = {first_history}\nsecond_history = {second_history}\n\n')
    
    if matrix[ver, hor] == 0:
        if hor > ver:
            #second is bigger
            print('-' * (hor - ver) + first[0:ver].lower() + first_history, 
                second[0:hor].lower() + second_history, 
                sep='\n')
        else:
            #first is bigger
            print(first[0:ver].lower() + first_history, 
                '-' * (ver - hor) + second[0:hor].lower() + second_history, 
                sep='\n')
        exit(0)

    if matrix[ver - 1][hor - 1] + (1 if first[ver - 1] == second[hor - 1] else -1) == matrix[ver][hor]:
        if first[ver - 1] == second[hor - 1]:
            PrintSubAnswer(hor - 1, ver - 1, first[ver - 1] + first_history, second[hor - 1] + second_history)
        else:
            PrintSubAnswer(hor - 1, ver - 1, first[ver - 1].lower() + first_history, second[hor - 1].lower() + second_history)

    if matrix[ver - 1][hor] - 1 == matrix[ver][hor]:
        PrintSubAnswer(hor, ver - 1, first[ver - 1] + first_history, '-' + second_history)

    if matrix[ver][hor - 1] - 1 == matrix[ver][hor]:
        PrintSubAnswer(hor - 1, ver, '-' + first_history, second[hor - 1] + second_history)

result = numpy.where(matrix == numpy.amax(matrix))
result = list(zip(result[0], result[1]))[0]
print(result[0], result[1])

if len(first[result[1] - 1::])

PrintSubAnswer(result[1], result[0], first[result[1] - 1::], second[result[0] - 1::])