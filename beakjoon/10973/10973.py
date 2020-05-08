N = int(input())

permutation = list(map(int, input().split()))


def prev_permutation(perm):
    bp = -1

    for i in range(len(perm)-1, 0, -1):
        if perm[i-1] > perm[i]:
            bp = i-1
            break

    if bp == -1:
        print(-1)
        return

    idx = bp
    for i in range(bp+1, len(perm)):
        if perm[i] < perm[bp]:
            idx = i

    perm[bp], perm[idx] = perm[idx], perm[bp]
    perm = perm[:bp+1]+sorted(perm[bp+1:], reverse=True)

    for i in perm:
        print(i, end=" ")

    return


prev_permutation(permutation)
