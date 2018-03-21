from random import random

a = [3, 4, 4, 6, 1, 4, 4]
b = list(int(100 * random()) for i in range(100))

def solution(N, A):
    counters = {}
    max_recorder = 0
    for i in A:
        if 1 <= i <= N:
            if i in [int(j) for j in counters.keys()]:
                counters['{0}'.format(i)] += 1
            else:
                counters['{0}'.format(i)] = 1
        elif i == N + 1 and len(counters.values()) != 0:
            max_recorder += max(counters.values())
            counters = {}
    result = [0] * N
    for i in range(N):
        if i + 1 in [int(j) for j in counters.keys()]:
            result[i] = counters['{0}'.format(i + 1)] + max_recorder
        else:
            result[i] = max_recorder
    return result
    
