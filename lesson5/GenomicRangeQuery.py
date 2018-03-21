S = 'CAGCCTA'
P = [2, 5, 0]
Q = [4, 5, 6]

def solution(S, P, Q):
    transposed = []
    for i in S:
        if i == 'A':
            transposed.append([1, 0, 0, 0])
        elif i == 'C':
            transposed.append([0, 1, 0, 0])
        elif i == 'G':
            transposed.append([0, 0, 1, 0])
        else:
            transposed.append([0, 0, 0, 1])
    for i in range(len(transposed) - 1):
        for j in range(4):
            transposed[i + 1][j] += transposed[i][j]
    result = []
    for i in range(len(P)):
        x = P[i]
        y = Q[i]
        sub = 0
        for j in range(4):
            if x >= 1:
                sub = transposed[x - 1][j]
            if transposed[y][j] - sub > 0:
                result.append(j + 1)
                break
    return result

# Note: This solution was not initially thought by me. I actually googled this problem, and find this blog(https://rafal.io/posts/codility-genomic-range-query.html) very useful.