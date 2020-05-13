# 6603 로또


def select(nums, selected, last, toPick):

    if toPick == 0:
        print(*selected)
        return

    for i in range(last+1, len(nums)):
        selected.append(nums[i])
        select(nums, selected, i, toPick-1)
        selected.pop()


while True:
    nums = list(map(int, input().split()))

    if nums[0] == 0:
        break

    select(nums[1:], [], -1, 6)
    print()
