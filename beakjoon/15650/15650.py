N, M = map(int, input().split())


def print_set(arr, selected, prev, toPick):

    if toPick == 0:
        print(*selected)
        return

    for i in range(prev+1, len(arr)):
        print_set(arr, selected+[arr[i]], i, toPick-1)


print_set([i+1 for i in range(N)], [], -1, M)
