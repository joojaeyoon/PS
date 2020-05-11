N, M = map(int, input().split())

nums = sorted(list(map(int, input().split())))
visited = [False for i in range(N)]


def print_set(selected, prev, toPick):
    if toPick == 0:
        print(*selected)
        return

    last = -1

    for i in range(prev+1, len(nums)):
        if not visited[i] and nums[i] != last:
            last = nums[i]
            visited[i] = True
            print_set(selected+[nums[i]], i, toPick-1)
            visited[i] = False


print_set([], -1, M)
