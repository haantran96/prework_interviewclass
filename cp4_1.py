import math
def subtract(A):
    first_half = [A[i] for i in range(math.floor(len(A)/2))]
    second_half = [A[j] for j in range(math.floor(len(A)/2),len(A))]
    reversed_2nd = second_half[::-1]
    result = []
    for i in range(len(first_half)):
        result.append(reversed_2nd[i] - first_half[i])
    result.extend(second_half)
    return result