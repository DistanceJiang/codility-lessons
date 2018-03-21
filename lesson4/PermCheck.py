def solution(A):
    reference = [0 for i in range(len(A))]
    for i in A:
        if i > len(A):
            return 0
        else:
            if reference[i - 1] == 0:
                reference[i - 1] = 1
            else:
                return 0
    return 1