N = int(input())

dp = [[0, 0], [0, 0]]

dp[0] = [0, 1]

for i in range(1, N):
    dp[i % 2][0] = dp[(i-1) % 2][0]+dp[(i-1) % 2][1]
    dp[i % 2][1] = dp[(i-1) % 2][0]

print(sum(dp[(N-1) % 2]))
