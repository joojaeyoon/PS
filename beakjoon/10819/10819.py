
from itertools import permutations


def getResult(nums):
    total = 0

    for i in range(len(nums)-1):
        total += abs(nums[i]-nums[i+1])

    return total


N = int(input())

nums = list(map(int, input().split()))

max_total = 0

for p in permutations(nums):
    max_total = max(getResult(p), max_total)

print(max_total)
