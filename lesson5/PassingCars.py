a = [0, 1, 0, 1, 1]
b = [1, 1, 1, 0, 0, 1, 1, 1, 0]

def solution(A):
    increament = 0
    result = 0
    for i in A:
        if i == 0:
            increament += 1
        else:
            result += increament
            if result > 1e9:
                return -1
    return result