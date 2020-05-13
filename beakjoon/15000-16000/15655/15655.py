N, M = map(int, input().split())

nums = sorted(list(map(int, input().split())))


def print_set(selected, prev, toPick):
    if toPick == 0:
        print(*selected)
        return

    for i in range(prev+1, N):
        print_set(selected+[nums[i]], i, toPick-1)


print_set([], -1, M)
