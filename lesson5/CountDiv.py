def solution(A, B, K):
    if A == B:
        return int(A % K == 0)
    elif A == 0:
        return B // K + 1
    else:
        return B // K  - (A - 1) // K