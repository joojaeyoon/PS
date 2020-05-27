N = int(input())

dp = [[0]*10 for _ in range(2)]

mod = 1000000000

dp[0] = [0]+[1]*9

for i in range(1, N+1):
    prev = (i-1) % 2
    dp[i % 2][0] = dp[prev][1]
    dp[i % 2][9] = dp[prev][8]
    for j in range(1, 9):
        dp[i % 2][j] = (dp[prev][j-1] + dp[prev][j+1]) % mod

print(sum(dp[(N-1) % 2]) % mod)
