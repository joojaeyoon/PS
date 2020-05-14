N = int(input())

mod = 10007

dp = [[0]*10 for _ in range(2)]

dp[0] = [1]*10

for i in range(1, N):
    for j in range(10):
        dp[i % 2][j] = sum(dp[(i-1) % 2][:j+1]) % mod

print(sum(dp[(N-1) % 2]) % mod)
