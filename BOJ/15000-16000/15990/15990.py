
T = int(input())

mod = 1000000009

dp = [[0 for _ in range(3)] for __ in range(100000)]

dp[0][0] = 1
dp[1][1] = 1
dp[2][0], dp[2][1], dp[2][2] = 1, 1, 1

for i in range(3, 100000):
    for j in range(3):
        for k in range(3):
            if j != k:
                dp[i][j] = (dp[i][j]+dp[i-j-1][k]) % mod

for _ in range(T):
    n = int(input())

    print((dp[n-1][0]+dp[n-1][1]+dp[n-1][2]) % mod)
