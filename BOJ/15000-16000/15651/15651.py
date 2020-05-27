N, M = map(int, input().split())


def print_set(arr, selected, toPick):
    if toPick == 0:
        print(*selected)
        return

    for i in range(N):
        print_set(arr, selected+[arr[i]], toPick-1)


print_set([i+1 for i in range(N)], [], M)
