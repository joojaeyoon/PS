
N = int(input())


def getCount(n, dp):

    if n <= 1:
        return dp[n]

    if len(dp) > n:
        return dp[n]

    n1 = getCount(n-1, dp)
    n2 = getCount(n-2, dp)

    dp.append([n1[0]+n2[0], n1[1] + n2[1]])

    return dp[-1]


for i in range(N):
    count = int(input())

    dp = [[1, 0], [0, 1]]

    result = getCount(count, dp)

    c0, c1 = result

    print(c0, c1)
