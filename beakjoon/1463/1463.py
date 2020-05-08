
N = int(input())

dp = [10000 for i in range(N+1)]

dp[1] = 0

for i in range(1, N):
    if i*3 < len(dp):
        dp[i*3] = min(dp[i]+1, dp[i*3])
    if i*2 < len(dp):
        dp[i*2] = min(dp[i]+1, dp[i*2])
    if i+1 < len(dp):
        dp[i+1] = min(dp[i]+1, dp[i+1])


print(dp[N])
