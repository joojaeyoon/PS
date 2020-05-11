N, M = map(int, input().split())

nums = sorted(list(map(int, input().split())))


def print_set(selected, toPick):
    if toPick == 0:
        print(*selected)
        return

    last = -1

    for i in range(len(nums)):
        if nums[i] != last:
            last = nums[i]
            print_set(selected+[nums[i]], toPick-1)


print_set([], M)
