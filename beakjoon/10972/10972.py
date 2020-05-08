N = int(input())

permutation = list(map(int, input().split()))


def next_permutation(permutation):
    bp = -1

    for i in range(len(permutation)-1, 0, -1):
        if permutation[i-1] < permutation[i]:
            bp = i-1
            break

    if bp == -1:
        print(-1)
        return

    idx = bp+1
    for i in range(bp+1, len(permutation)):
        if permutation[i] > permutation[bp] and permutation[i] < permutation[idx]:
            idx = i

    permutation[bp], permutation[idx] = permutation[idx], permutation[bp]
    permutation = permutation[:bp+1]+sorted(permutation[bp+1:])

    for i in permutation:
        print(i, end=" ")

    return


next_permutation(permutation)
