N, K = map(int, input().split())

dp = [[0 for __ in range(201)] for _ in range(201)]

dp[0] = [1 for _ in range(201)]

mod = 1000000000

for i in range(1, N+1):
    for j in range(1, K+1):
        dp[i][j] = (dp[i][j-1]+dp[i-1][j]) % mod

print(dp[N][K])
