
N = int(input())
P = list(map(int, input().split()))

dp = [0 for _ in range(N+1)]


for i in range(N):
    for j in range(i+1):
        dp[i] = max(dp[i-j-1]+P[j], dp[i])
print(dp[N-1])
