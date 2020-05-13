N, M = map(int, input().split())

nums = sorted(list(map(int, input().split())))


def print_set(selected, toPick):
    if toPick == 0:
        print(*selected)
        return

    for i in range(N):
        print_set(selected+[nums[i]], toPick-1)


print_set([], M)
