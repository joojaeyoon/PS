import sys

n = int(input())

wine = []
dp = [0 for _ in range(n)]

for _ in range(n):
    wine.append(int(sys.stdin.readline()))


def solution():
    if n == 1:
        print(wine[0])
        return

    dp[0] = wine[0]
    dp[1] = wine[0]+wine[1]

    for i in range(2, n):
        dp[i] = max(dp[i-2]+wine[i], wine[i]+wine[i-1]+dp[i-3], dp[i-1])

    print(dp[-1])


solution()
