def num_range(A, B, C):
    n = len(A)
    sets = []

    for i in range(n):
        total = 0
        j = i

        while total < B and j < n:
            total += A[j]
            j += 1

        while total >= B and total <= C and j <= n:
            if total <= C:
                sets.append(A[i:j])
            if j < n:
                total += A[j]
            j += 1

    return len(sets)

