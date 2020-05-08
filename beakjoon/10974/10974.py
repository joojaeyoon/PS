def next_permutation(perm):
    bp = -1

    for i in range(len(perm)-1, 0, -1):
        if perm[i-1] < perm[i]:
            bp = i-1
            break

    if bp == -1:
        return -1

    idx = bp+1
    for i in range(bp+1, len(perm)):
        if perm[i] > perm[bp] and perm[i] < perm[idx]:
            idx = i

    perm[bp], perm[idx] = perm[idx], perm[bp]
    perm = perm[:bp+1]+sorted(perm[bp+1:])

    print(*perm)

    return perm


N = int(input())

permutation = [i+1 for i in range(N)]

print(*permutation)

while True:

    permutation = next_permutation(permutation)

    if permutation == -1:
        break
