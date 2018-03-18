from random import random

a = list(int(20*random()) for i in range(20))

def solution(A):
    indicator = {}
    for i in A:
        if i > 0:
            indicator['{0}'.format(i)] = 1
    if len(indicator) == 0:
        return 1
    reference = sorted(list(int(i) for i in list(indicator.keys())))
    for i in range(len(reference)):
        if i+1 != reference[i]:
            return i+1
    return len(reference) + 1