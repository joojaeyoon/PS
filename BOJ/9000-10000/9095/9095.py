
T = int(input())

nums = [1, 2, 3]

count = 0


def getCount(n, sumVal):

    global count

    if n < sumVal:
        return
    elif n == sumVal:
        count += 1
        return

    for i in range(3):
        getCount(n, sumVal+nums[i])


for _ in range(T):
    n = int(input())

    getCount(n, 0)

    print(count)
    count = 0
