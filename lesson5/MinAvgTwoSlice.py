from random import random

a = [int(100 * random()) for i in range(30)]

def solution(A):
    p = prefix_sums(A)
    n = len(A)
    min_idx = 0
    min_value = 10001

    for i in range(n - 1):
        if i == 0:
            if p[1] / 2 < min_value:
                min_idx = 0
                min_value = p[1] / 2
            if len(p) > 2 and p[2] / 3 < min_value:
                min_idx = 0
                min_value = p[2] / 3
        else:
            if (p[i + 1] - p[i - 1]) / 2 < min_value:
                min_idx = i
                min_value = (p[i + 1] - p[i - 1]) / 2
                print(min_idx, min_value)
            if i < n - 2 and (p[i + 2] - p[i - 1]) / 3 < min_value:
                min_idx = i 
                min_value = (p[i + 2] - p[i - 1]) / 3
                print(min_idx, min_value)
    return min_idx

def prefix_sums(a):
    n = len(a)
    p = [0] * n
    for i in range(n):
        if i == 0:
            p[i] = a[i]
        else:
            p[i] = a[i] + p[i - 1]
    return p

# Every slice must be of size two or three. 
# Slices of bigger sizes are created from such smaller slices. 
# Therefore should any bigger slice have an optimal value, 
# all sub-slices must be the same, for this case to hold true. 
# Should this not be true, one of the sub-slices must be the optimal slice. 
# The others being bigger. Therefore we check all possible slices of size 2/3 
# and return the smallest one. The first such slice is the correct one, do not use <=!
# The description above are copied from https://www.martinkysel.com/codility-minavgtwoslice-solution/